from netCDF4 import Dataset
import numpy
from datetime import datetime, timedelta

class Ragged():
    '''
    object to represent a ragged array, with some helper functions.
    '''

    def __init__(self, filename):
        '''
        filename: name of netcdf file containing wod profiles
        '''
        self.rootgrp = Dataset(filename, "r", format="NETCDF4")

    def ncasts(self):
        return self.rootgrp.dimensions['casts'].size

    def variables(self):
        return self.rootgrp.variables

    def attributes(self):
        return self.rootgrp.ncattrs()

    def get_global_attr(self, attr):
        # unpack a global attribute from this ragged array.
        if attr in self.attributes():
            return self.rootgrp.getncattr(attr)
        else:
            print('Attribute ' + attr + ' not found in this ragged array. Valid options are: ')
            print(self.attributes())
            return None

class Profile():
    '''
    object to represent a single wodpy-compatible profile object
    '''

    ## generic helpers and format mungers

    def __init__(self, ragged, index):
        '''
        ragged: a Ragged object
        index: index of cast from Ragged object to turn into a profile
        '''

        self.r = ragged
        self.i = index

    def decode_bytearray(self, bytearray):
        '''
        decode a numpy masked array of bytes into a regular string
        '''

        return ''.join([a.decode('UTF-8') for i, a in enumerate(bytearray) if not bytearray.mask[i]])

    def determine_offset(self, var):
        '''
        determine the offset in the list of measurements for <var> where this profile's data begins
        '''

        previous = self.r.variables()[var][0:self.i]
        if not previous.mask is numpy.ma.nomask:
            return sum([int(a) for i, a in enumerate(previous) if not previous.mask[i]])
        else:
            return sum([int(a) for a in previous])

    def locate_in_ragged(self, v):
        '''
        returns (offset, nentries) for variable v to extract it for this profile from the raggedarray.
        '''
        offset = self.determine_offset(v+'_row_size')
        nentries = self.metadata(v+'_row_size')
        return offset, nentries

    ## profile metadata

    def metadata(self, metadata_key):
        # hardcoded list for now since per-profile and per-level variables are all in the same
        # netCDF variables list, but this function is only appropriate for per-profile info.
        # would like to see this autodetected in future.
        # furthermore splitting out into vars noted in the spec docs, and other vars I'm seeing
        # in data downloaded from NOAA; should converge as spec is finalized?
        spec_vars = ['Access_no', 'Bottom_Depth', 'Cast_Direction', 'country', 'dataset', 'date', 'dbase_orig',
                     'GMT_time', 'time', 'real_time', 'Orig_Stat_Num', 'originators_cruise_identifier'
                     'Recorder', 'Platform', 'WOD_cruise_identifier', 'wod_unique_cast', 'crs', 'lat', 'lon',
                     'Pressure_row_size', 'z_row_size', 'Temperature_Instrument', 'Temperature_row_size',
                     'Temperature_WODprofileflag', 'Salinity_row_size', 'Salinity_WODprofileflag',
                     'Oxygen_row_size', 'Oxygen_WODprofileflag']
        novel_vars = ['Temperature_WODflag', 'z_WODflag', 'needs_z_fix', 'Bottom_Hit', 'depth_eq', 'Dry_Bulb_Temp', 'Wind_Speed', 'Wind_Direction']
        metadata_vars = spec_vars + novel_vars
        if metadata_key not in metadata_vars:
            print('Metadata variable ' + metadata_key + ' not part of the IQuOD spec. Valid options are:')
            print(metadata_vars)
            return None
        elif metadata_key not in list(self.r.variables()):
            print('Metadata variable ' + metadata_key + ' part of the spec but not part of your current ragged array')
            return None
        else:
            return self.r.variables()[metadata_key][self.i].item()

    ### profile metadata - backwards compatibility helpers

    def uid(self):
        return self.metadata('wod_unique_cast')

    def latitude(self):
        return self.metadata('lat')

    def latitude(self):
        return self.metadata('lon')

    def n_levels(self):
        return self.metadata('z_row_size')

    def _date(self):
        return self.metadata('date')

    def year(self):
        return int(str(self._date())[0:4])

    def month(self):
        return int(str(self._date())[4:6])

    def day(self):
        return int(str(self._date())[6:8])

    def time(self):
        return self.metadata('GMT_time')

    def datetime(self):
        """ Returns the date and time as a datetime object. """

        time  = self.time()
        if time is None or time < 0 or time >= 24:
            time = 0

        try:
            d = datetime(self.year(), self.month(), self.day()) + timedelta(hours=time)
            return d
        except:
            return

    def cruise(self):

        fullcruise = self.decode_bytearray(self.r.variables()['WOD_cruise_identifier'][self.i])
        return int(fullcruise[2:])

    def PIs(self):
        offset = self.determine_offset('Primary_Investigator_rowsize')
        nentries = self.metadata('Primary_Investigator_rowsize')
        pis = self.r.variables()['Primary_Investigator'][offset:offset + nentries]
        return [self.decode_bytearray(a) for a in pis]

    def PIs_var(self):
        offset = self.determine_offset('Primary_Investigator_rowsize')
        nentries = self.metadata('Primary_Investigator_rowsize')
        vars = self.r.variables()['Primary_Investigator_VAR'][offset:offset + nentries]
        return [self.decode_bytearray(a) for a in vars]

    def originator_cruise(self):
        return self.decode_bytearray(self.metadata('originators_cruise_identifier'))

    def originator_station(self):
        return self.metadata('Orig_Stat_Num')

    def originator_flag_type(self):
        return None

    def probe_type(self, raw=False):
        # probe type; by default converts back to index from https://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf,
        # for backwards compatibility. Set raw=True to get the string directly from the netCDF dataset variable.

        probe = self.decode_bytearray(self.r.variables()['dataset'][self.i])
        if raw:
            return probe
        else:
            probecodes = {
                "unknown": 0,
                "MBT": 1,
                "XBT": 2,
                "DBT": 3,
                "CTD": 4,
                "STD": 5,
                "XCTD": 6,
                "bottle/rossette/net": 7,
                "underway/intake": 8,
                "profling float": 9,
                "moored buoy": 10,
                "drifting buoy": 11,
                "towed CTD": 12,
                "animal mounted": 13,
                "bucket": 14,
                "glider": 15,
                "microBT": 16
            }
            if probe in probecodes:
                return probecodes[probe]
            else:
                return None

    ## per-level info

    def level_unpack(self, v, datatype):
        # unpack variable v's datatype
        # v can be ['Pressure', 'z', 'Temperature', 'Salinity', 'Oxygen'] depending on datatype
        # datatype can be ['data', 'sigfigs', 'uncertainty', 'IQUODflag']

        # again would like to autodetect rather than hard code what is appropriate to parse as a per-level data
        # but this switch for now to reflect the spec
        if datatype == 'data':
            level_vars = ['Pressure', 'z', 'Temperature', 'Salinity', 'Oxygen']
            suffix = ''
        elif datatype == 'sigfigs':
            level_vars = ['Pressure', 'z', 'Temperature', 'Salinity', 'Oxygen']
            suffix = '_sigfigs'
        elif datatype == 'uncertainty':
            level_vars = ['Pressure', 'z', 'Temperature', 'Salinity']
            suffix = '_uncertainty'
        elif datatype == 'IQUODflag':
            level_vars = ['z', 'Temperature', 'Salinity', 'Oxygen']
            suffix = '_IQUODflag'
        else:
            print(datatype + ' is not a valid datatype to unpack. Allowed values are: ["data", "sigfigs", "uncertainty", "IQUODflag"]' )
            return numpy.ma.array(numpy.zeros(self.n_levels()), mask=True)

        if v in level_vars:
            offset, nentries = self.locate_in_ragged(v)
            data = self.r.variables()[v+suffix][offset:offset + nentries]
            return data
        else:
            print('Level variable '+ v +' not supported for ' + datatype + '. Supported measurements are:')
            print(level_vars)
            return numpy.ma.array(numpy.zeros(self.n_levels()), mask=True)

    ### per-level data - backwards compatibility helpers

    def var_level_qc(self, v, flagtype='orig'):
        # per level QC decisions from flagtype QC provider for variable v
        # typical values of flagtype: orig | IQuOD | WOD
        flag = v+'_'+flagtype+'flag'
        data = numpy.ma.array(numpy.zeros(self.n_levels()), mask=True)
        if flag in self.r.variables():
            offset = self.determine_offset(v+'_row_size')
            nentries = self.metadata(v+'_row_size')
            data = self.r.variables()[flag][offset:offset + nentries]
        return data

    def var_profile_qc(self, v):
        if v+'_WODprofileflag' in self.r.variables():
            return self.metadata(v+'_WODprofileflag')
        else:
            return None

    def var_qc_mask(self, v, flagtype='orig'):
        """ Returns a boolean array showing which levels are rejected
            by the quality control (values are True). A true is only
            put in the array if there is a rejection (not if there is 
            a missing value)."""
        data = numpy.ma.array(numpy.zeros(self.n_levels()), mask=False, dtype=bool)
        prof = self.var_profile_qc(v)
        if prof is not None and prof > 0:
            data[:] = True
        else:
            zqc = self.z_level_qc(flagtype)
            data[(zqc.mask == False) & (zqc > 0)] = True
            lqc = self.var_level_qc(v, flagtype)
            data[(lqc.mask == False) & (lqc > 0)] = True
        return data

    def z(self):
        return self.level_unpack('z', 'data')

    def z_unc(self):
        return self.level_unpack('z', 'uncertainty')

    def z_level_qc(self, flagtype='orig'):
        return self.var_level_qc('z', flagtype)

    def t(self):
        return self.level_unpack('Temperature', 'data')

    def t_unc(self):
        return self.level_unpack('Temperature', 'uncertainty')

    def t_qc_mask(self, flagtype='orig'):
        return var_qc_mask('Temperature', flagtype)

    def t_level_qc(self, flagtype='orig'):
        return self.var_level_qc('Temperature', flagtype)

    def t_profile_qc(self):
        return self.var_profile_qc('Temperature')

    def s(self):
        return self.level_unpack('Salinity', 'data')

    def s_qc_mask(self, flagtype='orig'):
        return var_qc_mask('Salinity', flagtype)

    def s_level_qc(self, flagtype='orig'):
        return self.var_level_qc('Salinity', flagtype)

    def s_profile_qc(self):
        return self.var_profile_qc('Salinity')

    def oxygen(self):
        return self.level_unpack('Oxygen', 'data')

    def p(self):
        return self.level_unpack('Pressure', 'data')

