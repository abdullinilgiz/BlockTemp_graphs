import matplotlib.pyplot as plt
import numpy as np
filename = 'txtdata/27.09.21_kA=30000_ZFC_convergence.txt'
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

ax = plt.axes(projection="3d")

ax.scatter(X, Z, Y, s=0.3)
plt.xlabel(r"$N_{step}$")
plt.ylabel(r"$T, K$")
ax.set_zlabel(r"$M, A^2/m^2$")
plt.title("28.09 5nm ZFC new")

plt.show()

filename = 'txtdata/27.09.21_kA=30000_FC_convergence.txt'
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

ax = plt.axes(projection="3d")

ax.scatter(X, Z, Y, s=0.3)
plt.xlabel(r"$N_{step}$")
plt.ylabel(r"$T, K$")
ax.set_zlabel(r"$M, A^2/m^2$")
plt.title("28.09 5nm FC new")

plt.show()

filename = 'txtdata/27.09.21_old_kA=30000_ZFC_convergence.txt'
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

ax = plt.axes(projection="3d")

ax.scatter(X, Z, Y, s=0.3)
plt.xlabel(r"$N_{step}$")
plt.ylabel(r"$T, K$")
ax.set_zlabel(r"$M, A^2/m^2$")
plt.title("28.09 5nm ZFC old")

plt.show()

filename = 'txtdata/27.09.21_old_kA=30000_FC_convergence.txt'
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

ax = plt.axes(projection="3d")

ax.scatter(X, Z, Y, s=0.3)
plt.xlabel(r"$N_{step}$")
plt.ylabel(r"$T, K$")
ax.set_zlabel(r"$M, A^2/m^2$")
plt.title("28.09 5nm FC old")

plt.show()