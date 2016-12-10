from datetime import datetime
from wodpy import wod
import numpy

class TestClass():
    def setUp(self):

        #create an artificial profile to trigger the temperature flag
        #sets first temperature to 99.9; otherwise identical to data/example.dat
        file = open("tests/testData/example.dat")

        self.demoProfile = wod.WodProfile(file)
        self.dataframe = self.demoProfile.df()
        self.dictionary = self.demoProfile.npdict()
        self.head = self.demoProfile.header()
        return

    def tearDown(self):
        return

    # ===================================================================
    # check the example from pp 137 of
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
        assert probe == 7, 'probe should have been , instead read %f' % probe
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

    def test_station(self):

        truth = None
        station = self.demoProfile.station()
        df_station = self.dataframe.station
        np_station = self.dictionary['station']
        assert station is truth
        assert df_station is truth
        assert np_station is truth
