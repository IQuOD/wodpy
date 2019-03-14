'''Defines a function that writes a single WOD profile to a file object.'''

def flt_to_string(value, precision=2):
    if value is None: return '-'
    for nbefore in range(100):
        if abs(value) < 10**nbefore: break
    sigdigits = nbefore + precision
    if sigdigits == 0: sigdigits = 1
    totdigits = sigdigits
    if value < 0: totdigits += 1
    asstring = (str(sigdigits) + str(totdigits) + str(precision) + '%' + str(totdigits) + 'i') % round(value * 10**precision) 
    return asstring

def ilen(integer): return len(str(integer))

def write_wodascii(fid,
                   uid      = 0,
                   country  = '99',
                   cruise   = 0,
                   year     = 9999,
                   month    = 99,
                   day      = 99,
                   time     = None,
                   lat      = None,
                   lon      = None,
                   probetype= 0,
                   z        = [],
                   t        = [],
                   qc       = [],
                   proftype = 0):
      
    # Our profile string will be held in variable p.             
    p = ''

    #### Primary header ####

    # Unique cast number.
    nb = ilen(uid)
    assert nb > 0 and nb < 10, 'UID must be a 1 - 9 character integer'
    p += str(nb) + str(uid)

    # Country code.
    nb = len(country)
    assert nb == 2, 'Country code must be 2 characters'
    p += country

    # Cruise number.
    nb = ilen(cruise)
    assert nb > 0 and nb < 10, 'Cruise number must be 1 - 9 characters'
    p += str(nb) + str(cruise)

    # Year.
    assert year > 1800 and year < 10000, 'Year not sensible'
    p += '%04i' % year

    # Month.
    message = 'Month must be in the range 1 - 12 but was ' + str(month)
    #assert month > 0 and month < 13, message
    p += '%02i' % month

    # Day.
    #assert day > 0 and day < 32, 'Day must be in the range 1 - 31'
    p += '%02i' % day

    # Time.
    p += flt_to_string(time)

    # Latitude and longitude.
    p += flt_to_string(lat, 3)
    p += flt_to_string(lon, 3)

    # Number of levels.
    nlevels = len(t)
    nb = ilen(nlevels)
    p += str(nb) + str(nlevels)

    # Profile type.
    p += str(proftype)

    # Number of variables - hardcoded to one (t) for now.
    nvars = 1    
    p += '%02i' % nvars

    # Variable data.
    variables = ['t']
    for ivar in range(nvars):
        # Variable code.
        if variables[ivar] == 't':
            varcode = 1
        nb = ilen(varcode)
        p += str(nb) + str(varcode)
        # QC flag.
        qcflag = 0
        p += str(qcflag)
        # Metadata.
        nmeta = 1
        nb = ilen(nmeta)
        p += str(nb) + str(nmeta)
        # -- Probe type - currently set to the same as second header 29.
        p += '15' + flt_to_string(probetype, 0)

    #### Character data ####
    p += '0'

    #### Secondary header ####
    s = '12' # One byte saying 2 second headers.
    # Probe type.
    s += '229' + flt_to_string(probetype, 0)
    s += '296' + flt_to_string(3, 0)

    # Add size of second headers to beginning.
    v0 = '0'
    v1 = '00'
    while v0 != v1:
        v0 = str(ilen(ilen(v1))) + str(ilen(v1)) + s
        v1 = str(ilen(ilen(v0))) + str(ilen(v0)) + s
    s = v1

    # Join to the profile. 
    p += s

    #### Biological header ####
    p += '0'

    #### Profile data ####
    for i in range(nlevels):
        p += flt_to_string(z[i], precision=3) # Value
        p += '0'                 # WOD flag
        p += '1'                 # Originator flag
        p += flt_to_string(t[i], precision=3) # Value
        p += '0'                 # WOD flag
        p += qc[i]               # Originator flag

    #### Write to file ####

    # Write to file - need to include the length of the profile, which
    # then affects the length, so this is a bit awkward.
    v0 = '0'
    v1 = '00'
    while v0 != v1:
        v0 = 'C' + str(ilen(ilen(v1))) + str(ilen(v1)) + p
        v1 = 'C' + str(ilen(ilen(v0))) + str(ilen(v0)) + p
    p = v1 
    for i in range(0, len(p), 80):
        section = p[i:i+80]
        sectionlen = len(section)
        for j in range(80-sectionlen):
            section += ' '
        section += '\n'
        fid.write(section)

    return

import glob
import gsw
from netCDF4 import Dataset
from netCDF4 import num2date

# Example writing delayed mode Argo data to wod ascii files.
for iregion, region in enumerate(['atl', 'pac', 'ind']):
    fid   = open(region + '.wodascii', 'w')
    profnum = 0
    files = sorted(glob.glob(region + '/*.nc'))
    for fn in files:
        nc = Dataset(fn)
        datatype = nc.variables['DATA_MODE'][:]
        platform = nc.variables['PLATFORM_NUMBER'][:]
        juld     = nc.variables['JULD'][:]
        juldunit = nc.variables['JULD'].units
        juldqc   = nc.variables['JULD_QC'][:]
        lats     = nc.variables['LATITUDE'][:]
        lons     = nc.variables['LONGITUDE'][:]
        posqc    = nc.variables['POSITION_QC'][:]
        pres     = nc.variables['PRES'][:]
        presqc   = nc.variables['PRES_ADJUSTED_QC'][:]
        temp     = nc.variables['TEMP'][:]
        tempqc   = nc.variables['TEMP_ADJUSTED_QC'][:]
        fv       = nc.variables['TEMP']._FillValue
        nc.close()

        for iprof in range(len(juld)):
            if datatype[iprof] != 'D': continue
            profnum += 1
            uid    = (iregion + 1) * 10**8 + profnum
            cruise = int(''.join(platform[iprof][0:7]))
            dt     = num2date(juld[iprof], juldunit)
            lat    = lats[iprof]
            lon    = lons[iprof]
            year   = dt.year
            month  = dt.month
            day    = dt.day
            time   = dt.hour + dt.minute / 60.0 # Can only store to nearest minute unless precision is increased.
            nlevs  = temp.shape[1]
            dlist  = []
            tlist  = []
            qclist = []
            for ilev in range(nlevs):
                if pres.mask[iprof,ilev] or temp.mask[iprof,ilev]: continue
                d = -1.0 * gsw.z_from_p(pres.data[iprof, ilev], lat)
                t = temp.data[iprof, ilev]
                if (juldqc[iprof] == '3' or juldqc[iprof] == '4' or
                    posqc[iprof] == '3' or posqc[iprof] == '4' or
                    presqc[iprof][ilev] == '3' or presqc[iprof][ilev] == '4' or
                    tempqc[iprof][ilev] == '3' or tempqc[iprof][ilev] == '4'):
                   qc = '4'
                   if presqc[iprof][ilev] == '8' or tempqc[iprof][ilev] == '8': print '8 in file ', fn
                   if presqc[iprof][ilev] == '5' or tempqc[iprof][ilev] == '5': print '5 in file ', fn
                else:
                   qc = '1'
                dlist.append(d)
                tlist.append(t)
                qclist.append(qc)
                
            write_wodascii(fid,
                           uid      = uid,
                           country  = '99',
                           cruise   = cruise,
                           year     = year,
                           month    = month,
                           day      = day,
                           time     = time,
                           lat      = lat,
                           lon      = lon,
                           probetype= 9, # Profiling float.
                           z        = dlist,
                           t        = tlist,
                           qc       = qclist)

    fid.close()


