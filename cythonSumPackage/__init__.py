"""
...
"""

# init file

# import cython created shared object files
import cythonSumPackage.SumArray # pure cython version
import cythonSumPackage.SumArrayCythonCpp # cython with cpp version

# import python sub-modules
import cythonSumPackage.UseSumArrayCython # some code that uses the cython code

# import core functionality
from .core import *
#from . import core
