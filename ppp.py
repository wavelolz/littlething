from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt
# draw circles
'''n = 2000
circle_num = 10
radius = np.linspace(10, 20, circle_num, endpoint=True)
fig, ax = plt.subplots(figsize = [15, 15])
ax.set_xlim([-22, 22])
ax.set_ylim([-22, 22])
marker_ang = np.linspace(0, 2 * np.pi, 12, endpoint= False)
for i in radius:
    angle = np.linspace(0, 2 * np.pi, 2000)
    x = i * np.cos(angle)
    y = i * np.sin(angle)
    marker_x = i * np.cos(marker_ang)
    marker_y = i * np.sin(marker_ang)
    ax.plot(x, y)
    ax.scatter(marker_x, marker_y, marker = "H")
    ax.set_aspect("equal")
    plt.pause(0.5)
plt.show()'''

# draw square
'''loc = np.array([[0, 0],
                [0, 3], 
                [-1, 3],
                [1, 3], 
                [1, 5], 
                [-1, 5],
                [-1, 3]])
n = 1000
angle = np.linspace(0, 2*np.pi, n, endpoint= False)
fig, ax = plt.subplots()
ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_aspect("equal")
color = ["#FF5733", "#FFE633", "#9CFF33", "#1AB92B", "#1AA1B9", "#5195FE", "#5156FE", 
        "#AD51FE", "#FB51FE", "#FE5169"]
color_select = 0
for i in angle:
    rot_mat = np.array([[np.cos(i), -np.sin(i)],
                    [np.sin(i), np.cos(i)]])
    rotate = np.matmul(loc, rot_mat)
    line_loc = list(zip(rotate[0], rotate[1]))
    square_loc = rotate[2:].ravel(order = "F").reshape(2, 5, order = "C")
    col = color[color_select % 10]
    ax.plot(line_loc[0], line_loc[1], color = col)
    ax.plot(square_loc[0], square_loc[1], color = col)
    plt.pause(0.05)
    color_select += 1
plt.show()'''

    




