import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

median1 = 14.36
q1_1 = 11.34
q3_1 = 16.79
min1 = 8.63
max1 = 22.33

cong = np.array([median1, q1_1, q3_1, min1, max1])

median2 = 21.02
q1_2 = 18.64
q3_2 = 24.52
min2 = 15.69
max2 = 35.26

incong = np.array([median2, q1_2, q3_2, min2, max2])


fig_2_plot = [cong, incong]

fig = plt.figure(1, figsize =(9, 6))
ax = fig.add_subplot(111)
ax.set_title('BoxPlot Distributions', fontweight = 'bold')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_ylim(0, 30)
bp = ax.boxplot(fig_2_plot)


plt.show()