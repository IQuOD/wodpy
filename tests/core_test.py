from datetime import datetime
from wodpy import wod
import numpy, math, pandas, pytest

@pytest.fixture
def classic1():
    # WOD13 format data
    classic = open("tests/testData/classic.dat")    
    # example from pp 124 of http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
    return wod.WodProfile(classic)

@pytest.fixture
def classic2():
    # WOD13 format data
    classic = open("tests/testData/classic.dat")    
    c = wod.WodProfile(classic) # iterate past the first object in the file
    # example with missing salinity information
    return wod.WodProfile(classic)

@pytest.fixture
def iquod1():
    # IQuOD 0.1 format data
    # short example (unpacked by hand to validate)
    iquod = open("tests/testData/iquod.dat")
    return wod.WodProfile(iquod)

@pytest.fixture
def iquod2():
    # IQuOD 0.1 format data
    iquod = open("tests/testData/iquod.dat")    
    c = wod.WodProfile(iquod) # iterate past the first object in the file
    # example with metadata
    return wod.WodProfile(iquod)

@pytest.fixture
def path1():
    # data with some interesting pathologies
    path = open("tests/testData/pathological.dat")
    return wod.WodProfile(path)

# ===================================================================
# check the example from pp 124 of
# http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf
# is extracted correctly by base functions.
# data is in `data/classic.dat`

def test_latitude(classic1):
    '''
    check latitude == 61.930
    '''

    latitude = classic1.latitude()
    df_latitude = classic1.df().attrs['latitude']
    np_latitude = classic1.npdict()['latitude']
    header_latitude = classic1.header().latitude
    assert latitude == 61.930, 'latitude should have been 61.930, instead read %f' % latitude
    assert df_latitude == 61.930, 'dataframe latitude should have been 61.930, instead read %f' % df_latitude
    assert np_latitude == 61.930, 'np dict latitude should have been 61.930, instead read %f' % np_latitude
    assert header_latitude == 61.931, 'header latitude should have been 61.930, instead read %f' % header_latitude

def test_latitude_error(classic1):
    '''
    check latitude error is None
    '''

    latitude_unc = classic1.latitude_unc()
    df_latitude_unc = classic1.df().attrs['latitude_unc']
    np_latitude_unc = classic1.npdict()['latitude_unc']
    header_latitude_unc = classic1.header().latitude_unc
    assert latitude_unc is None, 'latitude error is undefined for this profile, instead read %f' % latitude_unc
    assert df_latitude_unc is None, 'dataframe latitude error is undefined for this profile, instead read %f' % df_latitude_unc
    assert np_latitude_unc is None, 'npdict latitude error is undefined for this profile, instead read %f' % np_latitude_unc
    assert math.isnan(header_latitude_unc) , 'header latitude error is undefined for this profile, instead read %f' % header_latitude_unc

def test_longitude(classic1):
    '''
    check longitude == -172.270
    '''

    longitude = classic1.longitude()
    df_longitude = classic1.df().attrs['longitude']
    np_longitude = classic1.npdict()['longitude']
    header_longitude = classic1.header().longitude
    assert longitude == -172.270, 'longitude should have been -172.270, instead read %f' % longitude
    assert df_longitude == -172.270, 'dataframe longitude should have been -172.270, instead read %f' % df_longitude
    assert np_longitude == -172.270, 'np dict longitude should have been -172.270, instead read %f' % np_longitude
    assert header_longitude == -172.270, 'header longitude should have been -172.270, instead read %f' % header_longitude

def test_longitude_error(classic1):
    '''
    check longitude error is None
    '''

    longitude_unc = classic1.longitude_unc()
    df_longitude_unc = classic1.df().attrs['longitude_unc']
    np_longitude_unc = classic1.npdict()['longitude_unc']
    header_longitude_unc = classic1.header().longitude_unc
    assert longitude_unc is None, 'longitude error is undefined for this profile, instead read %f' % longitude_unc
    assert df_longitude_unc is None, 'dataframe longitude error is undefined for this profile, instead read %f' % df_longitude_unc
    assert np_longitude_unc is None, 'np dict longitude error is undefined for this profile, instead read %f' % np_longitude_unc
    assert math.isnan(header_longitude_unc), 'header longitude error is undefined for this profile, instead read %f' % header_longitude_unc

