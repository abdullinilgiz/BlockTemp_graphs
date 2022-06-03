import matplotlib.pyplot as plt
import numpy as np

filename = "txtdata/05.10.21_phitheta_FC150_index0.txt"
data = np.loadtxt(filename, delimiter=' ')

phi = []
theta = []
Z_ezy = []
Z_ext = []
Z_int = []
Z_sum = []

for i in range(len(data)):
    for j in range(5):
        if j == 0:
            phi.append(data[i][j])
        if j == 1:
            theta.append(data[i][j])
        if j == 2:
            Z_ext.append(data[i][j])
        if j == 3:
            Z_ezy.append(data[i][j])
        if j == 4:
            Z_int.append(data[i][j])
    Z_sum.append(Z_int[i] + Z_ezy[i] + Z_ext[i])

ax = plt.axes(projection="3d")
ax.scatter(phi, theta, Z_ezy, c=Z_ezy, cmap='viridis')
plt.xlabel(r"$\phi$", fontsize=18)
plt.ylabel(r"$\theta$", fontsize=18)
ax.set_zlabel(r"$E$", fontsize=18)
plt.title("Easy")
plt.show()

ax = plt.axes(projection="3d")
ax.scatter(phi, theta, Z_int, c=Z_int, cmap='viridis')
plt.xlabel(r"$\phi$", fontsize=18)
plt.ylabel(r"$\theta$", fontsize=18)
ax.set_zlabel(r"$E$", fontsize=18)
plt.title("Interaction")
plt.show()

ax = plt.axes(projection="3d")
ax.scatter(phi, theta, Z_ext, c=Z_ext, cmap='viridis')
plt.xlabel(r"$\phi$", fontsize=18)
plt.ylabel(r"$\theta$", fontsize=18)
ax.set_zlabel(r"$E$", fontsize=18)
plt.title("External")
plt.show()

ax = plt.axes(projection="3d")
ax.scatter(phi, theta, Z_sum, c=Z_sum, cmap='viridis')
plt.xlabel(r"$\phi$", fontsize=18)
plt.ylabel(r"$\theta$", fontsize=18)
ax.set_zlabel(r"$E$", fontsize=18)
plt.title("Full")
plt.show()


