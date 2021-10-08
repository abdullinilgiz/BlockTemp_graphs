import matplotlib.pyplot as plt
import numpy as np

filename = '06.10.21_kA=30000_FC_moments.txt'
data = np.loadtxt(filename, delimiter=' ')

index = [0, 200, 400, 600, 800, 1000]

for item in index:

    X = []
    Y = []
    Z = []

    for i in range(len(data)):
        if data[i][0] == 350:
            if data[i][1] == item:
                for j in range(5):
                    if j == 2:
                        X.append(data[i][j])
                    if j == 3:
                        Y.append(data[i][j])
                    if j == 4:
                        Z.append(data[i][j])

    ax = plt.axes(projection="3d")
    ax.set_title("350T index:" + str(item))
    ax.scatter(X, Z, Y, s=0.3)

    plt.show()

    X = []
    Y = []
    Z = []

    for i in range(len(data)):
        if data[i][0] == 250:
            if data[i][1] == item:
                for j in range(5):
                    if j == 2:
                        X.append(data[i][j])
                    if j == 3:
                        Y.append(data[i][j])
                    if j == 4:
                        Z.append(data[i][j])

    ax = plt.axes(projection="3d")
    ax.set_title("250T index:" + str(item))
    ax.scatter(X, Z, Y, s=0.3)

    plt.show()

    X = []
    Y = []
    Z = []

    for i in range(len(data)):
        if data[i][0] == 150:
            if data[i][1] == item:
                for j in range(5):
                    if j == 2:
                        X.append(data[i][j])
                    if j == 3:
                        Y.append(data[i][j])
                    if j == 4:
                        Z.append(data[i][j])

    ax = plt.axes(projection="3d")
    ax.set_title("150T index:" + str(item))
    ax.scatter(X, Z, Y, s=0.3)

    plt.show()