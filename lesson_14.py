"""Задание 1:

Сделать инт такой что 2 + 2 = 5

"""


class MyInt(int):
    def __add__(self, x):
        return super().__add__(x + 1)


y = MyInt(2)
print(y + 2)
print(y + 3)

"""Задание 2:

Сделать лист такой что больше 10 элементов нельзя в него поместить

"""


class MyList(list):
    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('error list length exceed > 10')
        else:
            super().append(x)

    def append(self, x):
        if len(self) == 10:
            raise ValueError('error list length exceed > 10')
        else:
            super().append(x)


print("___________________________________________")

y = MyList([1, 2, 3, 4, 5, 6, 7, 8])

y.append(9)
print(y)
y.append(100)
print(y)
y.append(102)

"""Задание 3:

Сделать лист с уникальными элементами

"""

class MyNewList(set):
    pass

y = MyNewList([1,2,5,5,1,2,3])

print(y)