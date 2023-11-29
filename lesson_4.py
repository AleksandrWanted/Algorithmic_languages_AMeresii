import random

import numpy as np

# задание 1: Используя numpy посчитать сумму ряда 0 - 100

sumNumRow = np.sum(np.array(range(0, 100)))
print(sumNumRow)

# задание 2: Используя numpy посчитать сумму ряда 0 - input()

upperLimit = input("Для вычисления суммы ряда введите верхнюю границу диапозона: ")
sumNumRow = np.sum(np.array(range(0, int(upperLimit))))
print(sumNumRow)

# задание 3: Используя numpy посчитать среднее среди 100 случайных чисел

randSumRow = []

while len(randSumRow) < 101:
    randSumRow.append(random.randrange(1, 1000))

randAverage = np.sum(randSumRow) / len(randSumRow)
print(randAverage)
