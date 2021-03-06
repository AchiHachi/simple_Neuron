import numpy as np


def f(x):    # Функция активации
    return 1 if x >= 0.5 else 0     # Результирующий параметр симпатии


def neuron(house, rock, sweet):
    x = np.array([house, rock, sweet])    # Вектор входного сигнала на основе параметров
    w1 = [0.3, 0.3, 0]    # Значения веса параметров (дом, рок, красота) первого нейрона
    w2 = [0.4, -0.5, 1]    # Значения веса параметров (дом, рок, красота) второго нейрона
    weight1 = np.array([w1, w2])    # Матрица 2х3 (объединяем веса двух нейронов)
    weight2 = np.array([-1, 1])     # Вектор 1х2 (вектор связи для выходного нейрона)

    sum_hidden = np.dot(weight1, x)    # Вычисляем сумму для каждого нейрона
    print("Значения сумм на нейронах скрытого слоя: " + str(sum_hidden))

    out_hidden = np.array([f(x) for x in sum_hidden])    # Вычисляем вектор выходных значений скрытых нейронов
    print("Значения на выходах нейронов скрытого слоя: " + str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)    # Вычисляем сумму на выходном нейроне
    y = f(sum_end)
    print("Выходное значение нейронной сети: " + str(y) + "\n")

    return y


def main(h, r, s):
    res = neuron(h, r, s)
    if res == 1:
        return "Ты мне нравишься..."
    else:
        return "До встречи"


assert main(0, 0, 0) == "До встречи"
assert main(0, 0, 1) == "Ты мне нравишься..."
assert main(0, 1, 0) == "До встречи"
assert main(0, 1, 1) == "Ты мне нравишься..."
assert main(1, 0, 0) == "До встречи"
assert main(1, 0, 1) == "Ты мне нравишься..."
assert main(1, 1, 0) == "До встречи"
assert main(1, 1, 1) == "До встречи"

