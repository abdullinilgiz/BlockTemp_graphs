import matplotlib.pyplot as plt
import numpy as np

filename = '17.09.21_kA=30000_ZFC_convergence.txt'
data = np.loadtxt(filename, delimiter=' ')
lastdotX = []
lastdotY = []
lastdotZ = []

X = []
Y = []
Z = []
counter = 0

for i in range(len(data)):
    for j in range(3):
        counter += 1
        if j == 0:
            Z.append(data[i][j])
        else:
            if j == 1:
                X.append(data[i][j])
            else:
                Y.append(data[i][j])
    if (((i % 900) == 899) and i != 0):
        lastdotX.append(X[len(X)-1])
        lastdotY.append(Y[len(Y)-1])
        lastdotZ.append(Z[len(Z)-1])

print(np.size(X), np.size(Y), np.size(Z))
print(np.size(lastdotX))

ax = plt.axes(projection="3d")

ax.scatter(X, Z, Y, s=0.3)
ax.scatter3D(lastdotX, lastdotZ, lastdotY, s=100, c="red")
plt.xlabel(r"$N_{step}$")
plt.ylabel(r"$T, K$")
ax.set_zlabel(r"$M, A^2/m^2$")
plt.title(" ")

plt.show()

outF = open("17.09.21_FC.txt", "w")
for i in range(len(lastdotX)):
    outF.write(str(lastdotZ[i]))
    outF.write(str(" "))
    outF.write(str(lastdotY[i]))
    outF.write("\n")
outF.close()
