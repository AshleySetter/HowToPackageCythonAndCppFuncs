from setuptools import setup
from setuptools.extension import Extension
import numpy

extensions = [
    Extension(
    name="cythonSumPackage.SumArray", # name/path of generated .so file
    sources=["cythonSumPackage/SumArrayCython/SumArray.c"], # cython generated c file
    include_dirs = [numpy.get_include()]), # gives access to numpy funcs inside cython code 
    Extension(
    name="cythonSumPackage.SumArrayCythonCpp", # name/path of generated .so file
    sources=["cythonSumPackage/SumArrayC/SumArrayCythonCpp.cpp"], # cython generated cpp file
    include_dirs = [numpy.get_include()], # gives access to numpy funcs inside cython code 
    language="c++",), # tells python that the language of the extension is c++
]

setup(name='cythonSumPackage',
      version='1.0',
      description='...',
      author='Ashley Setter',
      author_email='A.Setter@soton.ac.uk',
      include_package_data=True,
      packages=['cythonSumPackage',
                'cythonSumPackage.UseSumArrayCython',
      ],
      ext_modules = extensions,
)
