from datetime import datetime, timedelta
from wodpy import wod, wodnc
from wodpy.extra import Wod4CoTeDe
import numpy

class TestClass():
    def setUp(self):

        #create an artificial profile to trigger the temperature flag
        #sets first temperature to 99.9; otherwise identical to data/example.dat
        file = open("tests/testData/classic.dat")
        self.demoProfile = Wod4CoTeDe(file)

        ragged = wodnc.Ragged("tests/testData/ocldb1570984477.6279_OSD.nc")
        self.demonetCDF = Wod4CoTeDe(ragged, 55)
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
        nclatitude = self.demonetCDF.attributes['LATITUDE']
        assert latitude == 61.930, 'latitude should have been 61.930, instead read %f' % latitude
        assert round(nclatitude, 2) == 61.93, 'latitude should have been about 61.93, instead read %f' % nclatitude

    def test_longitude(self):
        '''
        check longitude == -172.270
        '''

        longitude = self.demoProfile.attributes['LONGITUDE']
        nclongitude = self.demonetCDF.attributes['LONGITUDE']
        assert longitude == -172.270, 'longitude should have been -172.270, instead read %f' % longitude
        assert round(nclongitude, 2) == -172.27, 'longitude should have been about -172.270, instead read %f' % nclongitude

    def test_uid(self):
        '''
        check cruise ID == 67064
        '''

        uid = self.demoProfile.attributes['uid']
        ncuid = self.demonetCDF.attributes['uid']
        assert uid == 67064, 'uid should have been 67064, instead read %f' % uid
        assert ncuid == 67064, 'uid should have been 67064, instead read %f' % ncuid

    def test_n_levels(self):
        '''
        check the number of levels == 4
        '''

        levels = self.demoProfile.attributes['n_levels']
        nclevels = self.demonetCDF.attributes['n_levels']
        assert levels == 4, 'levels should have been 4, instead read %f' % levels
        assert nclevels == 4, 'levels should have been 4, instead read %f' % nclevels

    def test_datetime(self):
        ''' 
        check datetime == 1934-08-07 10:22:12
        '''

        truth = datetime(1934, 8, 7, 10, 22, 12)
        time = self.demoProfile.attributes['datetime']
        nctime = self.demonetCDF.attributes['datetime']
        assert time - truth < timedelta(minutes=1), 'time should have been about 1934-08-07 10:22:12, instead read %s' % time
        assert nctime - truth < timedelta(minutes=1), 'time should have been about 1934-08-07 10:22:12, instead read %s' % nctime


    def test_probe_type(self):
        '''
        check probe type == 7 (bottle/rossete/net)
        '''

        probe = self.demoProfile.attributes['probe_type']
        ncprobe = self.demonetCDF.attributes['probe_type']
        assert probe == 'bottle/rossete/net', 'probe should have been , instead read %s' % probe
        assert ncprobe == 'bottle/rossete/net', 'probe should have been , instead read %s' % ncprobe


    def test_depth(self):
        '''
        check depths == [0.0, 10.0, 25.0, 50.0]
        '''

        truth = [0.0, 10.0, 25.0, 50.0]
        z = self.demoProfile['DEPTH']
        ncz = self.demonetCDF['DEPTH']
        assert numpy.array_equal(z, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % z.__str__()
        assert numpy.array_equal(ncz, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % ncz.__str__()


    def test_temperature(self):
        '''
        check temperatures == [8.960, 8.950, 0.900, -1.230]
        '''

        truth = [8.960, 8.950, 0.900, -1.230]
        t = [round(float(x),2) for x in self.demoProfile['TEMP']]
        nct = [round(float(x),2) for x in self.demonetCDF['TEMP']]
        assert numpy.array_equal(t, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % t.__str__()
        assert numpy.array_equal(nct, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % nct.__str__()


    def test_salinity(self):
        '''
        check salinities == [30.900, 30.900, 31.910, 32.410]
        '''
        
        truth = [30.900, 30.900, 31.910, 32.410]
        s = [round(float(x),2) for x in self.demoProfile['PSAL']]
        ncs = [round(float(x),2) for x in self.demonetCDF['PSAL']]
        assert numpy.array_equal(s, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % s.__str__()
        assert numpy.array_equal(ncs, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % ncs.__str__()

    def test_oxygen(self):
        '''
        check oxygen levels = [6.750, 6.700, 8.620, 7.280]
        '''

        truth = [6.750, 6.700, 8.620, 7.280]
        truth_nc = [293.90298, 291.90366, 375.3761,  317.39523]
        o2 = [round(float(x),2) for x in self.demoProfile['oxygen']]
        nco2 = [round(float(x),5) for x in self.demonetCDF['oxygen']]
        assert numpy.array_equal(o2, truth), 'oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % o2.__str__()
        assert numpy.array_equal(nco2, truth_nc), 'oxygen levels should have been [293.90298, 291.90366, 375.3761,  317.39523], instead read %s' % nco2.__str__()


    def test_phosphate(self):
        '''
        check phosphate levels = [0.650, 0.710, 0.900, 1.170]
        '''

        truth = [0.650, 0.710, 0.900, 1.170]
        truth_nc = [0.63, 0.69, 0.88, 1.14]
        phos = self.demoProfile['phosphate']
        phos = [round(float(x),2) for x in self.demoProfile['phosphate']]
        ncphos = [round(float(x),2) for x in self.demonetCDF['phosphate']]
        assert numpy.array_equal(phos, truth), 'phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % phos.__str__()
        assert numpy.array_equal(ncphos, truth_nc), 'phosphate levels should have been [0.63, 0.69, 0.88, 1.14], instead read %s' % ncphos.__str__()


    def test_silicate(self):
        '''
        check silicate levels = [20.500, 12.300, 15.400, 25.600]
        '''

        truth = [20.500, 12.300, 15.400, 25.600]
        truth_nc = [20, 12, 15, 25]
        sili = [round(float(x),2) for x in self.demoProfile['silicate']]
        ncsili = [round(float(x),2) for x in self.demonetCDF['silicate']]
        assert numpy.array_equal(sili, truth), 'silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % sili.__str__()
        assert numpy.array_equal(ncsili, truth_nc), 'silicate levels should have been [20, 12, 15, 25], instead read %s' % ncsili.__str__()


    def test_pH(self):
        '''
        check pH levels = [8.100, 8.100, 8.100, 8.050]
        '''

        truth = [8.100, 8.100, 8.100, 8.050]
        pH = self.demoProfile['pH']
        pH = [round(float(x),2) for x in self.demoProfile['pH']]
        ncpH = [round(float(x),2) for x in self.demonetCDF['pH']]
        assert numpy.array_equal(pH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % pH.__str__()
        assert numpy.array_equal(ncpH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % ncpH.__str__()




