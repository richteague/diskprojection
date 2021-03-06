# diskprojection

<p align='center'>
  <img src="HD163296_zeroth.png" width="793" height="549">
</p>

## What is it?

Functions to measure the height of optically thick emission, or photosphere, using the method presented in [Pinte et al. (2018)](https://ui.adsabs.harvard.edu/abs/2018A%26A...609A..47P/abstract), then use this information to reproject images into arbitrary angles. Very much a work in progress.

## How do I install it?

Currently the only way to install this is by cloning the repository then installing a local version.

```
$ git clone https://github.com/richteague/diskprojection.git
$ cd diskprojection
$ pip install .
```

This has a couple of dependencies, namely [astropy](https://github.com/astropy/astropy) and [GoFish](https://github.com/richteague/gofish), which should be installed automatically if you don't have them.

## How do I use it?

```python
# import the package
from diskprojection import disk_observation

# load up the observations
disk = disk_observation('path/to/imagecube.fits')

# grab the emission surface
r, z, Fnu, v = disk.get_emission_surface(inc=30.0, PA=35.0)

# make some cuts to get rid of poor points
r, z, Fnu, v = disk.clip_emission_surface(r, z, Fnu, v, min_Fnu=0.05)

# apply an iterative sigma clipping to remove noise
r, z, Fnu, v = disk.iterative_clip_emission_surface(r, z, Fnu, v)
```

A more comprehensive document will be coming soon.

#### Notes

Part of the code uses `detect_peaks.py` from [Marcos Duarte](https://github.com/demotu/BMC).