def test_uid(classic1):
    '''
    check profile ID == 67064
    '''

    uid = classic1.uid()
    df_uid = classic1.df().attrs['uid']
    np_uid = classic1.npdict()['uid']
    header_uid = classic1.header().uid
    assert uid == 67064, 'uid should have been 67064, instead read %f' % uid
    assert df_uid == 67064, 'dataframe uid should have been 67064, instead read %f' % df_uid
    assert np_uid == 67064, 'np dict uid should have been 67064, instead read %f' % np_uid
    assert header_uid == 67064, 'header uid should have been 67064, instead read %f' % header_uid

def test_n_levels(classic1):
    '''
    check the number of levels == 4
    '''

    levels = classic1.n_levels()
    df_levels = classic1.df().attrs['n_levels']
    np_levels = classic1.npdict()['n_levels']
    header_n_levels = classic1.header().n_levels
    assert levels == 4, 'levels should have been 4, instead read %f' % levels
    assert df_levels == 4, 'dataframe levels should have been 4, instead read %f' % df_levels
    assert np_levels == 4, 'np dict levels should have been 4, instead read %f' % np_levels
    assert header_n_levels == 4, 'header levels should have been 4, instead read %f' % header_levels

def test_year(classic1):
    '''
    check year == 1934
    '''

    year = classic1.year()
    df_year = classic1.df().attrs['year']
    np_year = classic1.npdict()['year']
    header_year = classic1.header().year
    assert year == 1934, 'year should have been 1934, instead read %f' % year
    assert df_year == 1934, 'dataframe year should have been 1934, instead read %f' % df_year
    assert np_year == 1934, 'np dict year should have been 1934, instead read %f' % np_year
    assert header_year == 1934, 'header year should have been 1934, instead read %f' % header_year

def test_month(classic1):
    '''
    check month == 8
    '''

    month = classic1.month() 
    df_month = classic1.df().attrs['month']
    np_month = classic1.npdict()['month']
    header_month = classic1.header().month
    assert month == 8, 'month should have been 8, instead read %f' % month
    assert df_month == 8, 'dataframe month should have been 8, instead read %f' % df_month
    assert np_month == 8, 'np dict month should have been 8, instead read %f' % np_month
    assert header_month == 8, 'header month should have been 8, instead read %f' % header_month


def test_day(classic1):
    '''
    check day == 7
    '''

    day = classic1.day()
    df_day = classic1.df().attrs['day']
    np_day = classic1.npdict()['day']
    header_day = classic1.header().day
    assert day == 7, 'day should have been 7, instead read %f' % day
    assert df_day == 7, 'dataframe day should have been 7, instead read %f' % df_day
    assert np_day == 7, 'np dict day should have been 7, instead read %f' % np_day
    assert header_day == 7, 'header day should have been 7, instead read %f' % header_day

def test_time(classic1):
    ''' 
    check time == 10.37
    '''

    time = classic1.time()
    df_time = classic1.df().attrs['time']
    np_time = classic1.npdict()['time']
    header_time = classic1.header().time
    assert time == 10.37, 'time should have been 10.37, instead read %f' % time
    assert df_time == 10.37, 'dataframe time should have been 10.37, instead read %f' % df_time
    assert np_time == 10.37, 'np dict time should have been 10.37, instead read %f' % np_time
    assert header_time == 10.37, 'header time should have been 10.37, instead read %f' % header_time


def test_datetime(classic1):
    '''
    check datetime 1934-8-7 10:22:12
    '''

    d = classic1.datetime()
    assert d == datetime(1934, 8, 7, 10, 22, 12), \
            'time should have been 1934-08-07 10:22:12, instead read %s' \
            % d


