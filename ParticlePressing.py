import matplotlib.pyplot as plt
import numpy as np
filename = 'initial positions'
data = np.loadtxt(filename, delimiter=' ')

X = []
Y = []
Z = []

for i in range(len(data)):
    for j in range(3):
        if j == 0:
            Z.append(data[i][j])
        else:
            if j == 1:
                X.append(data[i][j])
            else:
                Y.append(data[i][j])

filename = 'pressing positions'
data = np.loadtxt(filename, delimiter=' ')

Xp = []
Yp = []
Zp = []

for i in range(len(data)):
    # if (data[i][0] > 5):
        for j in range(3):
            if j == 0:
                Zp.append(data[i][j])
            else:
                if j == 1:
                    Xp.append(data[i][j])
                else:
                    Yp.append(data[i][j])

ax = plt.axes(projection="3d")

ax.scatter(X, Z, Y, s=5)
ax.scatter(Xp, Zp, Yp, s=50)
plt.xlabel(r"$x$")
# plt.xlim([-, 10])
plt.ylabel(r"$y$")
# plt.xlim([-10, 10])
ax.set_zlabel(r"$z$")
# ax.set_zlim([-10, 10])
plt.title("initialization")

plt.show()