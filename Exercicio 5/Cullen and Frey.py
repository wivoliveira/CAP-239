# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:38:16 2019

@author: Willian
"""
import numpy as np
import pylab

nomeArquivo = 'out.dat'		
data = np.genfromtxt(nomeArquivo, dtype = 'float32',filling_values = 0)

# -----> o histogrma esta saindo DIFERENTE do resultado obtido em R
""" Empirical density """
pylab.clf()
pylab.hist(data[:,9], bins=10, color='0.3', ec='1', density=True)#, cumulative=True)
pylab.title('Empirical density', fontsize = 16)
pylab.plt.xlabel('Data')
pylab.plt.ylabel('Density')

""" Cumulative distribution """
pylab.plt.subplots()
pylab.title('Cumulative distribution', fontsize = 16)
pylab.plot(np.sort(data[:,9]), np.linspace(0, 1, len(data[:, 9]), endpoint=False), linewidth=4)
pylab.plt.xlabel('Data')
pylab.plt.ylabel('CDF')
