[![Build Status](https://travis-ci.org/IQuOD/wodpy.svg?branch=master)](https://travis-ci.org/IQuOD/wodpy)


Release History:

version | DOI
--------|----
1.4.0   | <a href="http://dx.doi.org/10.5281/zenodo.225597"><img src="https://zenodo.org/badge/doi/10.5281/zenodo.225597.svg" alt="10.5281/zenodo.225597"></a>
1.3.0   | <a href="http://dx.doi.org/10.5281/zenodo.47960"><img src="https://zenodo.org/badge/doi/10.5281/zenodo.47960.svg" alt="10.5281/zenodo.47960"></a>
1.2.0   | <a href="http://dx.doi.org/10.5281/zenodo.46785"><img src="https://zenodo.org/badge/doi/10.5281/zenodo.46785.svg" alt="10.5281/zenodo.46785"></a>
1.1.0   | <a href="http://dx.doi.org/10.5281/zenodo.32632"><img src="https://zenodo.org/badge/doi/10.5281/zenodo.32632.svg" alt="10.5281/zenodo.32632"></a>
1.0     | <a href="http://dx.doi.org/10.5281/zenodo.31213"><img src="https://zenodo.org/badge/doi/10.5281/zenodo.31213.svg" alt="10.5281/zenodo.31213"></a>

## Data Unpacking

World Ocean Database data is encoded by the specification described [here](http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf). This `WodProfile` class reads this format, and returns an object with functions to help extract useful information from it.

### How to help

#### Trying things out

Please try unpacking your own WOD data using wodpy, and let us know how it goes in the issues. Any problems (not just bugs, but anything confusing or unintuitive), just let us know. Also, if there are more features you'd like to see (like more parts of the profile unpacked), ask away - community requests are high priority for new features.

#### Contributing

Contributions to wodpy are very welcome! Please follow these simple guidelines:

 - Please start by opening an issue or empty PR in this repo, so we can talk about your plans.
 - No PRs over 500 lines, please. (Why? See figure 1 [here](https://smartbear.com/SmartBear/media/pdfs/11_Best_Practices_for_Peer_Code_Review.pdf).)
 - New code should be packaged in small functions and classes wherever possible; no functions over 50 lines, please.
 - Write at least one test for every new function you create.
 - All tests must pass before any PR will be accepted.

### Usage

#### Install
from pip: `sudo pip install wodpy`

To use the `WodProfile` class, open a text file that conforms to the specification defined in the link above, and pass in the resulting file object:

```
from wodpy import wod

fid = open("example.dat")
profile = wod.WodProfile(fid)
```

`profile` now contains an object with many helper functions for extracting useful information from the first profile in `file`:

```
profile.latitude()  # Return the latitude of the profile.
profile.z()         # Return the depths of the observations.
profile.df()        # Return a pandas DataFrame containing all the information for this profile
```

Further profiles in the file can be read as follows:
```
profile2 = wod.WodProfile(fid) # Read the next profile.
profile2.is_last_profile_in_file(fid) # Is this the last profile?
```

Complete method lists and definitions are as follows.

### `WodProfile` methods

These methods are intended for end-user use, for decoding useful information from a profile.

#### Data Retrieval

These functions decode data from the current profile.

##### numpy

**Per-profile data:**
 - `cruise()`: Returns the cruise number.
 - `day()`: Returns the day.
 - `latitude()`: Returns the latitude of the profile.
 - `longitude()`: Returns the longitude of the profile.
 - `month()`: Returns the month.
 - `n_levels()`: Returns the number of levels in the profile.
 - `primary_header_keys()`: Returns a list of keys in the primary header.
 - `probe_type()`: Returns the contents of secondary header 29 if it exists, otherwise None.
 - `time()`: Returns the time.
 - `uid()`: Returns the unique identifier of the profile.
 - `year()`: Returns the year. 
 - `PIs()`: Returns a list of objects with keys "Variable code" and "P.I. code"
 - `originator_station()`: Returns a string denoting the originator station
 - `originator_cruise()`: Returns a string denoting the originator cruise

**Per-level data:**
 - `oxygen()`: Returns a numpy masked array of oxygen content (mL / L).
 - `p()`: Returns a numpy masked array of pressures (decibar).
 - `pH()`: Returns a numpy masked array of pH levels.
 - `phosphate()`: Returns a numpy masked array of phosphate content (uM / L).
 - `s()`: Returns a numpy masked array of salinity.
 - `s_level_qc(originator=False)`: Returns the quality control flag for each salinity level.
 - `s_profile_qc(originator=False)`: Returns the quality control flag for the salinity profile. 
 - `s_qc_mask()`: Returns a boolean array showing which salinity levels failed quality control. If the entire cast was rejected then all levels are set to True.
 - `silicate()`: Returns a numpy masked array of silicate content (uM / L).
 - `t()`: Returns a numpy masked array of temperatures (C).
 - `t_level_qc(originator=False)`: Returns the quality control flag for each temperature level.
 - `t_profile_qc(originator=False)`: Returns the quality control flag for the temperature profile.
 - `t_qc_mask()`: Returns a boolean array showing which temperature levels failed quality control. If the entire cast was rejected then all levels are set to True.
 - `z()`: Returns a numpy masked array of depths. 
 - `z_level_qc(originator=False)`: Returns a numpy masked array of depth quality control flags. Set the originator option if the originator flags are required.

Constructing the per-level `ndarrays` should not be done more than once per profile; for convenience, we provide the following wrapper to pull all this information out at once:
 - `npdict()`: Returns a `dict` with keys identical to the function names above, and corresponding values equal to the return values of those functions when run with default parameter values.

##### pandas

`profile.df()` returns a pandas `DataFrame`, with per-level information as columns and per-profile information as attributes:

**Columns:**
 - `depth`: level depths in meters
 - `depth_qc`: level depth qc flags (0 == all good)
 - `oxygen`: oxygen content (mL / L)
 - `pressure`: pressure (decibar)
 - `pH`: pH levels
 - `phosphate`: phosphate content (uM / L)
 - `salinity`: level salinities
 - `salinity_qc_flag`: level salinity qc flags (0 == all good)
 - `silicate`: silicate content (uM / L)
 - `temperature`: level temperature in Celcius
 - `temperature_qc_flag`: level temperature qc flags (0 == all good)


**Attributes:**
 - `cruise`: cruise ID number
 - `day`: of the month on [1, 31]
 - `latitude`: in degrees
 - `longitude`: in degrees
 - `month`: of the year on [1, 12]
 - `n_levels`: number of levels in profile (ie number of rows in dataframe)
 - `probe_type`: The contents of secondary header 29 if it exists, otherwise None.
 - `time`: in hours on the range [0, 24)
 - `uid`: unique identifier of profile
 - `year`
 - `PIs`
 - `originator_station`
 - `originator_cruise`

 Note that `DataFrame` attributes generally do not propagate to new `DataFrames` returned by operating on original `DataFrame`s.

**Headers Only**
 - `header()`: Returns a pandas `Series` with only the header information for the profile, keyed as the custom attributes on the full data frame described above.

##### CoTeDe

CoTeDe is a package to quality control hydrographic data, and t

The class `Wod4CoTeDe` provides a WOD profile in the format required by CoTeDe, which is a package to quality control hydrographic data. One could use it like:

>>> from wodpy.extra import Wod4CoTeDe

>>> fid = open('example.dat')
>>> p = WodProfile(fid)
>>> profile = Wod4CoTeDe(p)

or
>>> fid = open('example.data')
>>> profile = Wod4CoTeDe(fid)

To quality control that profile with the EuroGOOS standard:
>>> from cotede.qc import ProfileQC
>>> pqc = ProfileQC(profile, 'eurogoos')

All the information about the profile can be obtained at: pqc.attributes, pqc.data and pqc.flags. For more information, check CoTeDe's manual.



 
 
 
 


 









