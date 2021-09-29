import matplotlib.pyplot as plt
import numpy as np

filename = 'I2.dat'
data1 = np.loadtxt(filename)
filename = 'lump.dat'
data2 = np.loadtxt(filename)

X = []
Y = []

for i in range(len(data1)):
    if 510 < data1[i][1] < 640:
        X.append(data1[i][1])
        Y.append((data2[i][2] - data1[i][2]) / data2[i][2])

plt.plot(X, Y)
plt.xlabel(r"$\lambda, нм$")
plt.ylabel('a.u.')
plt.show()

for i in range(len(X)):
    X[i] = 1 / X[i] / 1.00027

plt.plot(X, Y)
plt.xlabel(r"$\nu, нм^{-1}$")
plt.ylabel('a.u.')
plt.show()

Xm = []
Ym = []

for i in (range(len(Y) - 4)):
    if Y[i] < Y[i + 2] and Y[i + 1] < Y[i + 2] and Y[i + 2] > Y[i + 3] and Y[i + 2] > Y[i + 4]:
        if 0.001839 < X[i] < 0.001959:  # and X[i] < 0.00177 :
            Ym.append(Y[i + 2])
            Xm.append(X[i + 2])

# print(Xm)
# print(Xm)

plt.scatter(X, Y, s=1, c='black')
plt.scatter(Xm, Ym, s=10, c='red')
plt.xlabel(r"$\nu, нм^{-1}$")
plt.ylabel('a.u.')
plt.show()

Xm = list(reversed(Xm))
outF = open("Xm.txt", "w")
for item in Xm:
    outF.write(str(item))
    outF.write("\n")
outF.close()

Nu_d = []
Nu = []
for i in range(len(Xm) - 1):
    Nu_d.append(Xm[i + 1] - Xm[i])
    Nu.append(Xm[i])

outF = open("delta Nu - Nu.txt", "w")
for i in range(len(Nu)):
    outF.write(str(Nu_d[i]) + " " + str(Nu[i]))
    outF.write("\n")
outF.close()

p, cov = np.polyfit(Nu_d, Nu, 1, cov=True)
print(p)
print(np.sqrt(np.diag(cov)))

plt.scatter(Nu_d, Nu, c='black')
plt.plot(Nu_d, np.polyval(p, Nu_d))
plt.xlabel(r"$\Delta \nu, нм^{-1}$")
plt.ylabel(r"$\nu, нм^{-1}$")

plt.show()
