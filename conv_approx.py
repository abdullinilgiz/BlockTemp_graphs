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

X_rev = []
Y_rev = []
for i in range(1+5000, 5000+5000):

    if 1/X[i]**2 < 0.000001:
        X_rev.append(1/X[i]**2)
        Y_rev.append(Y[i])

p, cov = np.polyfit(X_rev, Y_rev, 3, cov=True)
print(p)
print(np.sqrt(np.diag(cov)))

plt.scatter(X_rev, Y_rev, s=0.1)
plt.plot(X_rev, np.polyval(p, X_rev))
plt.xlim([0, 0.000001])
plt.show()
print(np.polyval(p, 0))


