
from wod import WodProfile


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
        if type(profile) == wod.WodProfile:
            self.profile = profile
        else:
            self.profile = WodProfile(profile)

        self.attributes = {}
        self.attributes['datetime'] = datetime(self.profile.year(),
                self.profile.month(), self.profile.day())
        self.attributes['LATITUDE'] = self.profile.latitude()
        self.attributes['LONGITUDE'] = self.profile.longitude()
        self.attributes['uid'] = self.profile.uid()

        self.data = {}
        # FIXME: pressure is 'almost' equal to depth.
        self.data['PRES'] = self.profile.z()
        self.data['DEPTH_QC'] = self.profile.z_level_qc()
        self.data['TEMP'] = self.profile.t()
        self.data['TEMP_QC'] = self.profile.t_qc_mask()
        self.data['PSAL'] = self.profile.s()
        
    def keys(self):
        return self.data.keys()

    def __getitem__(self, item):
        return self.data[item]    