def test_probe_type(classic1):
    '''
    check probe type == 7
    '''

    probe = classic1.probe_type() 
    df_probe = classic1.df().attrs['probe_type']
    np_probe = classic1.npdict()['probe_type']
    header_probe = classic1.header().probe_type
    assert probe == 7, 'probe should have been 7, instead read %f' % probe
    assert df_probe == 7, 'dataframe probe should have been 7, instead read %f' % df_probe
    assert np_probe == 7, 'np dict probe should have been 7, instead read %f' % np_probe
    assert header_probe == 7, 'header probe should have been 7, instead read %f' % header_probe


def test_depth(classic1):
    '''
    check depths == [0.0, 10.0, 25.0, 50.0]
    '''

    truth = [0.0, 10.0, 25.0, 50.0]
    z = classic1.z()
    df_z = classic1.df()['z']
    np_z = classic1.npdict()['z']
    assert numpy.array_equal(z, truth), 'depths should have been [0, 10, 25, 50], instead read %s' % z.__str__()
    assert numpy.array_equal(df_z, truth), 'dataframe depths should have been [0, 10, 25, 50], instead read %s' % df_z.tolist().__str__()
    assert numpy.array_equal(np_z, truth), 'numpy dict depths should have been [0, 10, 25, 50], instead read %s' % np_z.__str__()

def test_depth_error(classic1):
    '''
    check depth errors == [--,--,--,--] (all masked)
    '''

    truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
    dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
    z_unc = classic1.z_unc()
    df_z_unc = classic1.df()['z_unc']
    np_z_unc = classic1.npdict()['z_unc']
    assert numpy.array_equal(z_unc, truth), 'depth errors should have been all masked, instead read %s' % z_unc.__str__()
    assert df_z_unc.equals(dftruth), 'dataframe depth errors should have been all masked, instead read %s' % df_z_unc.__str__()
    assert numpy.array_equal(np_z_unc, truth), 'numpy dict depth errors should have been all masked, instead read %s' % np_z_unc.__str__()

def test_temperature(classic1):
    '''
    check temperatures == [8.960, 8.950, 0.900, -1.230]
    '''

    truth = [8.960, 8.950, 0.900, -1.230]
    t = classic1.t()
    df_t = classic1.df()['t']
    np_t = classic1.npdict()['t']
    assert numpy.array_equal(t, truth), 'temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % t.__str__()
    assert numpy.array_equal(df_t, truth), 'dataframe temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read \n%s' % df_t.__str__()
    assert numpy.array_equal(np_t, truth), 'numpy dict temperatures should have been [8.96, 8.95, 0.9, -1.23], instead read %s' % np_t.__str__()

def test_temperature_error(classic1):
    '''
    check temperature errors == [--,--,--,--] (all masked)
    '''

    truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
    dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
    t_unc = classic1.t_unc()
    df_t_unc = classic1.df()['t_unc']
    np_t_unc = classic1.npdict()['t_unc']

    assert numpy.array_equal(t_unc, truth), 'temperature errors should have been all masked, instead read %s' % t_unc.__str__()
    assert df_t_unc.equals(dftruth), 'dataframe temperature errors should have been all masked, instead read %s' % df_t_unc.__str__()
    assert numpy.array_equal(np_t_unc, truth), 'numpy dict temperature errors should have been all masked, instead read %s' % np_t_unc.__str__()


def test_salinity(classic1):
    '''
    check salinities == [30.900, 30.900, 31.910, 32.410]
    '''
    
    truth = [30.900, 30.900, 31.910, 32.410]
    s = classic1.s()
    df_s = classic1.df()['s']
    np_s = classic1.npdict()['s']
    assert numpy.array_equal(s, truth), 'salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % s.__str__()
    assert numpy.array_equal(df_s, truth), 'dataframe salinities should have been [30.9, 30.9, 31.91, 32.41], instead read \n%s' % df_s.__str__()
    assert numpy.array_equal(np_s, truth), 'numpy dict salinities should have been [30.9, 30.9, 31.91, 32.41], instead read %s' % np_s.__str__()

