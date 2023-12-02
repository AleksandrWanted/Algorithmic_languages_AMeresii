def compareApproximate(s1, s2):
    ngrams = [s1[i:i + 3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)

    return count / max(len(s1), len(s2)) > 0.6


"""Задание 1:

Описать классами ваши данные

"""


class Person:
    def __init__(self, name=None, age=None, height=None, weight=None,
                 address=None):
        (self.name, self.age, self.height, self.weight,
         self.address) = name, age, height, weight, address

    def __eq__(self, obj):
        return (obj.name == None or self.name == None or
                compareApproximate(obj.name, self.name)) and (
                obj.age == None or self.age == None or
                abs(obj.age - self.age) < 2) and (
                obj.height == None or self.height == None or
                abs(obj.height - self.height) < 5) and (
                obj.weight == None or self.weight == None or
                abs(obj.weight - self.weight) < 5) and (
                obj.address == None or self.address == None or
                compareApproximate(obj.address, self.address))

    def __gt__(self, obj):
        return (obj.name == None or self.name == None or
                obj.name == self.name) and (
                obj.age == None or self.age == None or
                obj.age < self.age) and (
                obj.height == None or self.height == None or
                obj.height < self.height) and (
                obj.weight == None or self.weight == None or
                obj.weight < self.weight) and (
                obj.address == None or self.address == None or
                obj.address == self.address)

    def __repr__(self):
        return (f"Person('{self.name}', '{self.age}', '{self.height}', "
                f"'{self.weight}', '{self.address}')")


people = [
    Person("Aleksandr", 30, 180, 100, "Lenina, 55, 15"),
    Person("Alksandr", 31, 178, 98, "Lnina, 50, 15"),
    Person("Michail", 41, 185, 95, "Revolytcii, 10, 150"),
    Person("Elena", 25, 168, 55, "Lenina, 71, 30"),
    Person("Elna", 23, 165, 52, "Lenina, 77, 33"),
    Person("Svetlana", 25, 170, 52, "Lenina, 71, 30"),
]


"""Задание 2:

Реализовать поиск по полям

"""

to_search_strict = [
    Person("Aleksandr", 18, 170, 80, "Lenina, 55, 15"),
    Person(age=29, height=150),
    Person(height=120),
    Person(name="Elena")
]

for p in people:
    print(p, p > to_search_strict[1])

print("_______________________________________")


"""Задание 3:

Сделать поиск нечетким

"""

to_search_approximate = [
    Person("Alksandr", 29, 180, 102, "Lenina, 55, 15"),
    Person(height=169),
    Person(height=182, weight=100)
]

for p in people:
    print(p, p == to_search_approximate[2])
