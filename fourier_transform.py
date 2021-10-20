import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as pat
from numpy.fft import fftfreq
import pandas as pd
from scipy.fft import fft
import glob
# path = [str(i) for i in glob.glob(
#     r"D:/dataset_fog_release/dataset/S*.txt")]
path = r"D:/dataset_fog_release/dataset/S01R01.txt"
data = np.ravel(np.loadtxt(path), order = "F").reshape(11, 151987)
for i in range(len(data) - 1):
    data[i] = data[i] / 1000
for i in range(2):
    data[i] = np.array_split(np.array(data[i][:151680]), 395)

# def run(p):
#     time = []
#     f1 = []
#     f2 = []
#     f3 = []
#     f4 = []
#     f5 = []
#     f6 = []
#     f7 = []
#     f8 = []
#     f9 = []
#     annotation = []
#     with open(p) as f:
#         lines = f.readlines()
#         for i in lines:
#             result = i.split(" ")
#             time.append(float(result[0]) / 1000)
#             f1.append(int(result[1]) / 1000)
#             f2.append(int(result[2]) / 1000)
#             f3.append(int(result[3]) / 1000)
#             f4.append(int(result[4]) / 1000)
#             f5.append(int(result[5]) / 1000)
#             f6.append(int(result[6]) / 1000)
#             f7.append(int(result[7]) / 1000)
#             f8.append(int(result[8]) / 1000)
#             f9.append(int(result[9]) / 1000)
#             annotation.append(int(result[10].rstrip()))
#     ts = np.array_split(time[:151680], 395)
#     f1s = np.array_split(f1[:151680], 395)
#     f2s = np.array_split(f2[:151680], 395)
#     f3s = np.array_split(f3[:151680], 395)
#     f4s = np.array_split(f4[:151680], 395)
#     f5s = np.array_split(f5[:151680], 395)
#     f6s = np.array_split(f6[:151680], 395)
#     f7s = np.array_split(f7[:151680], 395)
#     f8s = np.array_split(f8[:151680], 395)
#     f9s = np.array_split(f9[:151680], 395)
#     l = [f1s, f2s, f3s, f4s, f5s, f6s, f7s, f8s, f9s]

#     all_pt = []
#     for j in range(len(l)):
#         one_pt = []
#         for i in np.array(l[j]):
#             n = len(i)
#             total_time = 6
#             sample_freq = n / 6
#             yf = fft(i)[: n // 2]
#             psd = yf * np.conj(yf) / (n / 2)
#             x = fftfreq(n, 1 / sample_freq)[: n // 2]
#             loco_val = psd[(x >= 0.5) & (x <= 3)].sum()
#             freez_val = psd[(x > 3) & (x <= 8)].sum()
#             freez_index = freez_val / loco_val
#             one_pt.append([loco_val, freez_val, freez_index])
#         all_pt.append(one_pt)
#     all_pt = np.array(all_pt).transpose([1, 0, 2]).reshape(
#         395, 27).astype("float").round(5)
#     all_pt[np.isnan(all_pt)] = 0
#     body = ["ankle_", "upperleg_", "trunk_"]
#     direction = ["h_", "v_", "hl_"]
#     index = ["locoarea", "freezarea", "freezeindex"]
#     col_name = [i + j + k for i in body for j in direction for k in index]
#     df = pd.DataFrame(all_pt, columns=col_name)
#     df.to_csv("D:/freezing of gait/dataset_fog_release/feature/" + p[-10:],
#             sep="\t", header=True)
# for i in path:
#     run(i)
