import matplotlib.pyplot as plt
import numpy as np

filename = 'txtdata/'
data = np.loadtxt(filename, delimiter=' ')

fcX = []
fcY = []
fcYer = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            fcX.append(data[i][j])
        else:
            if j == 4:
                fcY.append(data[i][j])
            else:
                if j == 5:
                    fcYer.append(data[i][j])

filename = '20.09.21_kA=30000_ZFC.txt'
data = np.loadtxt(filename, delimiter=' ')

zfcX = []
zfcY = []
zfcYer = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            zfcX.append(data[i][j])
        else:
            if j == 4:
                zfcY.append(data[i][j])
            else:
                if j == 5:
                    zfcYer.append(data[i][j])

plt.errorbar(fcX, fcY, fcYer)
plt.errorbar(zfcX, zfcY, zfcYer)
plt.xlabel(r"$T, K$")
plt.ylabel(r"$M, A/m^2$")
plt.title(r"$T_{shell} = 5 нм, k_{A} = 30k$ old positioning")
plt.show()