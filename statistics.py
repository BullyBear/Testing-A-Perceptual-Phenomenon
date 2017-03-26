import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mean1 = 14.051
median1 = 14.357
range1 = 13.698
var1 = 12.669
stdev1 = 3.559

cong = np.array([mean1, median1, range1, var1, stdev1])

fig1 = plt.boxplot(cong)



mean2 = 22.016
median2 = 21.018
range2 = 19.568
var2 = 23.012
stdev2 = 4.797

incong = np.array([mean2, median2, range2, var2, stdev2])

fig2 = plt.boxplot(incong)


plt.show()

