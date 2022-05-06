import matplotlib.pyplot as plt
import numpy as np
filename = 'txtdata/05.05.22_random_initial_positions.txt'
data = np.loadtxt(filename, delimiter=' ')

X = []
Y = []
Z = []

for i in range(len(data)):
    for j in range(3):
        if j == 0:
            X.append(data[i][j])
        else:
            if j == 1:
                Y.append(data[i][j])
            else:
                Z.append(data[i][j])

filename = 'txtdata/05.05.22_random_pressed_positions.txt'
data = np.loadtxt(filename, delimiter=' ')

Xp = []
Yp = []
Zp = []

for i in range(len(data)):
    # if (data[i][0] > 5):
        for j in range(3):
            if j == 0:
                Xp.append(data[i][j])
            else:
                if j == 1:
                    Yp.append(data[i][j])
                else:
                    Zp.append(data[i][j])

radius = 11e-9
Xmax = np.array([[max(Xp) - radius for i in range(0, 10)] for j in range(0, 10)])
Ymax = np.array([[max(Yp) - radius for i in range(0, 10)] for j in range(0, 10)])
Zmax = np.array([[max(Zp) - radius for i in range(0, 10)] for j in range(0, 10)])
Xmin = np.array([[min(Xp) + radius for i in range(0, 10)] for j in range(0, 10)])
Ymin = np.array([[min(Yp) + radius for i in range(0, 10)] for j in range(0, 10)])
Zmin = np.array([[min(Zp) + radius for i in range(0, 10)] for j in range(0, 10)])
x_range = np.linspace(min(Xp), max(Xp), 10)
y_range = np.linspace(min(Yp), max(Yp), 10)
z_range = np.linspace(min(Zp), max(Zp), 10)

cntr = 0
for i in range(len(Xp)):
    if min(Xp)+radius < Xp[i] < max(Xp)-radius and min(Yp)+radius < Yp[i] < max(Yp)-radius and min(Zp)+radius < Zp[i] < max(Zp)-radius:
        cntr += 1
Xside = max(Xp) - min(Xp) - 2 * radius
Yside = max(Yp) - min(Yp) - 2 * radius
Zside = max(Zp) - min(Zp) - 2 * radius
# print(Xside)
# print(Yside)
# print(Zside)
print(cntr)
print(Xside * Yside * Zside)
print(cntr / Xside * Yside * Zside)

ax = plt.axes(projection="3d")

# ax.scatter(X, Y, Z, s=5)
ax.scatter(Xp, Yp, Zp, s=50)
x_surf, y_surf = np.meshgrid(x_range, y_range)
ax.plot_surface(x_surf, y_surf, Zmax, color='red')
ax.plot_surface(x_surf, y_surf, Zmin, color='red')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
ax.set_zlabel(r"$z$")
plt.title("Pressed particles")
plt.show()

ax = plt.axes(projection="3d")
ax.scatter(Xp, Yp, Zp, s=50)
x_surf, z_surf = np.meshgrid(x_range, z_range)
ax.plot_surface(x_surf, Ymax, z_surf, color='red')
ax.plot_surface(x_surf, Ymin, z_surf, color='red')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
ax.set_zlabel(r"$z$")
plt.title("Pressed particles")
plt.show()

ax = plt.axes(projection="3d")
ax.scatter(Xp, Yp, Zp, s=50)
y_surf, z_surf = np.meshgrid(y_range, z_range)
ax.plot_surface(Xmax, y_surf, z_surf, color='red')
ax.plot_surface(Xmin, y_surf, z_surf, color='red')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
ax.set_zlabel(r"$z$")
plt.title("Pressed particles")
plt.show()
