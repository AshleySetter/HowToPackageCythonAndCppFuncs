from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext as build_pyx
import numpy 


ext = [Extension('SumArrayCythonCpp',
                 ['SumArrayCythonCpp.pyx'],
                 include_dirs=[numpy.get_include()],
                 extra_compile_args=['-O3'],
                 extra_link_args=['-O3'],
                 language="c++")]

setup(name = 'SumArrayCythonCpp', ext_modules=ext, cmdclass = { 'build_ext': build_pyx })

