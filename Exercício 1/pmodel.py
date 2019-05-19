# -*- coding: utf-8 -*-
"""
Matemática Computacional I
Lista de Exercícios (2/10)

Exercício Extra - Converter o arquivo pmodel.m para python.

pmodel.m
   http://www2.meteo.uni-bonn.de/staff/venema/themes/surrogates/pmodel/pmodel.m
   
Dicas de funções equivalentes entre Matlab e NumPy
    Numpy for Matlab users
    https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html   

----------------------------------------
Version by Willian Vieira de Oliveira 
24/04/19
Python: 3.7.3
----------------------------------------
"""

# Python Standard Library
import numpy as np
import math

def pmodel(noValues = 256, p = 0.375, slope = np.array([])): #default arguments, in case they are not defined
    # Calculate length of time series
    noOrders = math.ceil(math.log2(noValues))
    noValuesGenerated = np.power(2, noOrders)
    
    # y is the time series generated with the p-model.
    y = 1
    
    for n in range(0, noOrders):
        y = next_step_1d(y, p)
        
    # If a slope if specified also a fractionally integrated time series (x) is
    # calculated from y.    
    if (slope): # if not empty
        fourierCoeff = fractal_spectrum_1d(noValues, slope/2) # Calculate the magnitudes of the coefficients of the Fourier spectrum. The Fourier slope is half of the slope of the power spectrum.
        meanVal = np.mean(y)
        stdy = np.std(y, ddof=1) # ddof: Delta Degrees of Freedom. ddof=1 is equivalent to the std function in Matlab
        x = np.fft.ifft(y - meanVal, axis = 0) # Calculate the Fourier coefficients of the original p-model time series
        phase = np.angle(x) # Calculate the phases, as these are kept intact, should not be changed by the Fourier filter.
        x = fourierCoeff * np.exp(1j*phase) # Calculate the complex Fourier coefficients with the specified spectral slope, and the phases of the p-model.
        x = np.real( np.fft.fft(x, axis = 0) ) # Generate the fractionally integrated time series.
        x = x * stdy / np.std(x, ddof=1)
        x = x + meanVal
    else:
        x = y  
    
    return x


def next_step_1d(y, p):
    np.random.seed(0)
    length = np.size(y)
    
    y2 = np.zeros(length*2)
    sign = np.random.rand(length) - 0.5
    
    sign = sign/np.abs(sign)
    
    y2[0:(2*length)-1:2] = y + sign*(1-2*p)*y
    y2[1:(2*length):2] = y - sign*(1-2*p)*y
    
    return y2


def fractal_spectrum_1d(noValues, slope):
    # if you want to make a large number of time series, please rewrite this
    # part to get rid of the for-loop.
    ori_vector_size = noValues
    ori_half_size = int(ori_vector_size/2)
    
    a = np.zeros( ori_vector_size ) #The magnitudes of the Fourier coefficients
    
    for t2 in range(0, (ori_half_size + 1)): #Remember how range works: [1, 3) = 1, 2
        t4 = ori_vector_size - t2
        
        if (t4 >= ori_vector_size):
            t4 = t2
        if (t2 == 0): # the DC-component of the Fourier spectrum should be zero.
            coeff = 0 
        else:
            coeff = np.power(int(t2), slope)            
            
        a[t2] = coeff
        a[t4] = coeff
    
    return a


#result = pmodel(2**12, 0.52, -1.66)

s8 = pmodel(2**12, 0.52, -1.66)
s9 = pmodel(2**12, 0.62, -0.45)
s10 = pmodel(2**12, 0.72, -0.75)

np.savetxt("s8.csv", s8, delimiter = ",")
np.savetxt("s9.csv", s9, delimiter = ",")
np.savetxt("s10.csv", s10, delimiter = ",")