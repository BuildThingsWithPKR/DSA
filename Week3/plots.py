# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 06:32:58 2024

@author: PKumars'
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams.update(plt.rcParamsDefault)


n = np.linspace(1, 30, num=300)

plt.plot(np.log2(n), np.log2(8*n),label=r'$log2(8n)$')
plt.plot(np.log2(n), np.log2(4*n*np.log2(n)),label=r'$4nlog2(n)$')
plt.plot(np.log2(n), np.log2(2*n*n),label=r'$log2(2n^2)$')
plt.plot(np.log2(n), np.log2(n*n*n),label=r'$log2(n^3)$')
plt.plot(np.log2(n), np.log2(pow(2,n)),label=r'$log2(2^n)$')

plt.xlabel("log(n)") 
plt.ylabel("log(f(n))") 
plt.title("Big-O Approximation Plots")

plt.legend()

plt.show()
