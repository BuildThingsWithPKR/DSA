# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 07:57:24 2024

@author: PKumars'
"""

# f(n) = n^c
# log2(f(n)) = c*log2(n)
# y = mx

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams.update(plt.rcParamsDefault)


n = np.linspace(1, 30, num=300)
plt.plot(np.log2(n), np.log2(pow(n,2)),label=r'$f(n)=log2(n^2)$')
plt.plot(np.log2(n), np.log2(pow(n,3)),label=r'$f(n)=log2(n^3)$')
plt.plot(np.log2(n), np.log2(pow(n,2.5)),label=r'$f(n)=log2(n^{2.5})$')

plt.xlabel("log2(n)") 
plt.ylabel("log2(f(n))")
plt.title("Logarithm power as slope")

plt.legend()

plt.show()
