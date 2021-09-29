import matplotlib.pyplot as plt
import numpy as np

Tshell_exp = [3.9, 4.5, 6.1]
Temp_exp = [400, 350, 280]

p1 = np.polyfit(Tshell_exp, Temp_exp, 1)

plt.plot(Tshell_exp, np.polyval(p1, Tshell_exp))
plt.scatter(Tshell_exp, Temp_exp)
plt.xlabel(r"$T_{shell}, нм$")
plt.ylabel(r"$T_{block}, K$")
plt.show()


kA_mod = [25000, 30000, 35000, 40000]
Temp_mod = [275, 300, 375, 425]

p2 = np.polyfit(kA_mod, Temp_mod, 1)
plt.plot(kA_mod, np.polyval(p2, kA_mod))
plt.scatter(kA_mod, Temp_mod)
plt.xlabel(r"$k_A, Дж/м^3$")
plt.ylabel(r"$T_{block}, K$")

plt.show()


