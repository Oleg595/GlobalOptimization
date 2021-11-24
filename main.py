import math

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def reader(url):
    """
    Read a csv file
    """
    reader = pd.read_excel(url)
    x = []
    y = []
    for i in range(200):
        x.append([reader["x_min"][i], reader["x_max"][i]])
        y.append([reader["y_min"][i], reader["y_max"][i]])

    return x, y


def plot(X, Y, point, title):
    fig, ax = plt.subplots()
    ax.plot(point[0], point[1], 'bo')
    for i in range(50):
        rect = patches.Rectangle((X[i][0], Y[i][0]), X[i][1] - X[i][0], Y[i][1] - Y[i][0], linewidth=1, edgecolor='r',
                                 facecolor='none')
        ax.add_patch(rect)
    plt.title(title)
    plt.legend(['точка минимума', 'итерации 1 - 50'])
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(point[0], point[1], 'bo')
    for i in range(50, 100):
        rect = patches.Rectangle((X[i][0], Y[i][0]), X[i][1] - X[i][0], Y[i][1] - Y[i][0], linewidth=1, edgecolor='y',
                                 facecolor='none')
        ax.add_patch(rect)
    plt.title(title)
    plt.legend(['точка минимума', 'итерации 51 - 100'])
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(point[0], point[1], 'bo')
    for i in range(100, 150):
        rect = patches.Rectangle((X[i][0], Y[i][0]), X[i][1] - X[i][0], Y[i][1] - Y[i][0], linewidth=1, edgecolor='b',
                                 facecolor='none')
        ax.add_patch(rect)
    plt.title(title)
    plt.legend(['точка минимума', 'итерации 101 - 150'])
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(point[0], point[1], 'bo')
    for i in range(150, 200):
        rect = patches.Rectangle((X[i][0], Y[i][0]), X[i][1] - X[i][0], Y[i][1] - Y[i][0], linewidth=1, edgecolor='c',
                                 facecolor='none')
        ax.add_patch(rect)
    plt.title(title)
    plt.legend(['точка минимума', 'итерации 151 - 200'])
    plt.show()

# Ackley function
X, Y = reader("Ackley.xlsx")
plot(X, Y, [0, 0], "Ackley function")

# Himmelblau function
X, Y = reader("Himmelblau.xlsx")
plot(X, Y, [[3, -2.805118, -3.77931, 3.584428], [2, 3.131312, -3.283186, -1.848126]], "Himmelblau function")
