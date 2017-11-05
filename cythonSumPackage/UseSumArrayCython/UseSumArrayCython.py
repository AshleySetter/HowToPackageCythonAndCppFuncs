from cythonSumPackage.SumArray import C_SumArray
from cythonSumPackage.SumArrayCythonCpp import C_SumArray as Cpp_SumArray
import numpy as np

def do_a_thing(n):
    test_array = np.array(list(range(n))).astype(float)
    sumval = C_SumArray(test_array)
    return sumval


def do_a_thing_with_cpp(n):
    test_array = np.array(list(range(n))).astype(float)
    sumval = Cpp_SumArray(test_array, n)
    return sumval
