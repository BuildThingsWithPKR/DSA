# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 06:32:58 2024

@author: PKumars'
"""

'''
# Numpy
# MatplotLib
# Latex
Requires latex installed for latex interpretation of legends
'''

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams.update(plt.rcParamsDefault)


n = np.linspace(1, 30, num=300)

plt.plot(np.log(n), np.log(8*n),label=r'$log(8n)$')
plt.plot(np.log(n), np.log(4*n*np.log(n)),label=r'$4nlog(n)$')
plt.plot(np.log(n), np.log(2*n*n),label=r'$log(2n^2)$')
plt.plot(np.log(n), np.log(n*n*n),label=r'$log(n^3)$')
plt.plot(np.log(n), np.log(pow(2,n)),label=r'$log(2^n)$')

plt.xlabel("log(n)") 
plt.ylabel("log(f(n))") 
plt.title("Big-O Approximation Plots")

plt.legend()

plt.show()
