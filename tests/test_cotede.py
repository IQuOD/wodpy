from datetime import datetime

from wodpy import wod
from wodpy.extra import Wod4CoTeDe
import numpy

class TestClass():
    def setUp(self):

        #create an artificial profile to trigger the temperature flag
        #sets first temperature to 99.9; otherwise identical to data/example.dat
        file = open("tests/testData/example.dat")

        self.demoProfile = Wod4CoTeDe(file)
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

        latitude = self.demoProfile.attributes['LATITUDE']
        assert latitude == 61.930, 'latitude should have been 61.930, instead read %f' % latitude


    def test_longitude(self):
        '''
        check longitude == -172.270
        '''

        longitude = self.demoProfile.attributes['LONGITUDE']
        assert longitude == -172.270, 'longitude should have been -172.270, instead read %f' % longitude

    def test_uid(self):
        '''
        check cruise ID == 67064
        '''

        uid = self.demoProfile.attributes['uid']
        assert uid == 67064, 'uid should have been 67064, instead read %f' % uid


    def test_n_levels(self):
        '''
        check the number of levels == 4
        '''

        levels = self.demoProfile.attributes['n_levels']
        assert levels == 4, 'levels should have been 4, instead read %f' % levels


    def test_datetime(self):
        ''' 
        check datetime == 1934-08-07 10:22:11
        '''

        truth = datetime(1934, 8, 7, 10, 22, 11)
        time = self.demoProfile.attributes['datetime']
        assert time == truth, \
                'time should have been 1934-08-07 10:22:11, instead read %s' \
                % time


    def test_probe_type(self):
        '''
        check probe type == 7 (bottle/rossete/net)
        '''

        probe = self.demoProfile.attributes['probe_type']
        assert probe == 'bottle/rossete/net', \
                'probe should have been , instead read %s' % probe


    def test_depth(self):
        '''
        check depths == [0.0, 10.0, 25.0, 50.0]
        '''

        truth = [0.0, 10.0, 25.0, 50.0]
        z = self.demoProfile['DEPTH']
        assert numpy.array_equal(z, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % z.__str__()


    def test_temperature(self):
        '''
        check temperatures == [8.960, 8.950, 0.900, -1.230]
        '''

        truth = [8.960, 8.950, 0.900, -1.230]
        t = self.demoProfile['TEMP']
        assert numpy.array_equal(t, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % t.__str__()


    def test_salinity(self):
        '''
        check salinities == [30.900, 30.900, 31.910, 32.410]
        '''
        
        truth = [30.900, 30.900, 31.910, 32.410]
        s = self.demoProfile['PSAL']
        assert numpy.array_equal(s, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % s.__str__()


    def test_oxygen(self):
        '''
        check oxygen levels = [6.750, 6.700, 8.620, 7.280]
        '''

        truth = [6.750, 6.700, 8.620, 7.280]
        o2 = self.demoProfile['oxygen']

        assert numpy.array_equal(o2, truth), 'oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % o2.__str__()


    def test_phosphate(self):
        '''
        check phosphate levels = [0.650, 0.710, 0.900, 1.170]
        '''

        truth = [0.650, 0.710, 0.900, 1.170]
        phos = self.demoProfile['phosphate']

        assert numpy.array_equal(phos, truth), 'phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % phos.__str__()


    def test_silicate(self):
        '''
        check silicate levels = [20.500, 12.300, 15.400, 25.600]
        '''

        truth = [20.500, 12.300, 15.400, 25.600]
        sili = self.demoProfile['silicate']

        assert numpy.array_equal(sili, truth), 'silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % sili.__str__()


    def test_pH(self):
        '''
        check pH levels = [8.100, 8.100, 8.100, 8.050]
        '''

        truth = [8.100, 8.100, 8.100, 8.050]
        pH = self.demoProfile['pH']

        assert numpy.array_equal(pH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % pH.__str__()
