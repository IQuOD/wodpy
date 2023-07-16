import logging, os
from datetime import datetime

module_logger = logging.getLogger("wodpy.extra")
try:
    from loky import get_reusable_executor
    LOKY_AVAILABLE = True
    module_logger.debug("Will use package loky to process in parallel.")
except:
    LOKY_AVAILABLE = False
    module_logger.info("Missing package loky. Falling back to threading.")

from .wod import WodProfile
from .wodnc import Ragged, ncProfile

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
    def __init__(self, profile, raggedIndex=None):
        """
            profile can be a WodProfile object or an open WOD ascii file, or a wodnc.Ragged object with raggedIndex indicating the nth profile to read from the netcdf.
            For example:
            >>> fid = open('example.dat')
            >>> p = WodProfile(fid)
            >>> profile = Wod4CoTeDe(p)

            or
            >>> fid = open('example.data')
            >>> profile = Wod4CoTeDe(fid)

            or
            >>> r = Ragged('example.nc')
            >>> profile = Wod4CoTeDe(r, 0)

        """
        if isinstance(raggedIndex, int) and isinstance(profile, Ragged):
            self.p = ncProfile(profile, raggedIndex)
        elif isinstance(profile, WodProfile):
            self.p = profile
        else:
            try: 
                self.p = WodProfile(profile)
            except:
                raise ValueError('Wod4CoTeDe requires a wod.WodProfile object, an open wod-ascii text file, or a wodnc.Ragged and ragged index.')

        self.attrs = {}
        self.attrs['LATITUDE'] = self.p.latitude()
        self.attrs['LONGITUDE'] = self.p.longitude()
        self.attrs['uid'] = self.p.uid()
        try:
            self.attrs['probe_code'] = int(self.p.probe_type())
            self.attrs['probe_type'] = \
                    probe_type_table[self.p.probe_type()]
        except:
            self.attrs['probe_code'] = None
            self.attrs['probe_type'] = None
        self.attrs['n_levels'] = self.p.n_levels()
        self.attrs['datetime'] = self.p.datetime()

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

    @property
    def attributes(self):
        """CoTeDe now uses .attrs instead of .attributes

           This is a temporary solution during transition. In the near
           future attributes will be dropped.
        """
        return self.attrs

    def keys(self):
        return self.data.keys()

    def __getitem__(self, item):
        return self.data[item]


class WODFile():
    """A WOD file object

    For now, let's assume it will be a plain ASCII type. Later we expand
    for other possibilities
    """
    def __init__(self, filename: str):
        self.fid = open(filename, mode="r")
        self.file_size = os.fstat(self.fid.fileno()).st_size




class ConcurrentMapping():
    def pmap(self, func, args=None, npes: int=4, timeout:int=2):
        """Parallel mapping"""
        executor = get_reusable_executor(max_workers=npes, timeout=timeout)
        results = executor.map(func, self)
        yield from results


class WODGenerator(ConcurrentMapping, WODFile):
    def __init__(self, filename: str):
        super().__init__(filename)

    def __iter__(self):
          return self

    def __next__(self):
        if self.fid.tell() >= self.file_size:
            raise StopIteration
        return WodProfile(self.fid)

    def map(self, func, args=None):
        """(Serial) mapping"""
        for p in self:
            yield func(p)
