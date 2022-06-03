import matplotlib.pyplot as plt
import numpy as np
date = '27.09.21'
filename = 'txtdata/' + date + '_old_kA=30000_FC.txt'
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

filename = 'txtdata/' + date + '_old_kA=30000_ZFC.txt'
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

filename = 'txtdata/' + date + '_kA=30000_FC.txt'
data = np.loadtxt(filename, delimiter=' ')

fcX1 = []
fcY1 = []
fcYer1 = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            fcX1.append(data[i][j])
        else:
            if j == 4:
                fcY1.append(data[i][j])
            else:
                if j == 5:
                    fcYer1.append(data[i][j])

filename = 'txtdata/' + date + '_kA=30000_ZFC.txt'
data = np.loadtxt(filename, delimiter=' ')

zfcX1 = []
zfcY1 = []
zfcYer1 = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            zfcX1.append(data[i][j])
        else:
            if j == 4:
                zfcY1.append(data[i][j])
            else:
                if j == 5:
                    zfcYer1.append(data[i][j])

today = "05.05.22_random"
filename = 'txtdata/' + today + '_kA=30000_FC.txt'
data = np.loadtxt(filename, delimiter=' ')

fcX2 = []
fcY2 = []
fcYer2 = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            fcX2.append(data[i][j])
        else:
            if j == 4:
                fcY2.append(data[i][j])
            else:
                if j == 5:
                    fcYer2.append(data[i][j])

filename = 'txtdata/' + today + '_kA=30000_ZFC.txt'
data = np.loadtxt(filename, delimiter=' ')

zfcX2 = []
zfcY2 = []
zfcYer2 = []

for i in range(len(data)):
    for j in range(6):
        if j == 0:
            zfcX2.append(data[i][j])
        else:
            if j == 4:
                zfcY2.append(data[i][j])
            else:
                if j == 5:
                    zfcYer2.append(data[i][j])


plt.errorbar(fcX, fcY, fcYer)
plt.errorbar(zfcX, zfcY, zfcYer)
plt.errorbar(fcX1, fcY1, fcYer1)
plt.errorbar(zfcX1, zfcY1, zfcYer1)
plt.errorbar(fcX2, fcY2, fcYer2)
plt.errorbar(zfcX2, zfcY2, zfcYer2, c="black")
plt.legend([r"$FC_{cubic}$", r"$ZFC_{cubic}$", r"$FC_{hex}$", r"$ZFC_{hex}$", r"$FC_{rnd}$", r"$ZFC_{rnd}$"])
plt.xlabel(r"$T, K$")
plt.ylabel(r"$M, A \cdot m^2$")
plt.title(r"$T_{shell} = 5 нм, k_{A} = 30k$")
plt.show()

# outF = open("fcX_fcY " + date + ".txt", "w")
# outF.write('FC Nstep = 1600\n')
# for i in range(len(fcX)):
#     if fcX[i] == 250 or fcX[i] == 150 or fcX[i] == 350:
#         outF.write(str(fcX[i]) + ' ' + str(fcY[i]))
#         outF.write("\n")
# outF.close()
#
# outF = open("zfcX_zfcY " + date + ".txt", "w")
# outF.write('ZFC Nstep = 1600\n')
# for i in range(len(zfcX)):
#     if zfcX[i] == 250 or zfcX[i] == 150 or zfcX[i] == 350:
#         outF.write(str(zfcX[i]) + ' ' + str(zfcY[i]))
#         outF.write("\n")
# outF.close()
#
#
# print('fc')
# print(fcX, fcY)
# print('zfc')
# print(zfcX, zfcY)

