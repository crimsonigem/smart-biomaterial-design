#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# To Compile the Cython part execute the following command:
# python setup.py build_ext -b .

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("peptide_design_fast",
                             ["peptide_design_fast.pyx"],
                             include_dirs=[np.get_include()])]
)