def test_salinity_error(classic1):
    '''
    check salinity errors == [--,--,--,--] (all masked)
    '''

    truth = numpy.ma.MaskedArray([0,0,0,0], [True, True, True, True])
    dftruth = pandas.Series(numpy.nan, index=[0,1,2,3])
    s_unc = classic1.s_unc()
    df_s_unc = classic1.df()['s_unc']
    np_s_unc = classic1.npdict()['s_unc']

    assert numpy.array_equal(s_unc, truth), 'salinity errors should have been all masked, instead read %s' % s_unc.__str__()
    assert df_s_unc.equals(dftruth), 'dataframe salinity errors should have been all masked, instead read %s' % df_s_unc.__str__()
    assert numpy.array_equal(np_s_unc, truth), 'numpy dict salinity errors should have been all masked, instead read %s' % np_s_unc.__str__()

def test_oxygen(classic1):
    '''
    check oxygen levels = [6.750, 6.700, 8.620, 7.280]
    '''

    truth = [6.750, 6.700, 8.620, 7.280]
    o2 = classic1.oxygen()
    df_o2 = classic1.df()['oxygen']
    np_o2 = classic1.npdict()['oxygen']

    assert numpy.array_equal(o2, truth), 'oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % o2.__str__()
    assert numpy.array_equal(df_o2, truth), 'dataframe oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read \n%s' % df_o2.__str__()
    assert numpy.array_equal(np_o2, truth), 'numpy dict oxygen levels should have been [6.750, 6.700, 8.620, 7.280], instead read %s' % np_o2.__str__()

def test_phosphate(classic1):
    '''
    check phosphate levels = [0.650, 0.710, 0.900, 1.170]
    '''

    truth = [0.650, 0.710, 0.900, 1.170]
    phos = classic1.phosphate()
    df_phos = classic1.df()['phosphate']
    np_phos = classic1.npdict()['phosphate']

    assert numpy.array_equal(phos, truth), 'phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % phos.__str__()
    assert numpy.array_equal(df_phos, truth), 'dataframe phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read \n%s' % df_phos.__str__()
    assert numpy.array_equal(np_phos, truth), 'numpy dict phosphate levels should have been [0.650, 0.710, 0.900, 1.170], instead read %s' % np_phos.__str__()

def test_silicate(classic1):
    '''
    check silicate levels = [20.500, 12.300, 15.400, 25.600]
    '''

    truth = [20.500, 12.300, 15.400, 25.600]
    sili = classic1.silicate()
    df_sili = classic1.df()['silicate']
    np_sili = classic1.npdict()['silicate']

    assert numpy.array_equal(sili, truth), 'silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % sili.__str__()
    assert numpy.array_equal(df_sili, truth), 'dataframe silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read \n%s' % df_sili.__str__()
    assert numpy.array_equal(np_sili, truth), 'numpy dict silicate levels should have been [20.500, 12.300, 15.400, 25.600], instead read %s' % np_sili.__str__()

def test_pH(classic1):
    '''
    check pH levels = [8.100, 8.100, 8.100, 8.050]
    '''

    truth = [8.100, 8.100, 8.100, 8.050]
    pH = classic1.pH()
    df_pH = classic1.df()['pH']
    np_pH = classic1.npdict()['pH']

    assert numpy.array_equal(pH, truth), 'pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % pH.__str__()
    assert numpy.array_equal(df_pH, truth), 'dataframe pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read \n%s' % df_pH.__str__()
    assert numpy.array_equal(np_pH, truth), 'numpy dict pH levels should have been [8.100, 8.100, 8.100, 8.050], instead read %s' % np_pH.__str__()

def test_PI(classic1):
    '''
    check for PI code
    '''

    truth = [{'Variable code': 0, 'P.I. code': 215}, {'Variable code': 0, 'P.I. code': 216}, {'Variable code': -5006, 'P.I. code': 217}, {'Variable code': -5002, 'P.I. code': 218}]
    PIs = classic1.PIs()
    df_PIs = classic1.df().attrs['PIs']
    np_PIs = classic1.npdict()['PIs']
    assert numpy.array_equal(PIs, truth), 'PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read %s' % PIs.__str__()
    assert numpy.array_equal(df_PIs, truth), 'dataframe PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read \n%s' % PIs.__str__()
    assert numpy.array_equal(np_PIs, truth), 'numpy dict PIs should have been [{"Variable code": 0, "P.I. code": 215}, {"Variable code": 0, "P.I. code": 216}, {"Variable code": -5006, "P.I. code": 217}, {"Variable code": -5002, "P.I. code": 218}], instead read %s' % PIs.__str__()

