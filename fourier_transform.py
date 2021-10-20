import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as pat
from numpy.fft import fftfreq
import pandas as pd
from scipy.fft import fft
import glob


path = r"D:\freezing of gait\dataset_fog_release\dataset\S01R01.txt"
data = np.ravel(np.loadtxt(path), order = "F").reshape(11, 151987)
for i in range(len(data) - 1):
    data[i] = data[i] / 1000
new_data = []
for i in range(len(data)):
    new_data.append(np.array_split(data[i][:151680], 395))
new_data = np.array(new_data) # 產生(11, 395, 384)的data, 11個變數，395個time interval，每個time interval有384個值

# Fourier transfomation
result = []
for j in range(1, len(new_data) - 1):
        temp = []
        for i in new_data[j]:
            # 參數設定
            n = len(i) # 觀察值數量
            total_time = 6 # 總經過時間，單位秒
            sample_freq = n / 6 # 取樣頻率

            # 傅立葉變換計算
            yf = fft(i)[: n // 2]
            psd = yf * np.conj(yf) / (n / 2)
            x = fftfreq(n, 1 / sample_freq)[: n // 2]

            # 特徵計算
            loco_val = psd[(x >= 0.5) & (x <= 3)].sum()
            freez_val = psd[(x > 3) & (x <= 8)].sum()
            freez_index = freez_val / loco_val
            temp.append([loco_val, freez_val, freez_index])
        result.append(temp)

# array維度調整，取到小數點下第5位
result = np.array(result).transpose(1, 0, 2).ravel(order = "C").reshape(395, 27, order = "C").astype("float").round(5)
result[np.isnan(result)] = 0 # 將nan值給成0

# column names創造
body = ["ankle_", "upperleg_", "trunk_"]
direction = ["h_", "v_", "hl_"]
index = ["locoarea", "freezarea", "freezeindex"]
col_name = [i + j + k for i in body for j in direction for k in index]

# 匯出
df = pd.DataFrame(result, columns=col_name)
df.to_csv("D:/freezing of gait/dataset_fog_release/feature/SR1.txt",
            sep="\t", header=True)
 







