from datetime import datetime, timedelta
from wodpy import wod, wodnc
from wodpy.extra import Wod4CoTeDe
import numpy, pytest

@pytest.fixture
def demoProfile():
    # WOD13 format data
    file = open("tests/testData/classic.dat")
    return Wod4CoTeDe(file)

@pytest.fixture
def demonetCDF():
    ragged = wodnc.Ragged("tests/testData/ocldb1570984477.6279_OSD.nc")
    return Wod4CoTeDe(ragged, 55)
    
def test_latitude(demoProfile, demonetCDF):
    '''
    check latitude == 61.930
    '''

    latitude = demoProfile.attributes['LATITUDE']
    nclatitude = demonetCDF.attributes['LATITUDE']
    assert latitude == 61.930, 'latitude should have been 61.930, instead read %f' % latitude
    assert round(nclatitude, 2) == 61.93, 'latitude should have been about 61.93, instead read %f' % nclatitude

def test_longitude(demoProfile, demonetCDF):
    '''
    check longitude == -172.270
    '''

    longitude = demoProfile.attributes['LONGITUDE']
    nclongitude = demonetCDF.attributes['LONGITUDE']
    assert longitude == -172.270, 'longitude should have been -172.270, instead read %f' % longitude
    assert round(nclongitude, 2) == -172.27, 'longitude should have been about -172.270, instead read %f' % nclongitude

def test_uid(demoProfile, demonetCDF):
    '''
    check cruise ID == 67064
    '''

    uid = demoProfile.attributes['uid']
    ncuid = demonetCDF.attributes['uid']
    assert uid == 67064, 'uid should have been 67064, instead read %f' % uid
    assert ncuid == 67064, 'uid should have been 67064, instead read %f' % ncuid

def test_n_levels(demoProfile, demonetCDF):
    '''
    check the number of levels == 4
    '''

    levels = demoProfile.attributes['n_levels']
    nclevels = demonetCDF.attributes['n_levels']
    assert levels == 4, 'levels should have been 4, instead read %f' % levels
    assert nclevels == 4, 'levels should have been 4, instead read %f' % nclevels

def test_datetime(demoProfile, demonetCDF):
    ''' 
    check datetime == 1934-08-07 10:22:12
    '''

    truth = datetime(1934, 8, 7, 10, 22, 12)
    time = demoProfile.attributes['datetime']
    nctime = demonetCDF.attributes['datetime']
    assert time - truth < timedelta(minutes=1), 'time should have been about 1934-08-07 10:22:12, instead read %s' % time
    assert nctime - truth < timedelta(minutes=1), 'time should have been about 1934-08-07 10:22:12, instead read %s' % nctime


def test_probe_type(demoProfile, demonetCDF):
    '''
    check probe type == 7 (bottle/rossete/net)
    '''

    probe = demoProfile.attributes['probe_type']
    ncprobe = demonetCDF.attributes['probe_type']
    assert probe == 'bottle/rossete/net', 'probe should have been , instead read %s' % probe
    assert ncprobe == 'bottle/rossete/net', 'probe should have been , instead read %s' % ncprobe


def test_depth(demoProfile, demonetCDF):
    '''
    check depths == [0.0, 10.0, 25.0, 50.0]
    '''

    truth = [0.0, 10.0, 25.0, 50.0]
    z = demoProfile['DEPTH']
    ncz = demonetCDF['DEPTH']
    assert numpy.array_equal(z, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % z.__str__()
    assert numpy.array_equal(ncz, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % ncz.__str__()


def test_temperature(demoProfile, demonetCDF):
    '''
    check temperatures == [8.960, 8.950, 0.900, -1.230]
    '''

    truth = [8.960, 8.950, 0.900, -1.230]
    t = [round(float(x),2) for x in demoProfile['TEMP']]
    nct = [round(float(x),2) for x in demonetCDF['TEMP']]
    assert numpy.array_equal(t, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % t.__str__()
    assert numpy.array_equal(nct, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % nct.__str__()


def test_salinity(demoProfile, demonetCDF):
    '''
    check salinities == [30.900, 30.900, 31.910, 32.410]
    '''
    
    truth = [30.900, 30.900, 31.910, 32.410]
    s = [round(float(x),2) for x in demoProfile['PSAL']]
    ncs = [round(float(x),2) for x in demonetCDF['PSAL']]
    assert numpy.array_equal(s, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % s.__str__()
    assert numpy.array_equal(ncs, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % ncs.__str__()

def test_oxygen(demoProfile, demonetCDF):
    '''
    check oxygen levels = [6.750, 6.700, 8.620, 7.280]
    '''

    truth = [6.750, 6.700, 8.620, 7.280]
    truth_nc = [293.90298, 291.90366, 375.3761,  317.39523]
    o2 = [round(float(x),2) for x in demoProfile['oxygen']]
    nco2 = [round(float(x),5) for x in demonetCDF['oxygen']]
    assert numpy.array_equal(o2, truth), 'oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % o2.__str__()
    assert numpy.array_equal(nco2, truth_nc), 'oxygen levels should have been [293.90298, 291.90366, 375.3761,  317.39523], instead read %s' % nco2.__str__()


def test_phosphate(demoProfile, demonetCDF):
    '''
    check phosphate levels = [0.650, 0.710, 0.900, 1.170]
    '''

    truth = [0.650, 0.710, 0.900, 1.170]
    truth_nc = [0.63, 0.69, 0.88, 1.14]
    phos = demoProfile['phosphate']
    phos = [round(float(x),2) for x in demoProfile['phosphate']]
    ncphos = [round(float(x),2) for x in demonetCDF['phosphate']]
    assert numpy.array_equal(phos, truth), 'phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % phos.__str__()
    assert numpy.array_equal(ncphos, truth_nc), 'phosphate levels should have been [0.63, 0.69, 0.88, 1.14], instead read %s' % ncphos.__str__()


def test_silicate(demoProfile, demonetCDF):
    '''
    check silicate levels = [20.500, 12.300, 15.400, 25.600]
    '''

    truth = [20.500, 12.300, 15.400, 25.600]
    truth_nc = [20, 12, 15, 25]
    sili = [round(float(x),2) for x in demoProfile['silicate']]
    ncsili = [round(float(x),2) for x in demonetCDF['silicate']]
    assert numpy.array_equal(sili, truth), 'silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % sili.__str__()
    assert numpy.array_equal(ncsili, truth_nc), 'silicate levels should have been [20, 12, 15, 25], instead read %s' % ncsili.__str__()


def test_pH(demoProfile, demonetCDF):
    '''
    check pH levels = [8.100, 8.100, 8.100, 8.050]
    '''

    truth = [8.100, 8.100, 8.100, 8.050]
    pH = demoProfile['pH']
    pH = [round(float(x),2) for x in demoProfile['pH']]
    ncpH = [round(float(x),2) for x in demonetCDF['pH']]
    assert numpy.array_equal(pH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % pH.__str__()
    assert numpy.array_equal(ncpH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % ncpH.__str__()




