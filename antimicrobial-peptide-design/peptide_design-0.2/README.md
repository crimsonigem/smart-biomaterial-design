-------
Information
-------

This module implement the method described in the paper "Machine Learning Assisted Design of Highly Active Peptides for Drug Discovery" published in PLOS Computational Biology in 2015.

In addition, you will most likely need the GS kernel to learn a model.
The GS source code can be downloaded at http://graal.ift.ulaval.ca/downloads/gs-kernel/

-------
How to install
-------

To ease the utilization, we have programmed a pure python implementation and very optimized version in Cython that is much faster than the pure python version.
We thus recommend to use the fast version.

-------

If you have cython installed you can compile the back-end with the following command:
> python setup.py build_ext -b .

To install the latest Cython version using easy_install:
> sudo easy_install cython

or using your package manager:
> sudo apt-get install cython

-------
About Cython
-------

Cython is a language that makes writing C extensions for the Python language as easy as Python itself. It is based on the well-known Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is a superset of the Python language that additionally supports calling C functions and declaring C types on variables and class attributes. This allows the compiler to generate very efficient C code from Cython code. The C code is generated once and then compiles with all major C/C++ compilers in CPython 2.4 and later, including Python 3.x.

http://cython.org/


-------
Usage
-------
peptide_length : int
    The length of the peptide.
    
training_peptides : list, np.array
    The peptides amino acids sequences of the training set.

beta : np.array
    Weight on training examples.
    
amino_acid_property_file : string
    Path to the amino acid property file.

sigma_position: float
    \sigma_p hyper-parameter of the GS kernel.
    
sigma_amino_acid: float
    \sigma_c hyper-parameter of the GS kernel.

substring_length: int
    Substring length hyper-parameter of the GS kernel

-------
Example
-------
from peptide_design import peptide_design

designer = peptide_design(peptide_length, training_peptides, beta, amino_acid_property_file, sigma_position, sigma_amino_acid, substring_length)
best_peptides, affinities = designer.k_longest_path(k)
