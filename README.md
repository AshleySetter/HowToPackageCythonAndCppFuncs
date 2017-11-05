# How to Package Cython and Cython-wrapped C++ Code within a python module

This repo contains a simple module with 3 sub-modules. It's purpose is to demonstrate how to package cython and cython-wrapped C++ code into a python module.

The Cython/C++ sub-modules are built/cythonized inside thier sub-directories into a .c (or .cpp) file which is then included as an extension to the module, this builds the shared object file in the build directory. The module init file then imports these shared object files such that the Cython/C++ functions may be called from the module identically to python functions.

The first sub-module is cythonSumPackage.SumArray which contains a pure cython implementation of an array summing function.

The second is cythonSumPackage.SumArrayCythonCpp which contains a cython-wrapped C++ implementation of an array summing function.

The third is a pure python module which uses the 2 above functions in a couple of simple functions which calculate the nth [triangular number](https://en.wikipedia.org/wiki/Triangular_number) by generating a numpy array from 0 to n-1 and summing it using the 2 above functions.

The contenst of this repo is:

```
HowToPackageCythonAndCppFuncs
├── MANIFEST.in                       # says which non .py files to include in build directory - not nessesary
├── cythonSumPackage                  
│   ├── SumArrayC                     # contains c++ source files and cython wrapper file
│   │   ├── SumArrayC.cpp             # c++ source file containing c++ function definition
│   │   ├── SumArrayCythonCpp.cpp     # cython generated c++ file (built when running make in this directory)
│   │   ├── SumArrayCythonCpp.pyx     # cython wrapper file - wraps c++ function in python wrapper
│   │   ├── __init__.py               # blank init file to indicate python module
│   │   ├── makefile                  # simple makefile to run the setup.py file
│   │   └── setup.py                  # setup file which builds the cpp source code and cython wrapper code into a cpp file
│   ├── SumArrayCython               
│   │   ├── SumArray.c                # cython generated c file (built when running make in this directory)
│   │   ├── SumArray.pyx              # cython source file containing python code to by cythonized
│   │   ├── __init__.py               # blank init file to indicate python module
│   │   ├── makefile                  # simple makefile to run the setup.py file
│   │   └── setup.py                  # setup which builds the cython code into a c file
│   ├── UseSumArrayCython            
│   │   ├── UseSumArrayCython.py      # some pure python code which uses the above 2 sub-packages
│   │   └── __init__.py               # init file which imports the contents of UseSumArrayCython.py into cythonSumPackage.UseSumArrayCython submodule
│   ├── __init__.py                   # init file which imports the generated shared object files and the UseSumArrayCython sub-module (and core functionality)
│   └── core.py                       # core functionality of cythonSumPackage - just a hello world function in this simple example
├── install.sh                        # simple script to install the package through pip using the setup.py file
└── setup.py                          # setup file importing the cython generated .c (and .cpp) files from sub-directories and building them as external modules
```

If in setting up your package you get the error message `ImportError: dynamic module does not define module export function (PyInit_<nameofcythoncode>)` it is because the name of your extension in your package setup.py (and therefore your generated .so file) must match the name of your extension given in the cython setup.py file. This is because the cython build generates various functions, including a function `PyInit_<nameofcythoncode>`, which tells python how to initise the C extension and communicate with it. *However* the name given in the package-level setup.py should also contain the path to the generated .SO file. In this package this is <packagename.extensionname>.
	