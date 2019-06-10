# -*- coding: utf-8 -*-
"""
Matemática Computacional I
Lista de Exercícios (9/10)

9 - Global Wavelet Spectrum
        
    9.1. Utilize o Waipy para obter o GWS (Morlet) de todas as ST do exercício 6.1.
    
--------------------------------------
                            Descrição das funções:

---- waipy.cwt() --------
Continuous wavelet transform from data. Wavelet params can be modified as you wish.

:Parameters:
      |  **Data:** array_like. Raw of data or normalized data.
      |  **pad:** 0 or 1 Pad the time series with zeroes to next pow of two length (recommended).
      |  **dt:** Time-step of the vector. Example: Hourly, daily, monthly, etc...
      |  **dj:** Divide octave in sub-octaves. If dj = 0.25 this will do 4 sub-octaves per octave.
      |  **s0:** The maximum frequency resolution. If it is an annual data, s0 = 2*dt say start at a scale of 6 months.
      |  **j1:** Divide the power-of-teo with dj sub-octaves each.
      |  **lag1:** Lag-1 autocoorelation for red noise background.
      |  **param:** The mother wavelet nondimensional time-parameter, depends on wavelet, for other wavelet than Morlet, see Torrence and Compo 1998.
      |  **mother:** string. The mother wavelet funtion. Can be 'Morlet', 'PAUL', 'DOG'.
      |  **name:** Name of Time Series or your Plot.

    :Returns:
      |  **result:** as dict. Returns all parameters for plot 
    
---- waipy.normalize() --------
Normalize by Standard Score - mean = 0 ; Variance = 1.

:Parameters:
      |  **Data, the loaded data.**
    :Returns:
      |  **normalized_data**

    :Notes:
      |  You can skip this function if it the normalization is not necessary (e.g. EOF data).

---- waipy.plot() --------
PLOT WAVELET TRANSFORM
    var = title name from data
    time  = vector get in load function
    data  = from normalize function
    dtmin = minimum resolution :1 octave
    result = dict from cwt function

--------------------------------------
Principais referências:     
    http://paos.colorado.edu/research/wavelets/bams_79_01_0061.pdf
    https://github.com/mabelcalim/waipy/blob/master/Waipy%20Examples%20/waipy_pr%C3%AAt-%C3%A0-porter.ipynb
    https://github.com/mabelcalim/waipy
    https://pywavelets.readthedocs.io/en/latest/ref/wavelets.html
    https://buildmedia.readthedocs.org/media/pdf/pywavelets/stable/pywavelets.pdf
----------------------------------------
Version by Willian Vieira de Oliveira 
29/05/19
Python: 3.7.3
----------------------------------------
"""
# import packages
import numpy as np
import waipy

nome = 'S3 (Morlet)' # nome da série para plotagem
nomeArquivo = 's3.csv'		
data = np.genfromtxt(nomeArquivo, dtype = 'float32',filling_values = 0)

time = np.linspace(0, len(data), len(data))

# Data normalization
data_norm = waipy.normalize(data)

# Continuous wavelet transform
result = waipy.cwt(data_norm, dt=0.25, pad=1, dj=0.25, s0=2*0.25, j1=7/0.25, lag1=0.72, param=6, mother='Morlet', name=nome)

# Plotting the result
waipy.wavelet_plot(var=nome, time=time, data=data_norm, dtmin=0.03125, result=result)
