import numpy as np
import matplotlib.pyplot as plt
import csv
import uncertainties.unumpy as unp
import scipy.stats as stats

f1 = np.genfromtxt("6.dat",delimiter=" ",unpack=True,usecols=0)
A1 = np.genfromtxt("6.dat",delimiter=" ",unpack=True,usecols=1)

plt.plot(f1,A1)
plt.show()
