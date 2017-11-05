import cython

import numpy as np
cimport numpy as np

cdef extern from "SumArrayC.cpp":
    double SumArray_Cpp(double* Array, int length)

@cython.boundscheck(False)
@cython.wraparound(False)
def C_SumArray(np.ndarray[double, mode="c"] InputArray not None, int length):
    return SumArray_Cpp(&InputArray[0], length)
