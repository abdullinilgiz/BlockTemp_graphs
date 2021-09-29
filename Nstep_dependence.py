import matplotlib.pyplot as plt
import numpy as np
##OLD
#150K
M_fc = [1.56348e-16, 1.70933e-16, 1.6304e-16]
M_zfc = [2.59281e-17, 3.74468e-17, 2.34323e-17]
N_fc = [3000, 1600, 800]

for i in range(len(N_fc)):
    N_fc[i] = 1 / (N_fc[i]**2)

plt.plot(N_fc, M_fc)
plt.plot(N_fc, M_zfc)
plt.title("old pos 150K")
plt.show()


#250K
M_fc = [1.54086e-16, 1.51075e-16, 1.57856e-16]
M_zfc = [1.49939e-16, 1.22282e-16, 6.58543e-17]
N_fc = [3000, 1600, 800]

for i in range(len(N_fc)):
    N_fc[i] = 1 / (N_fc[i]**2)

plt.plot(N_fc, M_fc)
plt.plot(N_fc, M_zfc)
plt.title("old pos 250K")
plt.show()

#350K
M_fc = [1.25225e-16, 1.20257e-16, 1.26482e-16]
M_zfc = [1.2542e-16, 1.31667e-16, 1.28354e-16]
N_fc = [3000, 1600, 800]

for i in range(len(N_fc)):
    N_fc[i] = 1 / (N_fc[i]**2)

plt.plot(N_fc, M_fc)
plt.plot(N_fc, M_zfc)
plt.title("old pos 350K")
plt.show()