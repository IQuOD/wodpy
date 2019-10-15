from datetime import datetime
from wodpy import netcdf
import numpy, math, pandas

class TestClass():
    def setUp(self):

        # example from pp 124 of http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
        # with IQuOD flags
        r = netcdf.Ragged("tests/testData/ocldb1570984477.6279_OSD.nc")
        self.classic1 = netcdf.Profile(r, 55)

        return

    def tearDown(self):
        return

    def test_latitude(self):
        '''
        check latitude == 61.93
        '''

        latitude = self.classic1.latitude()
        assert round(latitude, 2) == 61.93, 'latitude should have been approx 61.93, instead read %f' % latitude
        
