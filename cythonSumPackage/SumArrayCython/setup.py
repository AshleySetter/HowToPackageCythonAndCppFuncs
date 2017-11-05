from distutils.core import setup
from distutils.extension import Extension
#from Cython.Build import cythonize
from Cython.Distutils import build_ext as build_pyx
import numpy

ext = [Extension('SumArray',
                sources=["SumArray.pyx"],
                include_dirs = [numpy.get_include()])]

#setup(name="SumArray", ext_modules = cythonize([ext]))

setup(name = 'SumArray', ext_modules=ext, cmdclass = { 'build_ext': build_pyx })