def test_originator_cruise(classic1):

    truth = 'STOCS85A'
    originator_cruise = classic1.originator_cruise()
    df_originator_cruise = classic1.df().attrs['originator_cruise']
    np_originator_cruise = classic1.npdict()['originator_cruise']
    assert originator_cruise == truth, 'Originator cruise should have been STOCS85A, instead read %s' % originator_cruise
    assert df_originator_cruise == truth, 'dataframe riginator cruise should have been STOCS85A, instead read %s' % df_originator_cruise
    assert np_originator_cruise == truth, 'numpy dict originator cruise should have been STOCS85A, instead read %s' % np_originator_cruise

def test_originator_station(classic1):

    truth = None
    originator_station = classic1.originator_station()
    df_originator_station = classic1.df().attrs['originator_station']
    np_originator_station = classic1.npdict()['originator_station']
    assert originator_station == truth
    assert df_originator_station == truth
    assert np_originator_station == truth

# ===================================================================
# spot check another pre-iquod profile with many missing values
# data: data/classic.dat

def test_missing_vars(classic2):
    '''
    check that error value extraction does not fail when measured value is missing
    note if a variable value is missing, wodpy assumes the error on the value will also be missing
    '''

    truth = numpy.ma.MaskedArray([0]*24, [True]*24)
    s_unc = classic2.s_unc()
    assert numpy.array_equal(s_unc, truth), 'expected salinity errors to all be missing, but got %s instead' % s_unc.__str__()

# ===================================================================
# check that an IQuOD v 0.1 profile is unpacked correctly
# data is in `data/iquod.dat`

def test_iquod_latitude(iquod1):
    '''
    check latitude == 34.5883
    '''

    latitude = iquod1.latitude()
    df_latitude = iquod1.df().attrs['latitude']
    np_latitude = iquod1.npdict()['latitude']
    header_latitude = iquod1.header().latitude
    assert latitude == 34.5883, 'latitude should have been 34.5883, instead read %f' % latitude
    assert df_latitude == 34.5883, 'dataframe latitude should have been 34.5883, instead read %f' % df_latitude
    assert np_latitude == 34.5883, 'np dict latitude should have been 34.5883, instead read %f' % np_latitude
    assert header_latitude == 34.5883, 'header latitude should have been 34.5883, instead read %f' % header_latitude  

def test_iquod_latitude_error(iquod1):
    '''
    check latitude error is None
    '''

    latitude_unc = iquod1.latitude_unc()
    df_latitude_unc = iquod1.df().attrs['latitude_unc']
    np_latitude_unc = iquod1.npdict()['latitude_unc']
    header_latitude_unc = iquod1.header().latitude_unc
    assert latitude_unc is None, 'latitude error is undefined for this profile, instead read %f' % latitude_unc
    assert df_latitude_unc is None, 'dataframe latitude error is undefined for this profile, instead read %f' % df_latitude_unc
    assert np_latitude_unc is None, 'npdict latitude error is undefined for this profile, instead read %f' % np_latitude_unc
    assert math.isnan(header_latitude_unc) , 'header latitude error is undefined for this profile, instead read %f' % header_latitude_unc

def test_iquod_longitude(iquod1):
    '''
    check longitude == 134.2433
    '''

    longitude = iquod1.longitude()
    df_longitude = iquod1.df().attrs['longitude']
    np_longitude = iquod1.npdict()['longitude']
    header_longitude = iquod1.header().longitude
    assert longitude == 134.2433, 'longitude should have been 134.2433, instead read %f' % longitude
    assert df_longitude == 134.2433, 'dataframe longitude should have been 134.2433, instead read %f' % df_longitude
    assert np_longitude == 134.2433, 'np dict longitude should have been 134.2433, instead read %f' % np_longitude
    assert header_longitude == 134.2433, 'header longitude should have been 134.2433, instead read %f' % header_longitude

