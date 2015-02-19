# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:54:42 2015

@author: ajaver
"""
import numpy as np
cimport numpy as np
cimport cython
from libc.math cimport abs

ctypedef np.float64_t DTYPE_t

cdef inline int imAbsDiff(unsigned char a, unsigned char b): 
    return a-b if a>b else b-a 
@cython.boundscheck(False)

def image_difference(np.ndarray[np.uint8_t, ndim=2] f, np.ndarray[np.uint8_t, ndim=2] g):
    #f, g are to one dim vector
    
    cdef int n_row = f.shape[0];
    cdef int n_col = f.shape[1];
    cdef int i, k
    cdef double total;
    
    for i in range(n_row):
        for j in range(n_col):
            total += <double>imAbsDiff(f[i,j],g[i,j])
        
            
    return total/<double>(f.size)
    