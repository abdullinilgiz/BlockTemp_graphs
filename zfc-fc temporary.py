import matplotlib.pyplot as plt
import numpy as np

filename = 'txtdata/17.09.21_FC.txt'
data = np.loadtxt(filename, delimiter=' ')

fcX = []
fcY = []
fcYer = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            fcX.append(data[i][j])
        else:
            if j == 1:
                fcY.append(data[i][j])

filename = 'txtdata/17.09.21_ZFC.txt'
data = np.loadtxt(filename, delimiter=' ')

zfcX = []
zfcY = []
zfcYer = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            zfcX.append(data[i][j])
        else:
            if j == 1:
                zfcY.append(data[i][j])

plt.errorbar(fcX, fcY)
plt.errorbar(zfcX, zfcY)
plt.xlabel(r"$T, K$")
plt.ylabel(r"$M, A \cdot m^2$")
plt.title(r"$T_{shell} = 5 нм$")
plt.show()
