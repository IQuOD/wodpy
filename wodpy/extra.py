
from datetime import datetime

from wod import WodProfile

probe_type_table = {
        0: 'unkown',
        1: 'MBT',
        2: 'XBT',
        3: 'DBT',
        4: 'CTD',
        5: 'STD',
        6: 'XCTD',
        7: 'bottle/rossete/net',
        8: 'underway/intake',
        9: 'profiling float',
        10: 'moored buoy',
        11: 'drifting buoy',
        12: 'towed CTD',
        13: 'animal mounted',
        14: 'bucket',
        15: 'glider',
        16: 'microBT'
        }


class Wod4CoTeDe(object):
    """ Return a WOD profile in CoTeDe's standards

        CoTeDe is a package to quality control hydrographic data that
          can be used on WOD, but it must access the data in a specific
          structure, as offered here.
    """
    def __init__(self, profile):
        """
            profile can be a WodProfile object or an oppened WOD file.
            For example:
            >>> fid = open('example.dat')
            >>> p = WodProfile(fid)
            >>> profile = Wod4CoTeDe(p)

            or
            >>> fid = open('example.data')
            >>> profile = Wod4CoTeDe(fid)

        """
        if type(profile) == WodProfile:
            self.p = profile
        else:
            self.p = WodProfile(profile)

        self.attributes = {}
        self.attributes['LATITUDE'] = self.p.latitude()
        self.attributes['LONGITUDE'] = self.p.longitude()
        self.attributes['uid'] = self.p.uid()
        self.attributes['probe_code'] = int(self.p.probe_type())
        self.attributes['probe_type'] = probe_type_table[self.p.probe_type()]
        self.attributes['n_levels'] = self.p.n_levels()

        self.get_datetime()

        self.data = {}
        # FIXME: pressure is 'almost' equal to depth.
        self.data['PRES'] = self.p.z()
        self.data['DEPTH'] = self.p.z()
        self.data['DEPTH_QC'] = self.p.z_level_qc()
        self.data['TEMP'] = self.p.t()
        self.data['TEMP_QC'] = self.p.t_qc_mask()
        self.data['PSAL'] = self.p.s()
        self.data['oxygen'] = self.p.oxygen()
        self.data['silicate'] = self.p.silicate()
        self.data['phosphate'] = self.p.phosphate()
        self.data['pH'] = self.p.pH()

    def keys(self):
        return self.data.keys()

    def __getitem__(self, item):
        return self.data[item]

    def get_datetime(self):
        """ Extract datetime from the WOD profile

            This was copied from AutoQC.DummyCNV()
        """
        year  = self.p.year()
        month = self.p.month()
        day   = self.p.day()
        if day == 0: day = 15
        time  = self.p.time()
        if time is None or time < 0 or time >= 24:
            hours   = 0
            minutes = 0
            seconds = 0
        else:
            hours = int(time)
            minutesf = (time - hours) * 60
            minutes  = int(minutesf)
            seconds  = int((minutesf - minutes) * 60)

        self.attributes['datetime'] = datetime(year, month,
                day, hours, minutes, seconds)
