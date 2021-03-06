import matplotlib.pyplot as plt
import numpy as np
filename = 'longcalc/26.10.21_kA=30000_ZFC_convergence.txt'
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

ax.scatter(X, Z, Y, s=0.1)
plt.xlabel(r"$N_{step}$")
plt.ylabel(r"$T, K$")
ax.set_zlabel(r"$M, A^2/m^2$")
plt.title("5nm")

plt.show()
