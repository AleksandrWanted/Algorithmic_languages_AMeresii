import string
import unittest
from random import choice

import names
import pytest
from lesson_17 import *

"""Задание 2:

Подобрать эталонный метод в одной из библиотек

Ответ: сравнивать будет наш метод compare с библиотекой rapidfuzz (https://github.com/maxbachmann/RapidFuzz) 
которая имеет лицензию MIT, что делает ее более менее официальной для некоторых проектов

"""

from rapidfuzz import fuzz

str1 = "horror"
str2 = "comedy"
print("Сравнение строк [%s] и [%s]. Результат метод compare - %s, метод fuzz.ratio - %s" %
      (str1, str2, compare(str1, str2), fuzz.ratio(str1, str2)))

str1 = "horror"
str2 = "heror"
print("Сравнение строк [%s] и [%s]. Результат метод compare - %s, метод fuzz.ratio - %s" %
      (str1, str2, compare(str1, str2), fuzz.ratio(str1, str2)))

str1 = "horror"
str2 = "horor"
print("Сравнение строк [%s] и [%s]. Результат метод compare - %s, метод fuzz.ratio - %s" %
      (str1, str2, compare(str1, str2), fuzz.ratio(str1, str2)))

str1 = "horror"
str2 = "horror"
print("Сравнение строк [%s] и [%s]. Результат метод compare - %s, метод fuzz.ratio - %s" %
      (str1, str2, compare(str1, str2), fuzz.ratio(str1, str2)))

str1 = "horror"
str2 = "rorroh"
print("Сравнение строк [%s] и [%s]. Результат метод compare - %s, метод fuzz.ratio - %s" %
      (str1, str2, compare(str1, str2), fuzz.ratio(str1, str2)))

str1 = "horror"
str2 = "хоррор"
print("Сравнение строк [%s] и [%s]. Результат метод compare - %s, метод fuzz.ratio - %s" %
      (str1, str2, compare(str1, str2), fuzz.ratio(str1, str2)))

"""Задание 3:

Провести baseline тестирование

Ответ: провести базовое тестирование данной программы не возможно так как к ней отсутствуют
не функциональные требования. Но мы можем предположить что выбранная функция для сравнения строк
должна выполнять сравнение строк содержащих до 100 символов менее чем за 1мс.
Ниже представлен код который позволяет провести базовое тестирование на этих условиях.

"""

import time

str1 = "horror"
str2 = "heror"
start = time.perf_counter()
fuzz.ratio(str1, str2)
end = time.perf_counter()

print("Время работы функции fuzz.ratio при сравнении строк [%s] и [%s]: %s миллисекунд" % (str1, str2,
                                                                                           (end * 1000 - start * 1000)))

str1 = ''.join(choice(string.ascii_uppercase) for i in range(100))
str2 = ''.join(choice(string.ascii_uppercase) for i in range(100))

start = time.perf_counter()
fuzz.ratio(str1, str2)
end = time.perf_counter()

print("Время работы функции fuzz.ratio при сравнении строк длинной 100 символов: %s миллисекунд" % (
        end * 1000 - start * 1000))