def test_iquod_longitude_error(iquod1):
    '''
    check longitude error is None
    '''

    longitude_unc = iquod1.longitude_unc()
    df_longitude_unc = iquod1.df().attrs['longitude_unc']
    np_longitude_unc = iquod1.npdict()['longitude_unc']
    header_longitude_unc = iquod1.header().longitude_unc
    assert longitude_unc is None, 'longitude error is undefined for this profile, instead read %f' % longitude_unc
    assert df_longitude_unc is None, 'dataframe longitude error is undefined for this profile, instead read %f' % df_longitude_unc
    assert np_longitude_unc is None, 'npdict longitude error is undefined for this profile, instead read %f' % np_longitude_unc
    assert math.isnan(header_longitude_unc) , 'header longitude error is undefined for this profile, instead read %f' % header_longitude_unc


def test_iquod_uid(iquod1):
    '''
    check cruise ID == 13393621
    '''

    uid = iquod1.uid()
    df_uid = iquod1.df().attrs['uid']
    np_uid = iquod1.npdict()['uid']
    header_uid = iquod1.header().uid
    assert uid == 13393621, 'uid should have been 13393621, instead read %f' % uid
    assert df_uid == 13393621, 'dataframe uid should have been 13393621, instead read %f' % df_uid
    assert np_uid == 13393621, 'np dict uid should have been 13393621, instead read %f' % np_uid
    assert header_uid == 13393621, 'header uid should have been 13393621, instead read %f' % header_uid

def test_iquod_n_levels(iquod1):
    '''
    check the number of levels == 5
    '''

    levels = iquod1.n_levels()
    df_levels = iquod1.df().attrs['n_levels']
    np_levels = iquod1.npdict()['n_levels']
    header_n_levels = iquod1.header().n_levels
    assert levels == 5, 'levels should have been 5, instead read %f' % levels
    assert df_levels == 5, 'dataframe levels should have been 5, instead read %f' % df_levels
    assert np_levels == 5, 'np dict levels should have been 5, instead read %f' % np_levels
    assert header_n_levels == 5, 'header levels should have been 5, instead read %f' % header_levels

def test_iquod_year(iquod1):
    '''
    check year == 2000
    '''

    year = iquod1.year()
    df_year = iquod1.df().attrs['year']
    np_year = iquod1.npdict()['year']
    header_year = iquod1.header().year
    assert year == 2000, 'year should have been 2000, instead read %f' % year
    assert df_year == 2000, 'dataframe year should have been 2000, instead read %f' % df_year
    assert np_year == 2000, 'np dict year should have been 2000, instead read %f' % np_year
    assert header_year == 2000, 'header year should have been 2000, instead read %f' % header_year

def test_iquod_month(iquod1):
    '''
    check month == 1
    '''

    month = iquod1.month() 
    df_month = iquod1.df().attrs['month']
    np_month = iquod1.npdict()['month']
    header_month = iquod1.header().month
    assert month == 1, 'month should have been 1, instead read %f' % month
    assert df_month == 1, 'dataframe month should have been 1, instead read %f' % df_month
    assert np_month == 1, 'np dict month should have been 1, instead read %f' % np_month
    assert header_month == 1, 'header month should have been 1, instead read %f' % header_month

def test_iquod_day(iquod1):
    '''
    check day == 4
    '''

    day = iquod1.day()
    df_day = iquod1.df().attrs['day']
    np_day = iquod1.npdict()['day']
    header_day = iquod1.header().day
    assert day == 4, 'day should have been 4, instead read %f' % day
    assert df_day == 4, 'dataframe day should have been 4, instead read %f' % df_day
    assert np_day == 4, 'np dict day should have been 4, instead read %f' % np_day
    assert header_day == 4, 'header day should have been 4, instead read %f' % header_day

