import matplotlib.pyplot as plt
import numpy as np
filename = 'txtdata/initial positions.txt'
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

filename = 'txtdata/pressing positions.txt'
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

x_range = np.linspace(-15, 15, 10)
y_range = np.linspace(-15, 15, 10)
z_range = np.linspace(-15, 15, 10)
Xmax = np.array([[max(Xp)-1 for i in range(0, 10)] for j in range(0, 10)])
Ymax = np.array([[max(Yp)-1 for i in range(0, 10)] for j in range(0, 10)])
Zmax = np.array([[max(Zp)-1 for i in range(0, 10)] for j in range(0, 10)])
Xmin = np.array([[min(Xp)+1 for i in range(0, 10)] for j in range(0, 10)])
Ymin = np.array([[min(Yp)+1 for i in range(0, 10)] for j in range(0, 10)])
Zmin = np.array([[min(Zp)+1 for i in range(0, 10)] for j in range(0, 10)])

# Xmax = [max(Xp), 0, 0]
# Xmin = [min(Xp), 0, 0]
# Ymax = [0, max(Yp), 0]
# Ymin = [0, min(Yp), 0]
# Zmax = [0, 0, max(Zp)]
# Zmin = [0, 0, min(Zp)]

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
