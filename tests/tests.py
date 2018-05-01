from datetime import datetime
from wodpy import wod
import numpy, math, pandas

class TestClass():
    def setUp(self):

        #create an artificial profile to trigger the temperature flag
        #sets first temperature to 99.9; otherwise identical to data/example.dat
        f1 = open("tests/testData/example.dat")
        self.demoProfile = wod.WodProfile(f1)
        self.dataframe = self.demoProfile.df()
        self.dictionary = self.demoProfile.npdict()
        self.head = self.demoProfile.header()

        f2 = open("tests/testData/iquod.01.dat")
        self.demoIQuODProfile = wod.WodProfile(f2)
        self.IQuODdataframe = self.demoIQuODProfile.df()
        self.IQuODdictionary = self.demoIQuODProfile.npdict()
        self.IQuODhead = self.demoIQuODProfile.header()        
        return

    def tearDown(self):
        return

    # ===================================================================
    # check the example from pp 124 of
    # http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
    # is extracted correctly by base functions.
    # data is in `example.dat`
    
    def test_latitude(self):
        '''
        check latitude == 61.930
        '''

        latitude = self.demoProfile.latitude()
        df_latitude = self.dataframe.latitude
        np_latitude = self.dictionary['latitude']
        header_latitude = self.head.latitude
        assert latitude == 61.930, 'latitude should have been 61.930, instead read %f' % latitude
        assert df_latitude == 61.930, 'dataframe latitude should have been 61.930, instead read %f' % df_latitude
        assert np_latitude == 61.930, 'np dict latitude should have been 61.930, instead read %f' % np_latitude
        assert header_latitude == 61.930, 'header latitude should have been 61.930, instead read %f' % header_latitude

    def test_latitude_error(self):
        '''
        check latitude error is None
        '''

        dLatitude = self.demoProfile.dlatitude()
        df_dlatitude = self.dataframe.dlatitude
        np_dlatitude = self.dictionary['dlatitude']
        header_dlatitude = self.head.dlatitude
        assert dLatitude is None, 'latitude error is undefined for this profile, instead read %f' % dLatitude
        assert df_dlatitude is None, 'dataframe latitude error is undefined for this profile, instead read %f' % df_dlatitude
        assert np_dlatitude is None, 'npdict latitude error is undefined for this profile, instead read %f' % np_dlatitude
        assert math.isnan(header_dlatitude) , 'header latitude error is undefined for this profile, instead read %f' % header_dlatitude

    def test_longitude(self):
        '''
        check longitude == -172.270
        '''

        longitude = self.demoProfile.longitude()
        df_longitude = self.dataframe.longitude
        np_longitude = self.dictionary['longitude']
        header_longitude = self.head.longitude
        assert longitude == -172.270, 'longitude should have been -172.270, instead read %f' % longitude
        assert df_longitude == -172.270, 'dataframe longitude should have been -172.270, instead read %f' % df_longitude
        assert np_longitude == -172.270, 'np dict longitude should have been -172.270, instead read %f' % np_longitude
        assert header_longitude == -172.270, 'header longitude should have been -172.270, instead read %f' % header_longitude

    def test_longitude_error(self):
        '''
        check longitude error is None
        '''

        dLongitude = self.demoProfile.dlongitude()
        df_dlongitude = self.dataframe.dlongitude
        np_dlongitude = self.dictionary['dlongitude']
        header_dlongitude = self.head.dlongitude
        assert dLongitude is None, 'longitude error is undefined for this profile, instead read %f' % dLongitude
        assert df_dlongitude is None, 'dataframe longitude error is undefined for this profile, instead read %f' % df_dlongitude
        assert np_dlongitude is None, 'np dict longitude error is undefined for this profile, instead read %f' % np_dlongitude
        assert math.isnan(header_dlongitude), 'header longitude error is undefined for this profile, instead read %f' % header_dlongitude

    def test_uid(self):
        '''
        check cruise ID == 67064
        '''

        uid = self.demoProfile.uid()
        df_uid = self.dataframe.uid
        np_uid = self.dictionary['uid']
        header_uid = self.head.uid
        assert uid == 67064, 'uid should have been 67064, instead read %f' % uid
        assert df_uid == 67064, 'dataframe uid should have been 67064, instead read %f' % df_uid
        assert np_uid == 67064, 'np dict uid should have been 67064, instead read %f' % np_uid
        assert header_uid == 67064, 'header uid should have been 67064, instead read %f' % header_uid

    def test_n_levels(self):
        '''
        check the number of levels == 4
        '''

        levels = self.demoProfile.n_levels()
        df_levels = self.dataframe.n_levels
        np_levels = self.dictionary['n_levels']
        header_n_levels = self.head.n_levels
        assert levels == 4, 'levels should have been 4, instead read %f' % levels
        assert df_levels == 4, 'dataframe levels should have been 4, instead read %f' % df_levels
        assert np_levels == 4, 'np dict levels should have been 4, instead read %f' % np_levels
        assert header_n_levels == 4, 'header levels should have been 4, instead read %f' % header_levels

    def test_year(self):
        '''
        check year == 1934
        '''

        year = self.demoProfile.year()
        df_year = self.dataframe.year
        np_year = self.dictionary['year']
        header_year = self.head.year
        assert year == 1934, 'year should have been 1934, instead read %f' % year
        assert df_year == 1934, 'dataframe year should have been 1934, instead read %f' % df_year
        assert np_year == 1934, 'np dict year should have been 1934, instead read %f' % np_year
        assert header_year == 1934, 'header year should have been 1934, instead read %f' % header_year

    def test_month(self):
        '''
        check month == 8
        '''

        month = self.demoProfile.month() 
        df_month = self.dataframe.month
        np_month = self.dictionary['month']
        header_month = self.head.month
        assert month == 8, 'month should have been 8, instead read %f' % month
        assert df_month == 8, 'dataframe month should have been 8, instead read %f' % df_month
        assert np_month == 8, 'np dict month should have been 8, instead read %f' % np_month
        assert header_month == 8, 'header month should have been 8, instead read %f' % header_month


    def test_day(self):
        '''
        check day == 7
        '''

        day = self.demoProfile.day()
        df_day = self.dataframe.day
        np_day = self.dictionary['day']
        header_day = self.head.day
        assert day == 7, 'day should have been 7, instead read %f' % day
        assert df_day == 7, 'dataframe day should have been 7, instead read %f' % df_day
        assert np_day == 7, 'np dict day should have been 7, instead read %f' % np_day
        assert header_day == 7, 'header day should have been 7, instead read %f' % header_day

    def test_time(self):
        ''' 
        check time == 10.37
        '''

        time = self.demoProfile.time()
        df_time = self.dataframe.time
        np_time = self.dictionary['time']
        header_time = self.head.time
        assert time == 10.37, 'time should have been 10.37, instead read %f' % time
        assert df_time == 10.37, 'dataframe time should have been 10.37, instead read %f' % df_time
        assert np_time == 10.37, 'np dict time should have been 10.37, instead read %f' % np_time
        assert header_time == 10.37, 'header time should have been 10.37, instead read %f' % header_time


    def test_datetime(self):
        '''
        check datetime 1934-8-7 10:22:12
        '''

        d = self.demoProfile.datetime()
        assert d == datetime(1934, 8, 7, 10, 22, 12), \
                'time should have been 1934-08-07 10:22:12, instead read %s' \
                % d


    def test_probe_type(self):
        '''
        check probe type == 7
        '''

        probe = self.demoProfile.probe_type() 
        df_probe = self.dataframe.probe_type
        np_probe = self.dictionary['probe_type']
        header_probe = self.head.probe_type
        assert probe == 7, 'probe should have been 7, instead read %f' % probe
        assert df_probe == 7, 'dataframe probe should have been 7, instead read %f' % df_probe
        assert np_probe == 7, 'np dict probe should have been 7, instead read %f' % np_probe
        assert header_probe == 7, 'header probe should have been 7, instead read %f' % header_probe


    def test_depth(self):
        '''
        check depths == [0.0, 10.0, 25.0, 50.0]
        '''

        truth = [0.0, 10.0, 25.0, 50.0]
        z = self.demoProfile.z()
        df_z = self.dataframe['depth']
        np_z = self.dictionary['z']
        assert numpy.array_equal(z, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % z.__str__()
        assert numpy.array_equal(df_z, truth), 'dataframe depths should have been [0, 10, 25, 50], instead read %s' % df_z.tolist().__str__()
        assert numpy.array_equal(np_z, truth), 'numpy dict depths should have been [0, 10, 25, 50], instead read %s' % np_z.__str__()

    def test_depth_error(self):
        '''
        check depth errors == [--,--,--,--] (all masked)
        '''

        truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
        dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
        dz = self.demoProfile.dz()
        df_dz = self.dataframe['ddepth']
        np_dz = self.dictionary['dz']
        assert numpy.array_equal(dz, truth), 'depth errors should have been all masked, instead read %s' % dz.__str__()
        assert df_dz.equals(dftruth), 'dataframe depth errors should have been all masked, instead read %s' % df_dz.__str__()
        assert numpy.array_equal(np_dz, truth), 'numpy dict depth errors should have been all masked, instead read %s' % np_dz.__str__()

    def test_temperature(self):
        '''
        check temperatures == [8.960, 8.950, 0.900, -1.230]
        '''

        truth = [8.960, 8.950, 0.900, -1.230]
        t = self.demoProfile.t()
        df_t = self.dataframe['temperature']
        np_t = self.dictionary['t']
        assert numpy.array_equal(t, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % t.__str__()
        assert numpy.array_equal(df_t, truth), 'dataframe temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read \n%s' % df_t.__str__()
        assert numpy.array_equal(np_t, truth), 'numpy dict temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % np_t.__str__()

    def test_temperature_error(self):
        '''
        check temperature errors == [--,--,--,--] (all masked)
        '''

        truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
        dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
        dt = self.demoProfile.dt()
        df_dt = self.dataframe['dtemperature']
        np_dt = self.dictionary['dt']
   
        assert numpy.array_equal(dt, truth), 'temperature errors should have been all masked, instead read %s' % dt.__str__()
        assert df_dt.equals(dftruth), 'dataframe temperature errors should have been all masked, instead read %s' % df_dt.__str__()
        assert numpy.array_equal(np_dt, truth), 'numpy dict temperature errors should have been all masked, instead read %s' % np_dt.__str__()


    def test_salinity(self):
        '''
        check salinities == [30.900, 30.900, 31.910, 32.410]
        '''
        
        truth = [30.900, 30.900, 31.910, 32.410]
        s = self.demoProfile.s()
        df_s = self.dataframe['salinity']
        np_s = self.dictionary['s']
        assert numpy.array_equal(s, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % s.__str__()
        assert numpy.array_equal(df_s, truth), 'dataframe salinities should have been [30.9, 30.9, 31.91, 32.41], instead read \n%s' % df_s.__str__()
        assert numpy.array_equal(np_s, truth), 'numpy dict salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % np_s.__str__()

    def test_salinity_error(self):
        '''
        check salinity errors == [--,--,--,--] (all masked)
        '''

        truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
        dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
        ds = self.demoProfile.ds()
        df_ds = self.dataframe['dsalinity']
        np_ds = self.dictionary['ds']
   
        assert numpy.array_equal(ds, truth), 'salinity errors should have been all masked, instead read %s' % ds.__str__()
        assert df_ds.equals(dftruth), 'dataframe salinity errors should have been all masked, instead read %s' % df_ds.__str__()
        assert numpy.array_equal(np_ds, truth), 'numpy dict salinity errors should have been all masked, instead read %s' % np_ds.__str__()

    def test_oxygen(self):
        '''
        check oxygen levels = [6.750, 6.700, 8.620, 7.280]
        '''

        truth = [6.750, 6.700, 8.620, 7.280]
        o2 = self.demoProfile.oxygen()
        df_o2 = self.dataframe['oxygen']
        np_o2 = self.dictionary['oxygen']

        assert numpy.array_equal(o2, truth), 'oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % o2.__str__()
        assert numpy.array_equal(df_o2, truth), 'dataframe oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read \n%s' % df_o2.__str__()
        assert numpy.array_equal(np_o2, truth), 'numpy dict oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % np_o2.__str__()

    def test_phosphate(self):
        '''
        check phosphate levels = [0.650, 0.710, 0.900, 1.170]
        '''

        truth = [0.650, 0.710, 0.900, 1.170]
        phos = self.demoProfile.phosphate()
        df_phos = self.dataframe['phosphate']
        np_phos = self.dictionary['phosphate']

        assert numpy.array_equal(phos, truth), 'phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % phos.__str__()
        assert numpy.array_equal(df_phos, truth), 'dataframe phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read \n%s' % df_phos.__str__()
        assert numpy.array_equal(np_phos, truth), 'numpy dict phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % np_phos.__str__()

    def test_silicate(self):
        '''
        check silicate levels = [20.500, 12.300, 15.400, 25.600]
        '''

        truth = [20.500, 12.300, 15.400, 25.600]
        sili = self.demoProfile.silicate()
        df_sili = self.dataframe['silicate']
        np_sili = self.dictionary['silicate']

        assert numpy.array_equal(sili, truth), 'silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % sili.__str__()
        assert numpy.array_equal(df_sili, truth), 'dataframe silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read \n%s' % df_sili.__str__()
        assert numpy.array_equal(np_sili, truth), 'numpy dict silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % np_sili.__str__()

    def test_pH(self):
        '''
        check pH levels = [8.100, 8.100, 8.100, 8.050]
        '''

        truth = [8.100, 8.100, 8.100, 8.050]
        pH = self.demoProfile.pH()
        df_pH = self.dataframe['pH']
        np_pH = self.dictionary['pH']

        assert numpy.array_equal(pH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % pH.__str__()
        assert numpy.array_equal(df_pH, truth), 'dataframe pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read \n%s' % df_pH.__str__()
        assert numpy.array_equal(np_pH, truth), 'numpy dict pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % np_pH.__str__()

    def test_PI(self):
        '''
        check for PI code
        '''

        truth = [{'Variable code': 0, 'P.I. code': 215}, {'Variable code': 0, 'P.I. code': 216}, {'Variable code': -5006, 'P.I. code': 217}, {'Variable code': -5002, 'P.I. code': 218}]
        PIs = self.demoProfile.PIs()
        df_PIs = self.dataframe.PIs
        np_PIs = self.dictionary['PIs']
        assert numpy.array_equal(PIs, truth), 'PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read %s' % PIs.__str__()
        assert numpy.array_equal(df_PIs, truth), 'dataframe PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read \n%s' % PIs.__str__()
        assert numpy.array_equal(np_PIs, truth), 'numpy dict PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read %s' % PIs.__str__()

    def test_originator_cruise(self):

        truth = 'STOCS85A'
        originator_cruise = self.demoProfile.originator_cruise()
        df_originator_cruise = self.dataframe.originator_cruise
        np_originator_cruise = self.dictionary['originator_cruise']
        assert originator_cruise == truth, 'Originator cruise should have been STOCS85A, instead read %s' % originator_cruise
        assert df_originator_cruise == truth, 'dataframe riginator cruise should have been STOCS85A, instead read %s' % df_originator_cruise
        assert np_originator_cruise == truth, 'numpy dict originator cruise should have been STOCS85A, instead read %s' % np_originator_cruise

    def test_originator_station(self):

        truth = None
        originator_station = self.demoProfile.originator_station()
        df_originator_station = self.dataframe.originator_station
        np_originator_station = self.dictionary['originator_station']
        assert originator_station == truth
        assert df_originator_station == truth
        assert np_originator_station == truth

    # ===================================================================
    # check that an IQuOD v 0.1 profile is unpacked correctly
    # data is in `iquod.01.dat`

    def test_iquod_latitude(self):
        '''
        check latitude == 34.5883
        '''

        latitude = self.demoIQuODProfile.latitude()
        df_latitude = self.IQuODdataframe.latitude
        np_latitude = self.IQuODdictionary['latitude']
        header_latitude = self.IQuODhead.latitude
        assert latitude == 34.5883, 'latitude should have been 34.5883, instead read %f' % latitude
        assert df_latitude == 34.5883, 'dataframe latitude should have been 34.5883, instead read %f' % df_latitude
        assert np_latitude == 34.5883, 'np dict latitude should have been 34.5883, instead read %f' % np_latitude
        assert header_latitude == 34.5883, 'header latitude should have been 34.5883, instead read %f' % header_latitude  

    def test_iquod_latitude_error(self):
        '''
        check latitude error is None
        '''

        dLatitude = self.demoIQuODProfile.dlatitude()
        df_dlatitude = self.IQuODdataframe.dlatitude
        np_dlatitude = self.IQuODdictionary['dlatitude']
        header_dlatitude = self.IQuODhead.dlatitude
        assert dLatitude is None, 'latitude error is undefined for this profile, instead read %f' % dLatitude
        assert df_dlatitude is None, 'dataframe latitude error is undefined for this profile, instead read %f' % df_dlatitude
        assert np_dlatitude is None, 'npdict latitude error is undefined for this profile, instead read %f' % np_dlatitude
        assert math.isnan(header_dlatitude) , 'header latitude error is undefined for this profile, instead read %f' % header_dlatitude

    def test_iquod_longitude(self):
        '''
        check longitude == 134.2433
        '''

        longitude = self.demoIQuODProfile.longitude()
        df_longitude = self.IQuODdataframe.longitude
        np_longitude = self.IQuODdictionary['longitude']
        header_longitude = self.IQuODhead.longitude
        assert longitude == 134.2433, 'longitude should have been 134.2433, instead read %f' % longitude
        assert df_longitude == 134.2433, 'dataframe longitude should have been 134.2433, instead read %f' % df_longitude
        assert np_longitude == 134.2433, 'np dict longitude should have been 134.2433, instead read %f' % np_longitude
        assert header_longitude == 134.2433, 'header longitude should have been 134.2433, instead read %f' % header_longitude

    def test_iquod_longitude_error(self):
        '''
        check longitude error is None
        '''

        dLongitude = self.demoIQuODProfile.dlongitude()
        df_dlongitude = self.IQuODdataframe.dlongitude
        np_dlongitude = self.IQuODdictionary['dlongitude']
        header_dlongitude = self.IQuODhead.dlongitude
        assert dLongitude is None, 'longitude error is undefined for this profile, instead read %f' % dLongitude
        assert df_dlongitude is None, 'dataframe longitude error is undefined for this profile, instead read %f' % df_dlongitude
        assert np_dlongitude is None, 'npdict longitude error is undefined for this profile, instead read %f' % np_dlongitude
        assert math.isnan(header_dlongitude) , 'header longitude error is undefined for this profile, instead read %f' % header_dlongitude


    def test_iquod_uid(self):
        '''
        check cruise ID == 13393621
        '''

        uid = self.demoIQuODProfile.uid()
        df_uid = self.IQuODdataframe.uid
        np_uid = self.IQuODdictionary['uid']
        header_uid = self.IQuODhead.uid
        assert uid == 13393621, 'uid should have been 13393621, instead read %f' % uid
        assert df_uid == 13393621, 'dataframe uid should have been 13393621, instead read %f' % df_uid
        assert np_uid == 13393621, 'np dict uid should have been 13393621, instead read %f' % np_uid
        assert header_uid == 13393621, 'header uid should have been 13393621, instead read %f' % header_uid

    def test_iquod_n_levels(self):
        '''
        check the number of levels == 5
        '''

        levels = self.demoIQuODProfile.n_levels()
        df_levels = self.IQuODdataframe.n_levels
        np_levels = self.IQuODdictionary['n_levels']
        header_n_levels = self.IQuODhead.n_levels
        assert levels == 5, 'levels should have been 5, instead read %f' % levels
        assert df_levels == 5, 'dataframe levels should have been 5, instead read %f' % df_levels
        assert np_levels == 5, 'np dict levels should have been 5, instead read %f' % np_levels
        assert header_n_levels == 5, 'header levels should have been 5, instead read %f' % header_levels

    def test_iquod_year(self):
        '''
        check year == 2000
        '''

        year = self.demoIQuODProfile.year()
        df_year = self.IQuODdataframe.year
        np_year = self.IQuODdictionary['year']
        header_year = self.IQuODhead.year
        assert year == 2000, 'year should have been 2000, instead read %f' % year
        assert df_year == 2000, 'dataframe year should have been 2000, instead read %f' % df_year
        assert np_year == 2000, 'np dict year should have been 2000, instead read %f' % np_year
        assert header_year == 2000, 'header year should have been 2000, instead read %f' % header_year



    def test_iquod_month(self):
        '''
        check month == 1
        '''

        month = self.demoIQuODProfile.month() 
        df_month = self.IQuODdataframe.month
        np_month = self.IQuODdictionary['month']
        header_month = self.IQuODhead.month
        assert month == 1, 'month should have been 1, instead read %f' % month
        assert df_month == 1, 'dataframe month should have been 1, instead read %f' % df_month
        assert np_month == 1, 'np dict month should have been 1, instead read %f' % np_month
        assert header_month == 1, 'header month should have been 1, instead read %f' % header_month


    def test_iquod_day(self):
        '''
        check day == 4
        '''

        day = self.demoIQuODProfile.day()
        df_day = self.IQuODdataframe.day
        np_day = self.IQuODdictionary['day']
        header_day = self.IQuODhead.day
        assert day == 4, 'day should have been 4, instead read %f' % day
        assert df_day == 4, 'dataframe day should have been 4, instead read %f' % df_day
        assert np_day == 4, 'np dict day should have been 4, instead read %f' % np_day
        assert header_day == 4, 'header day should have been 4, instead read %f' % header_day

    def test_iquod_time(self):
        ''' 
        check time == 3.7
        '''

        time = self.demoIQuODProfile.time()
        df_time = self.IQuODdataframe.time
        np_time = self.IQuODdictionary['time']
        header_time = self.IQuODhead.time
        assert time == 3.7, 'time should have been 3.7, instead read %f' % time
        assert df_time == 3.7, 'dataframe time should have been 3.7, instead read %f' % df_time
        assert np_time == 3.7, 'np dict time should have been 3.7, instead read %f' % np_time
        assert header_time == 3.7, 'header time should have been 3.7, instead read %f' % header_time


    def test_iquod_datetime(self):
        '''
        check datetime 2000-1-4 3:42:00
        '''

        d = self.demoIQuODProfile.datetime()
        assert d == datetime(2000, 1, 4, 3, 42, 00), \
                'time should have been 2000-01-04 3:42:00, instead read %s' \
                % d


    def test_iquod_probe_type(self):
        '''
        check probe type == 4
        '''

        probe = self.demoIQuODProfile.probe_type() 
        df_probe = self.IQuODdataframe.probe_type
        np_probe = self.IQuODdictionary['probe_type']
        header_probe = self.IQuODhead.probe_type
        assert probe == 4, 'probe should have been 4, instead read %f' % probe
        assert df_probe == 4, 'dataframe probe should have been 4, instead read %f' % df_probe
        assert np_probe == 4, 'np dict probe should have been 4, instead read %f' % np_probe
        assert header_probe == 4, 'header probe should have been 4, instead read %f' % header_probe


    def test_iquod_depth(self):
        '''
        check depths == [0,2,5,10,20]
        '''

        truth = [0,2,5,10,20]
        z = self.demoIQuODProfile.z()
        df_z = self.IQuODdataframe['depth']
        np_z = self.IQuODdictionary['z']
        assert numpy.array_equal(z, truth), 'depths should have been [0,2,5,10,20], instead read %s' % z.__str__()
        assert numpy.array_equal(df_z, truth), 'dataframe depths should have been [0,2,5,10,20], instead read %s' % df_z.tolist().__str__()
        assert numpy.array_equal(np_z, truth), 'numpy dict depths should have been [0,2,5,10,20], instead read %s' % np_z.__str__()

    def test_iquod_depth_error(self):
        '''
        check depth errors == [0,.0016,.004,.008,.016]
        '''

        truth = [0,.0016,.004,.008,.016]
        dz = self.demoIQuODProfile.dz()
        df_dz = self.IQuODdataframe['ddepth']
        np_dz = self.IQuODdictionary['dz']
        assert numpy.array_equal(dz, truth), 'depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % dz.__str__()
        assert numpy.array_equal(df_dz, truth), 'dataframe depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % df_dz.__str__()
        assert numpy.array_equal(np_dz, truth), 'numpy dict depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % np_dz.__str__()

    def test_iquod_temperature(self):
        '''
        check temperatures == [11.1,11.2,11.0,11.0,11.0]
        '''

        truth = [11.1,11.2,11.0,11.0,11.0]
        t = self.demoIQuODProfile.t()
        df_t = self.IQuODdataframe['temperature']
        np_t = self.IQuODdictionary['t']
        assert numpy.array_equal(t, truth), 'temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read %s' % t.__str__()
        assert numpy.array_equal(df_t, truth), 'dataframe temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read \n%s' % df_t.__str__()
        assert numpy.array_equal(np_t, truth), 'numpy dict temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read %s' % np_t.__str__()

    def test_iquod_temperature_error(self):
        '''
        check temperature errors == [.01,.01,.01,.01,.01]
        '''

        truth = [.01,.01,.01,.01,.01]
        dt = self.demoIQuODProfile.dt()
        df_dt = self.IQuODdataframe['dtemperature']
        np_dt = self.IQuODdictionary['dt']
        assert numpy.array_equal(dt, truth), 'temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % dt.__str__()
        assert numpy.array_equal(df_dt, truth), 'dataframe temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % df_dt.__str__()
        assert numpy.array_equal(np_dt, truth), 'numpy dict temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % np_dt.__str__()

    def test_iquod_salinity(self):
        '''
        check salinities == [31.53,31.47,31.49,31.49,31.50]
        '''
        
        truth = [31.53,31.47,31.49,31.49,31.50]
        s = self.demoIQuODProfile.s()
        df_s = self.IQuODdataframe['salinity']
        np_s = self.IQuODdictionary['s']
        assert numpy.array_equal(s, truth), 'salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read %s' % s.__str__()
        assert numpy.array_equal(df_s, truth), 'dataframe salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read \n%s' % df_s.__str__()
        assert numpy.array_equal(np_s, truth), 'numpy dict salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read %s' % np_s.__str__()

    def test_iquod_salinity_error(self):
        '''
        check temperature errors == [.02,.02,.02,.02,.02]
        '''

        truth = [.02,.02,.02,.02,.02]
        ds = self.demoIQuODProfile.ds()
        df_ds = self.IQuODdataframe['dsalinity']
        np_ds = self.IQuODdictionary['ds']
        assert numpy.array_equal(ds, truth), 'salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % ds.__str__()
        assert numpy.array_equal(df_ds, truth), 'dataframe salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % df_ds.__str__()
        assert numpy.array_equal(np_ds, truth), 'numpy dict salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % np_ds.__str__()




