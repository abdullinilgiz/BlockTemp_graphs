import matplotlib.pyplot as plt
import numpy as np

filename = '6.1_1_d.txt'
data = np.loadtxt(filename, delimiter='\t')

print(data)

fcX = []
fcY = []
fcYer = []

for i in range(len(data)):
    for j in range(3):
        if j == 0:
            fcX.append(data[i][j])
        if j == 2:
            fcY.append(data[i][j])

filename = '6.1_2_d.txt'
data = np.loadtxt(filename, delimiter='\t')

zfcX = []
zfcY = []
zfcYer = []

for i in range(len(data)):
    for j in range(3):
        if j == 0:
            zfcX.append(data[i][j])
        if j == 2:
            zfcY.append(data[i][j])

plt.plot(fcX, fcY)
plt.scatter(fcX, fcY)
plt.plot(zfcX, zfcY)
plt.scatter(zfcX, zfcY)
plt.xlabel(r"$T, K$")
plt.ylabel(r"$M, (emu/g)$")
plt.legend(["ZFC", "FC"])
plt.title(r"$T_{shell} = 6.1 нм$")



plt.show()