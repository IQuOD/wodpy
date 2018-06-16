from datetime import datetime
from wodpy import wod
import numpy, math, pandas

class TestClass():
    def setUp(self):

        # WOD13 format data
        classic = open("tests/testData/classic.dat")
        # example from pp 124 of http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
        self.classic1 = wod.WodProfile(classic)
        self.classic1_df = self.classic1.df()
        self.classic1_dict = self.classic1.npdict()
        self.classic1_head = self.classic1.header()
        # example with missing salinity information
        self.classic2 = wod.WodProfile(classic)

        # IQuOD 0.1 format data
        # short example (unpacked by hand to validate)
        iquod = open("tests/testData/iquod.dat")
        self.iquod1 = wod.WodProfile(iquod)
        self.iquod1_df = self.iquod1.df()
        self.iquod1_dict = self.iquod1.npdict()
        self.iquod1_head = self.iquod1.header()    
        # example with some metadata
        self.iquod2 = wod.WodProfile(iquod)
        self.iquod2_df = self.iquod2.df()
        self.iquod2_dict = self.iquod2.npdict()
    
        return

    def tearDown(self):
        return

    # ===================================================================
    # check the example from pp 124 of
    # http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
    # is extracted correctly by base functions.
    # data is in `data/classic.dat`
    
    def test_latitude(self):
        '''
        check latitude == 61.930
        '''

        latitude = self.classic1.latitude()
        df_latitude = self.classic1_df.meta['latitude']
        np_latitude = self.classic1_dict['latitude']
        header_latitude = self.classic1_head.latitude
        assert latitude == 61.930, 'latitude should have been 61.930, instead read %f' % latitude
        assert df_latitude == 61.930, 'dataframe latitude should have been 61.930, instead read %f' % df_latitude
        assert np_latitude == 61.930, 'np dict latitude should have been 61.930, instead read %f' % np_latitude
        assert header_latitude == 61.930, 'header latitude should have been 61.930, instead read %f' % header_latitude

    def test_latitude_error(self):
        '''
        check latitude error is None
        '''

        latitude_unc = self.classic1.latitude_unc()
        df_latitude_unc = self.classic1_df.meta['latitude_unc']
        np_latitude_unc = self.classic1_dict['latitude_unc']
        header_latitude_unc = self.classic1_head.latitude_unc
        assert latitude_unc is None, 'latitude error is undefined for this profile, instead read %f' % latitude_unc
        assert df_latitude_unc is None, 'dataframe latitude error is undefined for this profile, instead read %f' % df_latitude_unc
        assert np_latitude_unc is None, 'npdict latitude error is undefined for this profile, instead read %f' % np_latitude_unc
        assert math.isnan(header_latitude_unc) , 'header latitude error is undefined for this profile, instead read %f' % header_latitude_unc

    def test_longitude(self):
        '''
        check longitude == -172.270
        '''

        longitude = self.classic1.longitude()
        df_longitude = self.classic1_df.meta['longitude']
        np_longitude = self.classic1_dict['longitude']
        header_longitude = self.classic1_head.longitude
        assert longitude == -172.270, 'longitude should have been -172.270, instead read %f' % longitude
        assert df_longitude == -172.270, 'dataframe longitude should have been -172.270, instead read %f' % df_longitude
        assert np_longitude == -172.270, 'np dict longitude should have been -172.270, instead read %f' % np_longitude
        assert header_longitude == -172.270, 'header longitude should have been -172.270, instead read %f' % header_longitude

    def test_longitude_error(self):
        '''
        check longitude error is None
        '''

        longitude_unc = self.classic1.longitude_unc()
        df_longitude_unc = self.classic1_df.meta['longitude_unc']
        np_longitude_unc = self.classic1_dict['longitude_unc']
        header_longitude_unc = self.classic1_head.longitude_unc
        assert longitude_unc is None, 'longitude error is undefined for this profile, instead read %f' % longitude_unc
        assert df_longitude_unc is None, 'dataframe longitude error is undefined for this profile, instead read %f' % df_longitude_unc
        assert np_longitude_unc is None, 'np dict longitude error is undefined for this profile, instead read %f' % np_longitude_unc
        assert math.isnan(header_longitude_unc), 'header longitude error is undefined for this profile, instead read %f' % header_longitude_unc

    def test_uid(self):
        '''
        check cruise ID == 67064
        '''

        uid = self.classic1.uid()
        df_uid = self.classic1_df.meta['uid']
        np_uid = self.classic1_dict['uid']
        header_uid = self.classic1_head.uid
        assert uid == 67064, 'uid should have been 67064, instead read %f' % uid
        assert df_uid == 67064, 'dataframe uid should have been 67064, instead read %f' % df_uid
        assert np_uid == 67064, 'np dict uid should have been 67064, instead read %f' % np_uid
        assert header_uid == 67064, 'header uid should have been 67064, instead read %f' % header_uid

    def test_n_levels(self):
        '''
        check the number of levels == 4
        '''

        levels = self.classic1.n_levels()
        df_levels = self.classic1_df.meta['n_levels']
        np_levels = self.classic1_dict['n_levels']
        header_n_levels = self.classic1_head.n_levels
        assert levels == 4, 'levels should have been 4, instead read %f' % levels
        assert df_levels == 4, 'dataframe levels should have been 4, instead read %f' % df_levels
        assert np_levels == 4, 'np dict levels should have been 4, instead read %f' % np_levels
        assert header_n_levels == 4, 'header levels should have been 4, instead read %f' % header_levels

    def test_year(self):
        '''
        check year == 1934
        '''

        year = self.classic1.year()
        df_year = self.classic1_df.meta['year']
        np_year = self.classic1_dict['year']
        header_year = self.classic1_head.year
        assert year == 1934, 'year should have been 1934, instead read %f' % year
        assert df_year == 1934, 'dataframe year should have been 1934, instead read %f' % df_year
        assert np_year == 1934, 'np dict year should have been 1934, instead read %f' % np_year
        assert header_year == 1934, 'header year should have been 1934, instead read %f' % header_year

    def test_month(self):
        '''
        check month == 8
        '''

        month = self.classic1.month() 
        df_month = self.classic1_df.meta['month']
        np_month = self.classic1_dict['month']
        header_month = self.classic1_head.month
        assert month == 8, 'month should have been 8, instead read %f' % month
        assert df_month == 8, 'dataframe month should have been 8, instead read %f' % df_month
        assert np_month == 8, 'np dict month should have been 8, instead read %f' % np_month
        assert header_month == 8, 'header month should have been 8, instead read %f' % header_month


    def test_day(self):
        '''
        check day == 7
        '''

        day = self.classic1.day()
        df_day = self.classic1_df.meta['day']
        np_day = self.classic1_dict['day']
        header_day = self.classic1_head.day
        assert day == 7, 'day should have been 7, instead read %f' % day
        assert df_day == 7, 'dataframe day should have been 7, instead read %f' % df_day
        assert np_day == 7, 'np dict day should have been 7, instead read %f' % np_day
        assert header_day == 7, 'header day should have been 7, instead read %f' % header_day

    def test_time(self):
        ''' 
        check time == 10.37
        '''

        time = self.classic1.time()
        df_time = self.classic1_df.meta['time']
        np_time = self.classic1_dict['time']
        header_time = self.classic1_head.time
        assert time == 10.37, 'time should have been 10.37, instead read %f' % time
        assert df_time == 10.37, 'dataframe time should have been 10.37, instead read %f' % df_time
        assert np_time == 10.37, 'np dict time should have been 10.37, instead read %f' % np_time
        assert header_time == 10.37, 'header time should have been 10.37, instead read %f' % header_time


    def test_datetime(self):
        '''
        check datetime 1934-8-7 10:22:12
        '''

        d = self.classic1.datetime()
        assert d == datetime(1934, 8, 7, 10, 22, 12), \
                'time should have been 1934-08-07 10:22:12, instead read %s' \
                % d


    def test_probe_type(self):
        '''
        check probe type == 7
        '''

        probe = self.classic1.probe_type() 
        df_probe = self.classic1_df.meta['probe_type']
        np_probe = self.classic1_dict['probe_type']
        header_probe = self.classic1_head.probe_type
        assert probe == 7, 'probe should have been 7, instead read %f' % probe
        assert df_probe == 7, 'dataframe probe should have been 7, instead read %f' % df_probe
        assert np_probe == 7, 'np dict probe should have been 7, instead read %f' % np_probe
        assert header_probe == 7, 'header probe should have been 7, instead read %f' % header_probe


    def test_depth(self):
        '''
        check depths == [0.0, 10.0, 25.0, 50.0]
        '''

        truth = [0.0, 10.0, 25.0, 50.0]
        z = self.classic1.z()
        df_z = self.classic1_df['z']
        np_z = self.classic1_dict['z']
        assert numpy.array_equal(z, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % z.__str__()
        assert numpy.array_equal(df_z, truth), 'dataframe depths should have been [0, 10, 25, 50], instead read %s' % df_z.tolist().__str__()
        assert numpy.array_equal(np_z, truth), 'numpy dict depths should have been [0, 10, 25, 50], instead read %s' % np_z.__str__()

    def test_depth_error(self):
        '''
        check depth errors == [--,--,--,--] (all masked)
        '''

        truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
        dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
        z_unc = self.classic1.z_unc()
        df_z_unc = self.classic1_df['z_unc']
        np_z_unc = self.classic1_dict['z_unc']
        assert numpy.array_equal(z_unc, truth), 'depth errors should have been all masked, instead read %s' % z_unc.__str__()
        assert df_z_unc.equals(dftruth), 'dataframe depth errors should have been all masked, instead read %s' % df_z_unc.__str__()
        assert numpy.array_equal(np_z_unc, truth), 'numpy dict depth errors should have been all masked, instead read %s' % np_z_unc.__str__()

    def test_temperature(self):
        '''
        check temperatures == [8.960, 8.950, 0.900, -1.230]
        '''

        truth = [8.960, 8.950, 0.900, -1.230]
        t = self.classic1.t()
        df_t = self.classic1_df['t']
        np_t = self.classic1_dict['t']
        assert numpy.array_equal(t, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % t.__str__()
        assert numpy.array_equal(df_t, truth), 'dataframe temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read \n%s' % df_t.__str__()
        assert numpy.array_equal(np_t, truth), 'numpy dict temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % np_t.__str__()

    def test_temperature_error(self):
        '''
        check temperature errors == [--,--,--,--] (all masked)
        '''

        truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
        dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
        t_unc = self.classic1.t_unc()
        df_t_unc = self.classic1_df['t_unc']
        np_t_unc = self.classic1_dict['t_unc']
   
        assert numpy.array_equal(t_unc, truth), 'temperature errors should have been all masked, instead read %s' % t_unc.__str__()
        assert df_t_unc.equals(dftruth), 'dataframe temperature errors should have been all masked, instead read %s' % df_t_unc.__str__()
        assert numpy.array_equal(np_t_unc, truth), 'numpy dict temperature errors should have been all masked, instead read %s' % np_t_unc.__str__()


    def test_salinity(self):
        '''
        check salinities == [30.900, 30.900, 31.910, 32.410]
        '''
        
        truth = [30.900, 30.900, 31.910, 32.410]
        s = self.classic1.s()
        df_s = self.classic1_df['s']
        np_s = self.classic1_dict['s']
        assert numpy.array_equal(s, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % s.__str__()
        assert numpy.array_equal(df_s, truth), 'dataframe salinities should have been [30.9, 30.9, 31.91, 32.41], instead read \n%s' % df_s.__str__()
        assert numpy.array_equal(np_s, truth), 'numpy dict salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % np_s.__str__()

    def test_salinity_error(self):
        '''
        check salinity errors == [--,--,--,--] (all masked)
        '''

        truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
        dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
        s_unc = self.classic1.s_unc()
        df_s_unc = self.classic1_df['s_unc']
        np_s_unc = self.classic1_dict['s_unc']
   
        assert numpy.array_equal(s_unc, truth), 'salinity errors should have been all masked, instead read %s' % s_unc.__str__()
        assert df_s_unc.equals(dftruth), 'dataframe salinity errors should have been all masked, instead read %s' % df_s_unc.__str__()
        assert numpy.array_equal(np_s_unc, truth), 'numpy dict salinity errors should have been all masked, instead read %s' % np_s_unc.__str__()

    def test_oxygen(self):
        '''
        check oxygen levels = [6.750, 6.700, 8.620, 7.280]
        '''

        truth = [6.750, 6.700, 8.620, 7.280]
        o2 = self.classic1.oxygen()
        df_o2 = self.classic1_df['oxygen']
        np_o2 = self.classic1_dict['oxygen']

        assert numpy.array_equal(o2, truth), 'oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % o2.__str__()
        assert numpy.array_equal(df_o2, truth), 'dataframe oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read \n%s' % df_o2.__str__()
        assert numpy.array_equal(np_o2, truth), 'numpy dict oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % np_o2.__str__()

    def test_phosphate(self):
        '''
        check phosphate levels = [0.650, 0.710, 0.900, 1.170]
        '''

        truth = [0.650, 0.710, 0.900, 1.170]
        phos = self.classic1.phosphate()
        df_phos = self.classic1_df['phosphate']
        np_phos = self.classic1_dict['phosphate']

        assert numpy.array_equal(phos, truth), 'phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % phos.__str__()
        assert numpy.array_equal(df_phos, truth), 'dataframe phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read \n%s' % df_phos.__str__()
        assert numpy.array_equal(np_phos, truth), 'numpy dict phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % np_phos.__str__()

    def test_silicate(self):
        '''
        check silicate levels = [20.500, 12.300, 15.400, 25.600]
        '''

        truth = [20.500, 12.300, 15.400, 25.600]
        sili = self.classic1.silicate()
        df_sili = self.classic1_df['silicate']
        np_sili = self.classic1_dict['silicate']

        assert numpy.array_equal(sili, truth), 'silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % sili.__str__()
        assert numpy.array_equal(df_sili, truth), 'dataframe silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read \n%s' % df_sili.__str__()
        assert numpy.array_equal(np_sili, truth), 'numpy dict silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % np_sili.__str__()

    def test_pH(self):
        '''
        check pH levels = [8.100, 8.100, 8.100, 8.050]
        '''

        truth = [8.100, 8.100, 8.100, 8.050]
        pH = self.classic1.pH()
        df_pH = self.classic1_df['pH']
        np_pH = self.classic1_dict['pH']

        assert numpy.array_equal(pH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % pH.__str__()
        assert numpy.array_equal(df_pH, truth), 'dataframe pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read \n%s' % df_pH.__str__()
        assert numpy.array_equal(np_pH, truth), 'numpy dict pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % np_pH.__str__()

    def test_PI(self):
        '''
        check for PI code
        '''

        truth = [{'Variable code': 0, 'P.I. code': 215}, {'Variable code': 0, 'P.I. code': 216}, {'Variable code': -5006, 'P.I. code': 217}, {'Variable code': -5002, 'P.I. code': 218}]
        PIs = self.classic1.PIs()
        df_PIs = self.classic1_df.meta['PIs']
        np_PIs = self.classic1_dict['PIs']
        assert numpy.array_equal(PIs, truth), 'PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read %s' % PIs.__str__()
        assert numpy.array_equal(df_PIs, truth), 'dataframe PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read \n%s' % PIs.__str__()
        assert numpy.array_equal(np_PIs, truth), 'numpy dict PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read %s' % PIs.__str__()

    def test_originator_cruise(self):

        truth = 'STOCS85A'
        originator_cruise = self.classic1.originator_cruise()
        df_originator_cruise = self.classic1_df.meta['originator_cruise']
        np_originator_cruise = self.classic1_dict['originator_cruise']
        assert originator_cruise == truth, 'Originator cruise should have been STOCS85A, instead read %s' % originator_cruise
        assert df_originator_cruise == truth, 'dataframe riginator cruise should have been STOCS85A, instead read %s' % df_originator_cruise
        assert np_originator_cruise == truth, 'numpy dict originator cruise should have been STOCS85A, instead read %s' % np_originator_cruise

    def test_originator_station(self):

        truth = None
        originator_station = self.classic1.originator_station()
        df_originator_station = self.classic1_df.meta['originator_station']
        np_originator_station = self.classic1_dict['originator_station']
        assert originator_station == truth
        assert df_originator_station == truth
        assert np_originator_station == truth

    # ===================================================================
    # spot check another pre-iquod profile with many missing values
    # data: data/classic.dat

    def test_missing_vars(self):
        '''
        check that error value extraction does not fail when measured value is missing
        note if a variable value is missing, wodpy assumes the error on the value will also be missing
        '''

        truth = numpy.ma.MaskedArray([0]*24, [True]*24)
        s_unc = self.classic2.s_unc()
        assert numpy.array_equal(s_unc, truth), 'expected salinity errors to all be missing, but got %s instead' % s_unc.__str__()

    # ===================================================================
    # check that an IQuOD v 0.1 profile is unpacked correctly
    # data is in `data/iquod.dat`

    def test_iquod_latitude(self):
        '''
        check latitude == 34.5883
        '''

        latitude = self.iquod1.latitude()
        df_latitude = self.iquod1_df.meta['latitude']
        np_latitude = self.iquod1_dict['latitude']
        header_latitude = self.iquod1_head.latitude
        assert latitude == 34.5883, 'latitude should have been 34.5883, instead read %f' % latitude
        assert df_latitude == 34.5883, 'dataframe latitude should have been 34.5883, instead read %f' % df_latitude
        assert np_latitude == 34.5883, 'np dict latitude should have been 34.5883, instead read %f' % np_latitude
        assert header_latitude == 34.5883, 'header latitude should have been 34.5883, instead read %f' % header_latitude  

    def test_iquod_latitude_error(self):
        '''
        check latitude error is None
        '''

        latitude_unc = self.iquod1.latitude_unc()
        df_latitude_unc = self.iquod1_df.meta['latitude_unc']
        np_latitude_unc = self.iquod1_dict['latitude_unc']
        header_latitude_unc = self.iquod1_head.latitude_unc
        assert latitude_unc is None, 'latitude error is undefined for this profile, instead read %f' % latitude_unc
        assert df_latitude_unc is None, 'dataframe latitude error is undefined for this profile, instead read %f' % df_latitude_unc
        assert np_latitude_unc is None, 'npdict latitude error is undefined for this profile, instead read %f' % np_latitude_unc
        assert math.isnan(header_latitude_unc) , 'header latitude error is undefined for this profile, instead read %f' % header_latitude_unc

    def test_iquod_longitude(self):
        '''
        check longitude == 134.2433
        '''

        longitude = self.iquod1.longitude()
        df_longitude = self.iquod1_df.meta['longitude']
        np_longitude = self.iquod1_dict['longitude']
        header_longitude = self.iquod1_head.longitude
        assert longitude == 134.2433, 'longitude should have been 134.2433, instead read %f' % longitude
        assert df_longitude == 134.2433, 'dataframe longitude should have been 134.2433, instead read %f' % df_longitude
        assert np_longitude == 134.2433, 'np dict longitude should have been 134.2433, instead read %f' % np_longitude
        assert header_longitude == 134.2433, 'header longitude should have been 134.2433, instead read %f' % header_longitude

    def test_iquod_longitude_error(self):
        '''
        check longitude error is None
        '''

        longitude_unc = self.iquod1.longitude_unc()
        df_longitude_unc = self.iquod1_df.meta['longitude_unc']
        np_longitude_unc = self.iquod1_dict['longitude_unc']
        header_longitude_unc = self.iquod1_head.longitude_unc
        assert longitude_unc is None, 'longitude error is undefined for this profile, instead read %f' % longitude_unc
        assert df_longitude_unc is None, 'dataframe longitude error is undefined for this profile, instead read %f' % df_longitude_unc
        assert np_longitude_unc is None, 'npdict longitude error is undefined for this profile, instead read %f' % np_longitude_unc
        assert math.isnan(header_longitude_unc) , 'header longitude error is undefined for this profile, instead read %f' % header_longitude_unc


    def test_iquod_uid(self):
        '''
        check cruise ID == 13393621
        '''

        uid = self.iquod1.uid()
        df_uid = self.iquod1_df.meta['uid']
        np_uid = self.iquod1_dict['uid']
        header_uid = self.iquod1_head.uid
        assert uid == 13393621, 'uid should have been 13393621, instead read %f' % uid
        assert df_uid == 13393621, 'dataframe uid should have been 13393621, instead read %f' % df_uid
        assert np_uid == 13393621, 'np dict uid should have been 13393621, instead read %f' % np_uid
        assert header_uid == 13393621, 'header uid should have been 13393621, instead read %f' % header_uid

    def test_iquod_n_levels(self):
        '''
        check the number of levels == 5
        '''

        levels = self.iquod1.n_levels()
        df_levels = self.iquod1_df.meta['n_levels']
        np_levels = self.iquod1_dict['n_levels']
        header_n_levels = self.iquod1_head.n_levels
        assert levels == 5, 'levels should have been 5, instead read %f' % levels
        assert df_levels == 5, 'dataframe levels should have been 5, instead read %f' % df_levels
        assert np_levels == 5, 'np dict levels should have been 5, instead read %f' % np_levels
        assert header_n_levels == 5, 'header levels should have been 5, instead read %f' % header_levels

    def test_iquod_year(self):
        '''
        check year == 2000
        '''

        year = self.iquod1.year()
        df_year = self.iquod1_df.meta['year']
        np_year = self.iquod1_dict['year']
        header_year = self.iquod1_head.year
        assert year == 2000, 'year should have been 2000, instead read %f' % year
        assert df_year == 2000, 'dataframe year should have been 2000, instead read %f' % df_year
        assert np_year == 2000, 'np dict year should have been 2000, instead read %f' % np_year
        assert header_year == 2000, 'header year should have been 2000, instead read %f' % header_year

    def test_iquod_month(self):
        '''
        check month == 1
        '''

        month = self.iquod1.month() 
        df_month = self.iquod1_df.meta['month']
        np_month = self.iquod1_dict['month']
        header_month = self.iquod1_head.month
        assert month == 1, 'month should have been 1, instead read %f' % month
        assert df_month == 1, 'dataframe month should have been 1, instead read %f' % df_month
        assert np_month == 1, 'np dict month should have been 1, instead read %f' % np_month
        assert header_month == 1, 'header month should have been 1, instead read %f' % header_month

    def test_iquod_day(self):
        '''
        check day == 4
        '''

        day = self.iquod1.day()
        df_day = self.iquod1_df.meta['day']
        np_day = self.iquod1_dict['day']
        header_day = self.iquod1_head.day
        assert day == 4, 'day should have been 4, instead read %f' % day
        assert df_day == 4, 'dataframe day should have been 4, instead read %f' % df_day
        assert np_day == 4, 'np dict day should have been 4, instead read %f' % np_day
        assert header_day == 4, 'header day should have been 4, instead read %f' % header_day

    def test_iquod_time(self):
        ''' 
        check time == 3.7
        '''

        time = self.iquod1.time()
        df_time = self.iquod1_df.meta['time']
        np_time = self.iquod1_dict['time']
        header_time = self.iquod1_head.time
        assert time == 3.7, 'time should have been 3.7, instead read %f' % time
        assert df_time == 3.7, 'dataframe time should have been 3.7, instead read %f' % df_time
        assert np_time == 3.7, 'np dict time should have been 3.7, instead read %f' % np_time
        assert header_time == 3.7, 'header time should have been 3.7, instead read %f' % header_time


    def test_iquod_datetime(self):
        '''
        check datetime 2000-1-4 3:42:00
        '''

        d = self.iquod1.datetime()
        assert d == datetime(2000, 1, 4, 3, 42, 00), \
                'time should have been 2000-01-04 3:42:00, instead read %s' \
                % d


    def test_iquod_probe_type(self):
        '''
        check probe type == 4
        '''

        probe = self.iquod1.probe_type() 
        df_probe = self.iquod1_df.meta['probe_type']
        np_probe = self.iquod1_dict['probe_type']
        header_probe = self.iquod1_head.probe_type
        assert probe == 4, 'probe should have been 4, instead read %f' % probe
        assert df_probe == 4, 'dataframe probe should have been 4, instead read %f' % df_probe
        assert np_probe == 4, 'np dict probe should have been 4, instead read %f' % np_probe
        assert header_probe == 4, 'header probe should have been 4, instead read %f' % header_probe

    def test_iquod_depth(self):
        '''
        check depths == [0,2,5,10,20]
        '''

        truth = [0,2,5,10,20]
        z = self.iquod1.z()
        df_z = self.iquod1_df['z']
        np_z = self.iquod1_dict['z']
        assert numpy.array_equal(z, truth), 'depths should have been [0,2,5,10,20], instead read %s' % z.__str__()
        assert numpy.array_equal(df_z, truth), 'dataframe depths should have been [0,2,5,10,20], instead read %s' % df_z.tolist().__str__()
        assert numpy.array_equal(np_z, truth), 'numpy dict depths should have been [0,2,5,10,20], instead read %s' % np_z.__str__()

    def test_iquod_depth_error(self):
        '''
        check depth errors == [0,.0016,.004,.008,.016]
        '''

        truth = [0,.0016,.004,.008,.016]
        z_unc = self.iquod1.z_unc()
        df_z_unc = self.iquod1_df['z_unc']
        np_z_unc = self.iquod1_dict['z_unc']
        assert numpy.array_equal(z_unc, truth), 'depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % z_unc.__str__()
        assert numpy.array_equal(df_z_unc, truth), 'dataframe depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % df_z_unc.__str__()
        assert numpy.array_equal(np_z_unc, truth), 'numpy dict depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % np_z_unc.__str__()

    def test_iquod_temperature(self):
        '''
        check temperatures == [11.1,11.2,11.0,11.0,11.0]
        '''

        truth = [11.1,11.2,11.0,11.0,11.0]
        t = self.iquod1.t()
        df_t = self.iquod1_df['t']
        np_t = self.iquod1_dict['t']
        assert numpy.array_equal(t, truth), 'temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read %s' % t.__str__()
        assert numpy.array_equal(df_t, truth), 'dataframe temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read \n%s' % df_t.__str__()
        assert numpy.array_equal(np_t, truth), 'numpy dict temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read %s' % np_t.__str__()

    def test_iquod_temperature_error(self):
        '''
        check temperature errors == [.01,.01,.01,.01,.01]
        '''

        truth = [.01,.01,.01,.01,.01]
        t_unc = self.iquod1.t_unc()
        df_t_unc = self.iquod1_df['t_unc']
        np_t_unc = self.iquod1_dict['t_unc']
        assert numpy.array_equal(t_unc, truth), 'temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % t_unc.__str__()
        assert numpy.array_equal(df_t_unc, truth), 'dataframe temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % df_t_unc.__str__()
        assert numpy.array_equal(np_t_unc, truth), 'numpy dict temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % np_t_unc.__str__()

    def test_iquod_salinity(self):
        '''
        check salinities == [31.53,31.47,31.49,31.49,31.50]
        '''
        
        truth = [31.53,31.47,31.49,31.49,31.50]
        s = self.iquod1.s()
        df_s = self.iquod1_df['s']
        np_s = self.iquod1_dict['s']
        assert numpy.array_equal(s, truth), 'salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read %s' % s.__str__()
        assert numpy.array_equal(df_s, truth), 'dataframe salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read \n%s' % df_s.__str__()
        assert numpy.array_equal(np_s, truth), 'numpy dict salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read %s' % np_s.__str__()

    def test_iquod_salinity_error(self):
        '''
        check temperature errors == [.02,.02,.02,.02,.02]
        '''

        truth = [.02,.02,.02,.02,.02]
        s_unc = self.iquod1.s_unc()
        df_s_unc = self.iquod1_df['s_unc']
        np_s_unc = self.iquod1_dict['s_unc']
        assert numpy.array_equal(s_unc, truth), 'salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % s_unc.__str__()
        assert numpy.array_equal(df_s_unc, truth), 'dataframe salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % df_s_unc.__str__()
        assert numpy.array_equal(np_s_unc, truth), 'numpy dict salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % np_s_unc.__str__()

    # metadata tests

    def test_metadata(self):
        '''
        check correct unpacking of temperature and salinity metadata from iquod profile
        '''

        truth_t = [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}]
        truth_s = [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}]
        t_meta = self.iquod2.t_metadata()
        s_meta = self.iquod2.s_metadata()
        df_t_meta = self.iquod2_df.meta['t_metadata']
        df_s_meta = self.iquod2_df.meta['s_metadata']
        np_t_meta = self.iquod2_dict['t_metadata']
        np_s_meta = self.iquod2_dict['s_metadata']

        assert numpy.array_equal(truth_t, t_meta), "temperature metadata should have been [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % t_meta.__str__()
        assert numpy.array_equal(truth_s, s_meta), "salinity metadata should have been [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % s_meta.__str__()
        assert numpy.array_equal(truth_t, df_t_meta), "dataframe temperature metadata should have been [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % df_t_meta.__str__()
        assert numpy.array_equal(truth_s, df_s_meta), "dataframe salinity metadata should have been [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % df_s_meta.__str__()
        assert numpy.array_equal(truth_t, np_t_meta), "dict temperature metadata should have been [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % np_t_meta.__str__()
        assert numpy.array_equal(truth_s, np_s_meta), "dict salinity metadata should have been [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % np_s_meta.__str__()

    def test_missing_metadata(self):
        '''
        make sure absent metadata doesn't cause problems
        '''

        # pre-iquod format
        t_meta = self.classic1.t_metadata()
        s_meta = self.classic1.s_metadata()
        assert numpy.array_equal([], t_meta), 'temperature metadata should have been [], instead read %s' % t_meta.__str__()
        assert numpy.array_equal([], s_meta), 'salinity metadata should have been [], instead read %s' % s_meta.__str__()

        # iquod format
        t_meta = self.iquod1.t_metadata()
        s_meta = self.iquod1.s_metadata()
        assert numpy.array_equal([], t_meta), 'iquod temperature metadata should have been [], instead read %s' % t_meta.__str__()
        assert numpy.array_equal([], s_meta), 'iquod salinity metadata should have been [], instead read %s' % s_meta.__str__()

        # pre-iquod format, with metadata (but no intelligent metadata flag)
        truth_t = [{'code': 5, 'value': 4.0, 'iMeta': 0}]
        t_meta = self.classic2.t_metadata()
        assert numpy.array_equal(truth_t, t_meta), "temperature metadata should have been [{'code': 5, 'value': 4.0, 'iMeta': 0}], instead read %s" % t_meta.__str__()