def test_iquod_time(iquod1):
    ''' 
    check time == 3.7
    '''

    time = iquod1.time()
    df_time = iquod1.df().attrs['time']
    np_time = iquod1.npdict()['time']
    header_time = iquod1.header().time
    assert time == 3.7, 'time should have been 3.7, instead read %f' % time
    assert df_time == 3.7, 'dataframe time should have been 3.7, instead read %f' % df_time
    assert np_time == 3.7, 'np dict time should have been 3.7, instead read %f' % np_time
    assert header_time == 3.7, 'header time should have been 3.7, instead read %f' % header_time


def test_iquod_datetime(iquod1):
    '''
    check datetime 2000-1-4 3:42:00
    '''

    d = iquod1.datetime()
    assert d == datetime(2000, 1, 4, 3, 42, 00), \
            'time should have been 2000-01-04 3:42:00, instead read %s' \
            % d


def test_iquod_probe_type(iquod1):
    '''
    check probe type == 4
    '''

    probe = iquod1.probe_type() 
    df_probe = iquod1.df().attrs['probe_type']
    np_probe = iquod1.npdict()['probe_type']
    header_probe = iquod1.header().probe_type
    assert probe == 4, 'probe should have been 4, instead read %f' % probe
    assert df_probe == 4, 'dataframe probe should have been 4, instead read %f' % df_probe
    assert np_probe == 4, 'np dict probe should have been 4, instead read %f' % np_probe
    assert header_probe == 4, 'header probe should have been 4, instead read %f' % header_probe

def test_iquod_depth(iquod1):
    '''
    check depths == [0,2,5,10,20]
    '''

    truth = [0,2,5,10,20]
    z = iquod1.z()
    df_z = iquod1.df()['z']
    np_z = iquod1.npdict()['z']
    assert numpy.array_equal(z, truth), 'depths should have been [0,2,5,10,20], instead read %s' % z.__str__()
    assert numpy.array_equal(df_z, truth), 'dataframe depths should have been [0,2,5,10,20], instead read %s' % df_z.tolist().__str__()
    assert numpy.array_equal(np_z, truth), 'numpy dict depths should have been [0,2,5,10,20], instead read %s' % np_z.__str__()

def test_iquod_depth_error(iquod1):
    '''
    check depth errors == [0,.0016,.004,.008,.016]
    '''

    truth = [0,.0016,.004,.008,.016]
    z_unc = iquod1.z_unc()
    df_z_unc = iquod1.df()['z_unc']
    np_z_unc = iquod1.npdict()['z_unc']
    assert numpy.array_equal(z_unc, truth), 'depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % z_unc.__str__()
    assert numpy.array_equal(df_z_unc, truth), 'dataframe depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % df_z_unc.__str__()
    assert numpy.array_equal(np_z_unc, truth), 'numpy dict depth errors should have been [0,.0016,.004,.008,.016], instead read %s' % np_z_unc.__str__()

def test_iquod_temperature(iquod1):
    '''
    check temperatures == [11.1,11.2,11.0,11.0,11.0]
    '''

    truth = [11.1,11.2,11.0,11.0,11.0]
    t = iquod1.t()
    df_t = iquod1.df()['t']
    np_t = iquod1.npdict()['t']
    assert numpy.array_equal(t, truth), 'temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read %s' % t.__str__()
    assert numpy.array_equal(df_t, truth), 'dataframe temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read \n%s' % df_t.__str__()
    assert numpy.array_equal(np_t, truth), 'numpy dict temperatures should have been [11.1,11.2,11.0,11.0,11.0], instead read %s' % np_t.__str__()

def test_iquod_temperature_error(iquod1):
    '''
    check temperature errors == [.01,.01,.01,.01,.01]
    '''

    truth = [.01,.01,.01,.01,.01]
    t_unc = iquod1.t_unc()
    df_t_unc = iquod1.df()['t_unc']
    np_t_unc = iquod1.npdict()['t_unc']
    assert numpy.array_equal(t_unc, truth), 'temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % t_unc.__str__()
    assert numpy.array_equal(df_t_unc, truth), 'dataframe temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % df_t_unc.__str__()
    assert numpy.array_equal(np_t_unc, truth), 'numpy dict temperature errors should have been [.01,.01,.01,.01,.01], instead read %s' % np_t_unc.__str__()

