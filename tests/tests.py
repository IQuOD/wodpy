from wodpy import wod

class TestClass():
    def setUp(self):

        #create an artificial profile to trigger the temperature flag
        #sets first temperature to 99.9; otherwise identical to data/example.dat
        file = open("tests/testData/example.dat")

        self.demoProfile = wod.WodProfile(file)

        return

    def tearDown(self):
        return

    # ===================================================================
    # check the example from pp 137 of
    # http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
    # is extracted correctly.
    # data is in `example.dat`
    
    def test_latitude(self):
        '''
        check latitude == 61.930
        '''

        latitude = self.demoProfile.latitude()
        assert latitude == 61.930, 'latitude should have been 61.930, instead read %f' % latitude

    def test_longitude(self):
        '''
        check longitude == -172.270
        '''

        longitude = self.demoProfile.longitude()
        assert longitude == -172.270, ' should have been , instead read %f' % longitude

    def test_uid(self):
        '''
        check cruise ID == 67064
        '''

        uid = self.demoProfile.uid()
        assert uid == 67064, ' should have been , instead read %f' % uid

    def test_n_levels(self):
        '''
        check the number of levels == 4
        '''

        levels = self.demoProfile.n_levels()
        assert levels == 4, ' should have been , instead read %f' % levels

    def test_year(self):
        '''
        check year == 1934
        '''

        year = self.demoProfile.year()
        assert year == 1934, ' should have been , instead read %f' % year

    def test_month(self):
        '''
        check month == 8
        '''

        month = self.demoProfile.month() 
        assert month == 8, ' should have been , instead read %f' % month

    def test_day(self):
        '''
        check day == 7
        '''

        day = self.demoProfile.day()
        assert day == 7, ' should have been , instead read %f' % day

    def test_time(self):
        ''' 
        check time == 10.37
        '''

        time = self.demoProfile.time()
        assert time == 10.37, ' should have been , instead read %f' % time

    def test_probe_type(self):
        '''
        check probe type == 7
        '''

        probe = self.demoProfile.probe_type() 
        assert probe == 7, ' should have been , instead read %f' % probe