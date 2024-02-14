from datetime import datetime, timedelta
from wodpy import wodnc
import numpy, math, pandas, pytest

@pytest.fixture
def classic1():
    # example from pp 124 of http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
    # with IQuOD flags
    r = wodnc.Ragged("tests/testData/ocldb1570984477.6279_OSD.nc")
    return wodnc.ncProfile(r, 55)

def test_latitude(classic1):
    '''
    check latitude == 61.93
    '''

    latitude = classic1.latitude()
    assert round(latitude, 2) == 61.93, 'latitude should have been approx 61.93, instead read %f' % latitude
    
def test_longitude(classic1):
    '''
    check latitude == -172.270
    '''

    longitude = classic1.longitude()
    assert round(longitude, 2) == -172.270, 'longitude should have been approx -172.270, instead read %f' % longitude

def test_uid(classic1):
    '''
    check profile ID == 67064
    '''

    uid = classic1.uid()
    assert uid == 67064, 'uid should have been 67064, instead read %f' % uid

def test_n_levels(classic1):
    '''
    check the number of levels == 4
    '''

    levels = classic1.n_levels()
    assert levels == 4, 'levels should have been 4, instead read %f' % levels

def test_year(classic1):
    '''
    check year == 1934
    '''

    year = classic1.year()
    assert year == 1934, 'year should have been 1934, instead read %f' % year

def test_month(classic1):
    '''
    check month == 8
    '''

    month = classic1.month() 
    assert month == 8, 'month should have been 8, instead read %f' % month

def test_day(classic1):
    '''
    check day == 7
    '''

    day = classic1.day()
    assert day == 7, 'day should have been 7, instead read %f' % day

def test_time(classic1):
    ''' 
    check time == 10.37
    '''

    time = classic1.time()
    assert round(time,2) == 10.37, 'time should have been 10.37, instead read %f' % time

def test_datetime(classic1):
    '''
    check datetime is close to 1934-8-7 10:22:12
    allow a 36 second (== 0.01 hour) deviation for round off error in the time
    '''

    d = classic1.datetime()
    assert timedelta(seconds=-18) < (d - datetime(1934, 8, 7, 10, 22, 12)) < timedelta(seconds=18), 'time should have been close to 1934-08-07 10:22:12, instead read %s' % d

def test_probe_type(classic1):
    '''
    check probe type == 7
    '''

    probe = classic1.probe_type() 
    assert probe == 7, 'probe should have been 7, instead read %f' % probe

def test_depth(classic1):
    '''
    check depths == [0.0, 10.0, 25.0, 50.0]
    '''

    truth = [0.0, 10.0, 25.0, 50.0]
    truth = [numpy.float32(t) for t in truth]
    z = classic1.z()
    assert numpy.array_equal(z, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % z.__str__()

def test_temperature(classic1):
    '''
    check temperatures == [8.960, 8.950, 0.900, -1.230]
    '''

    truth = [8.960, 8.950, 0.900, -1.230]
    truth = [numpy.float32(t) for t in truth]
    t = classic1.t()
    assert numpy.array_equal(t, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % t.__str__()

def test_temperature_WODflags(classic1):
    '''
    check WOD flags are not returned = [--, --, --, --]
    '''

    qc = classic1.t_level_qc('WOD')
    assert numpy.alltrue(qc.mask) , \
        'temperature_WODflags should not be in file, instead read %s' % qc.__str__()


def test_temperature_IQUODflags(classic1):
    '''
    check IQUOD flags are returned = [0, 0, 0, 0]
    '''

    errors = []
    truth = [0, 0, 0, 0]
    qc = classic1.t_level_qc('IQUOD')
    # replace assertions by conditions
    if numpy.alltrue(qc.mask):
        errors.append("Temperature_IQUODflags not found in file")
    if not numpy.array_equal(qc, truth):
        errors.append('Temperature_IQUODflags should have been [0, 0, 0, 0], instead read %s' % qc.__str__())

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_salinity(classic1):
    '''
    check salinities == [30.900, 30.900, 31.910, 32.410]
    '''
    
    truth = [30.900, 30.900, 31.910, 32.410]
    truth = [numpy.float32(t) for t in truth]
    s = classic1.s()
    assert numpy.array_equal(s, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % s.__str__()

def test_oxygen(classic1):
    truth = [293.90298, 291.90366, 375.3761,  317.39523]
    truth = [numpy.float32(t) for t in truth]
    s = classic1.oxygen()
    assert numpy.array_equal(s, truth), 'dissolved oxygen should have been [293.90298, 291.90366, 375.3761,  317.39523], instead read %s' % s.__str__()

def test_phosphate(classic1):
    truth = [0.63, 0.69, 0.88, 1.14]
    truth = [numpy.float32(t) for t in truth]
    s = classic1.phosphate()
    assert numpy.array_equal(s, truth), 'phosphate should have been [0.63, 0.69, 0.88, 1.14], instead read %s' % s.__str__()

def test_silicate(classic1):
    truth = [20, 12, 15, 25]
    truth = [numpy.float32(t) for t in truth]
    s = classic1.silicate()
    assert numpy.array_equal(s, truth), 'silicate should have been [20, 12, 15, 25], instead read %s' % s.__str__()

def test_pH(classic1):
    truth = [8.100, 8.100, 8.100, 8.050]
    truth = [numpy.float32(t) for t in truth]
    s = classic1.pH()
    assert numpy.array_equal(s, truth), 'pH should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % s.__str__()




