from matplotlib import transforms
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import pandas as pd
from pathlib import Path
import random

r_min, r_max = 3, 5
radius = np.linspace(r_min, r_max, 10)
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim([-r_max*1.1, r_max*1.1])
ax.set_ylim([-r_max*1.1, r_max*1.1])
for i in radius:
    angle = np.linspace(0, 2*np.pi, int(10*i))
    x = i * np.cos(angle)
    y = i * np.sin(angle)
    ax.scatter(x, y, color = "black")

xleft_min, xleft_max = -8, -4
xleft = np.linspace(xleft_min, xleft_max, 100)

plt.show()








    




    