def test_iquod_salinity(iquod1):
    '''
    check salinities == [31.53,31.47,31.49,31.49,31.50]
    '''
    
    truth = [31.53,31.47,31.49,31.49,31.50]
    s = iquod1.s()
    df_s = iquod1.df()['s']
    np_s = iquod1.npdict()['s']
    assert numpy.array_equal(s, truth), 'salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read %s' % s.__str__()
    assert numpy.array_equal(df_s, truth), 'dataframe salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read \n%s' % df_s.__str__()
    assert numpy.array_equal(np_s, truth), 'numpy dict salinities should have been [31.53,31.47,31.49,31.49,31.50], instead read %s' % np_s.__str__()

def test_iquod_salinity_error(iquod1):
    '''
    check temperature errors == [.02,.02,.02,.02,.02]
    '''

    truth = [.02,.02,.02,.02,.02]
    s_unc = iquod1.s_unc()
    df_s_unc = iquod1.df()['s_unc']
    np_s_unc = iquod1.npdict()['s_unc']
    assert numpy.array_equal(s_unc, truth), 'salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % s_unc.__str__()
    assert numpy.array_equal(df_s_unc, truth), 'dataframe salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % df_s_unc.__str__()
    assert numpy.array_equal(np_s_unc, truth), 'numpy dict salinity errors should have been [.02,.02,.02,.02,.02], instead read %s' % np_s_unc.__str__()

    # metadata tests

def test_metadata(iquod2):
    '''
    check correct unpacking of temperature and salinity metadata from iquod profile
    '''

    truth_t = [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}]
    truth_s = [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}]
    t_meta = iquod2.t_metadata()
    s_meta = iquod2.s_metadata()
    df_t_meta = iquod2.df().attrs['t_metadata']
    df_s_meta = iquod2.df().attrs['s_metadata']
    np_t_meta = iquod2.npdict()['t_metadata']
    np_s_meta = iquod2.npdict()['s_metadata']

    assert numpy.array_equal(truth_t, t_meta), "temperature metadata should have been [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % t_meta.__str__()
    assert numpy.array_equal(truth_s, s_meta), "salinity metadata should have been [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % s_meta.__str__()
    assert numpy.array_equal(truth_t, df_t_meta), "dataframe temperature metadata should have been [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % df_t_meta.__str__()
    assert numpy.array_equal(truth_s, df_s_meta), "dataframe salinity metadata should have been [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % df_s_meta.__str__()
    assert numpy.array_equal(truth_t, np_t_meta), "dict temperature metadata should have been [{'code': 3, 'value': 102.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % np_t_meta.__str__()
    assert numpy.array_equal(truth_s, np_s_meta), "dict salinity metadata should have been [{'code': 3, 'value': 202.0, 'iMeta': 0}, {'code': 5, 'value': 411.0, 'iMeta': 0}], instead read %s" % np_s_meta.__str__()

def test_missing_metadata(classic1, classic2, iquod1):
    '''
    make sure absent metadata doesn't cause problems
    '''

    # pre-iquod format
    t_meta = classic1.t_metadata()
    s_meta = classic1.s_metadata()
    assert numpy.array_equal([], t_meta), 'temperature metadata should have been [], instead read %s' % t_meta.__str__()
    assert numpy.array_equal([], s_meta), 'salinity metadata should have been [], instead read %s' % s_meta.__str__()

    # iquod format
    t_meta = iquod1.t_metadata()
    s_meta = iquod1.s_metadata()
    assert numpy.array_equal([], t_meta), 'iquod temperature metadata should have been [], instead read %s' % t_meta.__str__()
    assert numpy.array_equal([], s_meta), 'iquod salinity metadata should have been [], instead read %s' % s_meta.__str__()

    # pre-iquod format, with metadata (but no intelligent metadata flag)
    truth_t = [{'code': 5, 'value': 4.0, 'iMeta': 0}]
    t_meta = classic2.t_metadata()
    assert numpy.array_equal(truth_t, t_meta), "temperature metadata should have been [{'code': 5, 'value': 4.0, 'iMeta': 0}], instead read %s" % t_meta.__str__()




    























