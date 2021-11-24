

import numpy as np
import matplotlib.pyplot as plt
import time
data = np.loadtxt("D:/freezing of gait/dataset_fog_release/dataset/S01R01.txt").transpose(1, 0)
interval = 10
move = 3
start = 1700
stay_time = 0.7


index = np.array([int(start * 64), int(start * 64 + interval * 64)])
x = data[0][index[0] : index[1]] / 1000
y = data[1][index[0] : index[1]] / 1000
label = data[10][index[0] : index[1]]
 
fig, ax = plt.subplots(figsize = [20, 6])

while True:
    ax.plot(x, y)
    ax.fill_between(x, y1 = min(min(y), -2), y2 = max(max(y), 2), where = (label == 0), alpha = 0.3, color = "yellow")
    ax.fill_between(x, y1 = min(min(y), -2), y2 = max(max(y), 2), where = (label == 2), alpha = 0.3, color = "red")
    ax.set_ylim([min(min(y), -2), max(max(y), 2)])
    plt.pause(stay_time)
    ax.cla()
    index += int(move * 64)
    x = data[0][index[0] : index[1]] / 1000
    y = data[1][index[0] : index[1]] / 1000
    label = data[10][index[0] : index[1]]


plt.show()


