#include <iostream>

double SumArray_Cpp(double* Array, int length){
  double Sum = 0.0;

  for(int i=0; i<length; i++){
    Sum+= Array[i];
  }
  return Sum;
}
