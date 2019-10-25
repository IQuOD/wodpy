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

    ## metadata

    def latitude(self):
        return self.r.variables()['lat'][self.i].item()

    def latitude_unc(self):
        return None

    def longitude(self):
        return self.r.variables()['lon'][self.i].item()

    def longitude_unc(self):
        return None

    def uid(self):
        return self.r.variables()['wod_unique_cast'][self.i].item()

    def n_levels(self):
        return self.r.variables()['z_row_size'][self.i].item()

    def _date(self):
        return self.r.variables()['date'][self.i].item()

    def year(self):
        return int(str(self._date())[0:4])

    def month(self):
        return int(str(self._date())[4:6])

    def day(self):
        return int(str(self._date())[6:8])

    def time(self):
        return self.r.variables()['GMT_time'][self.i].item()

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
        ntemps = self.r.variables()['Primary_Investigator_rowsize'][self.i].item()
        pis = self.r.variables()['Primary_Investigator'][offset:offset + ntemps]
        return [self.decode_bytearray(a) for a in pis]

    def PIs_var(self):
        offset = self.determine_offset('Primary_Investigator_rowsize')
        ntemps = self.r.variables()['Primary_Investigator_rowsize'][self.i].item()
        vars = self.r.variables()['Primary_Investigator_VAR'][offset:offset + ntemps]
        return [self.decode_bytearray(a) for a in vars]

    def originator_cruise(self):
        return self.decode_bytearray(self.r.variables()['originators_cruise_identifier'][self.i])

    def originator_station(self):
        return self.r.variables()['Orig_Stat_Num'][self.i].item()

    def extract_secondary_header(self, index):
        return None

    def originator_flag_type(self):
        return None

    def probe_type(self):
        return None

    def var_index(self, code=1, s=False):
        return None

    def var_data(self, v):
        '''
        generic variable extractor. examples of v:
        'Temperature', 'Salinity', 'Oxygen', 'Phosphate', 'Silicate', 'pH', ...
        '''

        offset = self.determine_offset(v+'_row_size')
        ntemps = self.r.variables()[v+'_row_size'][self.i].item()
        return self.r.variables()[v][offset:offset + ntemps]

    def var_data_unc(self, v):
        offset = self.determine_offset(v+'_row_size')
        ntemps = self.r.variables()[v+'_row_size'][self.i].item()
        return self.r.variables()[v+'_uncertainty'][offset:offset + ntemps]

    def var_metadata(self, index):
        return None

    def var_level_qc(self, v, flagtype='IQuOD'):
        if flagtype == 'IQuOD':
            flag = 'Temperature_IQUODflag'
        elif flagtype == 'WOD':
            flag = 'Temperature_WODflag'

        offset = self.determine_offset(v+'_row_size')
        ntemps = self.r.variables()[v+'_row_size'][self.i].item()
        return self.r.variables()[flag][offset:offset + ntemps]

    def var_profile_qc(self, v):
        return self.r.variables()[v+'_WODprofileflag'][self.i].item()

    def var_qc_mask(self, index):
        return None

    ## level info

    def z(self):
        offset = self.determine_offset('z_row_size')
        return self.r.variables()['z'][offset:offset + self.n_levels()]

    def z_unc(self):
        offset = self.determine_offset('z_row_size')
        return self.r.variables()['z_uncertainty'][offset:offset + self.n_levels()]

    def z_level_qc(self, flagtype='IQuOD'):
        if flagtype == 'IQuOD':
            flag = 'z_IQUODflag'
        elif flagtype == 'WOD':
            flag = 'z_WODflag'

        offset = self.determine_offset('z_row_size')
        return self.r.variables()[flag][offset:offset + self.n_levels()]

    def t(self):
        return self.var_data('Temperature')

    def t_unc(self):
        return self.var_data_unc('Temperature')

    def t_qc_mask(self):
        return None

    def t_level_qc(self, flagtype='IQuOD'):
        return self.var_level_qc('Temperature', flagtype)

    def t_profile_qc(self):
        return self.var_profile_qc('Temperature')

    def t_metadata(self):
        return None

    def s(self):
        return self.var_data('Salinity')

    def s_qc_mask(self):
        return None

    def s_level_qc(self, flagtype='IQuOD'):
        return self.var_level_qc('Salinity', flagtype)

    def s_profile_qc(self):
        return self.var_profile_qc('Salinity')

    def s_metadata(self):
        return None

    def oxygen(self):
        return self.var_data('Oxygen')

    def phosphate(self):
        return self.var_data('Phosphate')

    def silicate(self):
        return self.var_data('Silicate')

    def pH(self):
        return self.var_data('pH')

    def p(self):
        return None

