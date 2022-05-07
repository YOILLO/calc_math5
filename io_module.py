import matplotlib.pyplot as plt
from functions import *

def plot(arr, x_0, y_0):
    x = []
    y = []
    for i in arr:
        x.append(i)
        y.append(arr[i])
    plt.plot(x, y)
    plt.plot(x_0, y_0, marker="o", markersize=10)
    plt.show()


def ask_float(str):
    num = 0
    while True:
        try:
            num = float(input(str))
            return num
        except Exception:
            print("Введите число")

def ask_function():
    for i in range(1, 5):
        print(i, ": y' = ", get_str_func(i))
    num  = 0
    while num < 1 or num > 4:
        try:
            num = int(input("Выберите функцию: "))
        except Exception:
            print("Введите число")
    return get_func(num)