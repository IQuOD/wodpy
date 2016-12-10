
from datetime import datetime

from .wod import WodProfile

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
        try:
            self.p = WodProfile(profile)
        except:
            self.p = profile

        self.attributes = {}
        self.attributes['LATITUDE'] = self.p.latitude()
        self.attributes['LONGITUDE'] = self.p.longitude()
        self.attributes['uid'] = self.p.uid()
        try:
            self.attributes['probe_code'] = int(self.p.probe_type())
            self.attributes['probe_type'] = \
                    probe_type_table[self.p.probe_type()]
        except:
            self.attributes['probe_code'] = None
            self.attributes['probe_type'] = None
        self.attributes['n_levels'] = self.p.n_levels()
        self.attributes['datetime'] = self.p.datetime()

        self.data = {}
        # FIXME: pressure is 'almost' equal to depth.
        self.data['PRES'] = self.p.z()
        self.data['DEPTH'] = self.p.z()
        self.data['DEPTH_QC'] = self.p.z_level_qc()
        self.data['TEMP'] = self.p.t()
        self.data['TEMP_QC'] = self.p.t_qc_mask()
        self.data['PSAL'] = self.p.s()
        for v in ['oxygen', 'silicate', 'phosphate', 'pH']:
            try:
                exec("self.data['%s'] = self.p.%s()" % (v, v))
            except:
                pass

    def keys(self):
        return self.data.keys()

    def __getitem__(self, item):
        return self.data[item]
