################### DRAFT #####################

# netCDF quickstart

## load data into a profile object:

# from wodpy import wodnc
# r = wodnc.Ragged("/wodpy/ocldb1617988395.19301_XBT.nc")
# p = wodnc.Profile(r, 0)  # get the first profile in the file

## find out what data is available:

# print(p.show_profile_metadata())
# print(p.show_level_data())

## extract a metadata using the keys you found above:

# print(p.metadata('country'))

## extract some per-level data using the keys you found above:

# print(p.level_unpack('Temperature'))

################### DRAFT #####################

from netCDF4 import Dataset
import numpy, logging
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

    def dimensions(self):
        return self.rootgrp.dimensions

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

class ncProfile():
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
        # trim variable v to ust include the variable name left of any underscore:
        v = v.split('_')[0]
        offset = int(self.determine_offset(v+'_row_size'))
        nentries = int(self.metadata(v+'_row_size'))
        return offset, nentries

    def is_metadata(self, metadata_key):
        '''
        returns true if metadata_key looks like metadata, 
        ie something that has one value per profile

        current approximation: metadata come in lists the length of the number of profiles
        '''

        if metadata_key in self.r.variables():
            try:
                if len(self.r.variables()[metadata_key]) == self.r.ncasts():
                    return True
                else:
                    return False
            except:
                logging.warning(metadata_key + ' neither profile metadata nor level data.')
                return False
        else:
            logging.warning(metadata_key + ' not found in this dataset.')
            return False

    def is_level_data(self, data_key):
        '''
        returns true if data_key looks like per level data
        '''

        if data_key not in self.r.rootgrp.variables.keys():
            return False
        if len(self.r.rootgrp.variables[data_key].dimensions) == 0:
            # logging.warning(data_key + ' is not level data and of zero size.')
            return False
        if '_obs' in self.r.rootgrp.variables[data_key].dimensions[0]:
            # per level data should have a *_obs dimension 
            return True
        else:
            # logging.warning(data_key + ' is not level data.')
            return False                    

    def show_profile_metadata(self):
        '''
        returns the list of all valid variable names that correspond to profile metadata
        '''

        return [x for x in self.r.variables().keys() if self.is_metadata(x)]

    def show_level_data(self):
        '''
        returns the list of all valid level data names
        '''

        return [x for x in self.r.variables().keys() if self.is_level_data(x)]

    ## core data extraction

    def metadata(self, metadata_key):
        # hardcoded list for now since per-profile and per-level variables are all in the same
        # netCDF variables list, but this function is only appropriate for per-profile info.
        # would like to see this autodetected in future.
       
        if self.is_metadata(metadata_key):
            try:
                return self.r.variables()[metadata_key][self.i].item()
            except:
                return self.decode_bytearray(self.r.variables()[metadata_key][self.i])
        else:
            logging.warning(metadata_key + ' not a valid metadata name. See Profile.r.variables().keys() for all variables, and Profile.is_metadata() to check if a key is per-profile metadata.')

    def level_unpack(self, level_key):
        # unpack per-level variable level_key

        data = numpy.ma.array(numpy.zeros(self.n_levels()), mask=True)

        if self.is_level_data(level_key):
            offset, nentries = self.locate_in_ragged(level_key)
            data = self.r.variables()[level_key][offset:offset + nentries]
        else:
            logging.warning('Level variable ' + level_key + ' not found.')
        
        return data

    
    ## helpers to match behavior of ASCII parser #############################################

    def latitude(self):
        return self.metadata('lat')

    def latitude_unc(self):
        raise NotImplementedError('tbd')

    def longitude(self):
        return self.metadata('lon')

    def longitude_unc(self):
        raise NotImplementedError('tbd')

    def uid(self):
        return self.metadata('wod_unique_cast')

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
        raise NotImplementedError('tbd')

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

    def var_level_qc(self, v, flagtype='orig'):
        # per level QC decisions from flagtype QC provider for variable v
        # typical values of flagtype: orig | WOD
        # redundant with level_unpack, here for symmetry with ascii implementation

        return self.level_unpack(v+'_'+flagtype+'flag')

    def var_profile_qc(self, v):
        # also here for consistency with ascii parser

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
        return self.level_unpack('z')

    def z_unc(self):
        raise NotImplementedError('tbd')

    def z_level_qc(self, flagtype='orig'):
        return self.var_level_qc('z', flagtype)

    def var_data_unc(self):
        raise NotImplementedError('tbd')

    def var_metadata(self):
        raise NotImplementedError('tbd')

    def t(self):
        return self.level_unpack('Temperature')

    def t_unc(self):
        raise NotImplementedError('tbd')

    def t_qc_mask(self, flagtype='orig'):
        return self.var_qc_mask('Temperature', flagtype)

    def t_level_qc(self, flagtype='orig'):
        return self.var_level_qc('Temperature', flagtype)

    def t_profile_qc(self):
        return self.var_profile_qc('Temperature')

    def t_metadata(self):
        raise NotImplementedError('tbd')

    def s(self):
        return self.level_unpack('Salinity')

    def s_unc(self):
        raise NotImplementedError('tbd')

    def s_qc_mask(self, flagtype='orig'):
        return self.var_qc_mask('Salinity', flagtype)

    def s_level_qc(self, flagtype='orig'):
        return self.var_level_qc('Salinity', flagtype)

    def s_profile_qc(self):
        return self.var_profile_qc('Salinity')

    def s_metadata(self):
        raise NotImplementedError('tbd')

    def oxygen(self):
        return self.level_unpack('Oxygen')  

    def phosphate(self):
        return self.level_unpack('Phosphate')  

    def silicate(self):
        return self.level_unpack('Silicate')  

    def pH(self):
        return self.level_unpack('pH') 

    def p(self):
        raise NotImplementedError('tbd')  

    def df(self):
        raise NotImplementedError('tbd')

    def npdict(self):
        raise NotImplementedError('tbd')

    def header(self):
        raise NotImplementedError('tbd')
