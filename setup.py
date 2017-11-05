from setuptools import setup
from setuptools.extension import Extension
import numpy

extensions = [
    Extension(
    name="cythonSumPackage.SumArray",
    sources=["cythonSumPackage/SumArrayCython/SumArray.c"],
    include_dirs = [numpy.get_include()]),
    Extension(
    name="cythonSumPackage.SumArrayCythonCpp", # name/path of generated .so file
    sources=["cythonSumPackage/SumArrayC/SumArrayCythonCpp.cpp"], # cython generated cpp file
#             "cythonSumPackage/SumArrayC/SumArrayC.cpp"], # source cpp file containing funcs
    include_dirs = [numpy.get_include()],
    language="c++",),
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
