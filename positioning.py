import matplotlib.pyplot as plt
import numpy as np

filename = 'positioning.txt'
data = np.loadtxt(filename, delimiter=' ')

X = []
Y = []
Z = []

for i in range(len(data)):
    #if 50 > i:
        for j in range(3):
            if j == 0:
                X.append(data[i][j])
            else:
                if j == 1:
                    Y.append(data[i][j])
                else:
                    if j == 2:
                        Z.append(data[i][j])


# print(X)
# print(Y)
# print(Z)



ax = plt.axes(projection="3d")

ax.scatter(X, Y, Z, s=600)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim3d(0, 10)
ax.set_ylim3d(0, 10)
ax.set_zlim3d(0, 10)
plt.show()