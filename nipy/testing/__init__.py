"""The testing directory contains a small set of imaging files to be used
for doctests only.  More thorough tests and example data will be stored in
a nipy-data-suite to be created later and downloaded separately.

Examples
--------

>>> from nipy.testing import funcfile
>>> from nipy.io.api import load_image
>>> img = load_image(funcfile)
>>> img.shape
(17, 21, 3, 20)

"""

import os

#__all__ = ['funcfile', 'anatfile']

# Discover directory path
filepath = os.path.abspath(__file__)
basedir = os.path.dirname(filepath)

funcfile = os.path.join(basedir, 'functional.nii.gz')
anatfile = os.path.join(basedir, 'anatomical.nii.gz')

from numpy.testing import *
import decorators as dec
from nose.tools import assert_true, assert_false
import data
from data import datapjoin