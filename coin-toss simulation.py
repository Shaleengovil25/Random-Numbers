# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:09:29 2020

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails=[]  #Array containing number of Tails appeared in 10 tosses.
for x in range(10000):
    tails=[0]   #Array containing 10 outcomes of 10 tosses.
    for x in range(10):
        coin=np.random.randint(0,2)
        tails.append(tails[x]+coin)
    final_tails.append(tails[-1])
plt.hist(final_tails,bins=10)
plt.ylabel('Frequency')  # Frequrncy of Heads or Tails When process is simulated 10K times.
plt.xlabel('Bins')       #No. of  Heads or Tails in 10 throws.
plt.title('Coin-toss Simulation')
plt.show()
