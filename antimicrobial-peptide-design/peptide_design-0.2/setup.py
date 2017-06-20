#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
---------------------------------------------------------------------
Copyright 2015 Sebastien Giguere

This file is part of peptide_design

peptide_design is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

peptide_design is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with peptide_design.  If not, see <http://www.gnu.org/licenses/>.
---------------------------------------------------------------------
'''

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
