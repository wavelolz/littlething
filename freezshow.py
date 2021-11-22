

import numpy as np
import matplotlib.pyplot as plt
import time
data = np.loadtxt("D:/freezing of gait/dataset_fog_release/dataset/S01R01.txt").transpose(1, 0)
interval = 300
move = 50
start = 76000
speed = 0.1
index = np.array([start, start + interval])
x = data[0][index[0] : index[1]] / 1000
y = data[1][index[0] : index[1]] / 1000
label = data[10][index[0] : index[1]]
 
fig, ax = plt.subplots(figsize = [20, 6])
try:
    while True:
     ax.plot(x, y)
     if any(label // 2):
         label_location = [i for i in range(len(label)) if label[i] == 2]
         ax.fill(x = [label_location[0], label_location[-1]], y = [min(min(y), -2), max(max(y), 2)], alpha = 0.3)
     ax.set_ylim([min(min(y), -2), max(max(y), 2)])
     plt.pause(speed)
     ax.cla()
     index += move
     x = data[0][index[0] : index[1]] / 1000
     y = data[1][index[0] : index[1]] / 1000
     
except IndexError:
    print("research end")
plt.show()
