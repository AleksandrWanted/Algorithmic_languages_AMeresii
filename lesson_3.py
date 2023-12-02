"""Задание 1:

Выбрать персонажа, перебрав всех циклом в списке

"""

personsList = [
    ["Aleksandr", "Meresii", "АСУ4-23-1мз", 1, "group leader"],
    ["Petr", "Ivanov", "АСУ4-23-1мз", 1, "student"],
    ["Ivan", "Semenov", "АСУ4-22-1мз", 1, "student"],
    ["Sergei", "Petrov", "АСУ4-21-1мз", 3, "student"],
    ["Elena", "Popova", "АСУ4-21-1мз", 3, "group leader"],
    ["John", "Doe", "АСУ8-23-1мз", 1, "student"],
    ["Maria", "Utkina", "АСУ8-23-1мз", 1, "group leader"],
]


def search_person_by_attr_in_list(attr_name, attr_value):
    target = []

    for person in personsList:
        if attr_name == "name":
            if person[0] == attr_value:
                target.append(person)
        elif attr_name == "surname":
            if person[1] == attr_value:
                target.append(person)
        elif attr_name == "group":
            if person[2] == attr_value:
                target.append(person)
        elif attr_name == "course":
            if person[3] == attr_value:
                target.append(person)
        elif attr_name == "role":
            if person[4] == attr_value:
                target.append(person)

    return target


print(search_person_by_attr_in_list("name", "Aleksandr"))
print(search_person_by_attr_in_list("group", "АСУ8-23-1мз"))
print(search_person_by_attr_in_list("surname", "Petuhov"))

"""Задание 2:

Выбрать персонажа, перебрав всех циклом в словаре

"""

personsDict = {
    "1": {"name": "Aleksandr", "surname": "Meresii", "group": "АСУ4-23-1мз",
          "course": 1, "role": "group leader"},
    "2": {"name": "Petr", "surname": "Ivanov", "group": "АСУ4-23-1мз",
          "course": 1, "role": "student"},
    "3": {"name": "Ivan", "surname": "Semenov", "group": "АСУ4-22-1мз",
          "course": 1, "role": "student"},
    "4": {"name": "Sergei", "surname": "Petrov", "group": "АСУ4-21-1мз",
          "course": 3, "role": "student"},
    "5": {"name": "Elena", "surname": "Popova", "group": "АСУ4-21-1мз",
          "course": 3, "role": "group leader"},
    "6": {"name": "John", "surname": "Doe", "group": "АСУ8-23-1мз",
          "course": 1, "role": "student"},
    "7": {"name": "Maria", "surname": "Utkina", "group": "АСУ8-23-1мз",
          "course": 1, "role": "group leader"},
}


def search_person_by_attr_in_dict(attr_name, attr_value):
    target = {}

    for identifier, person in personsDict.items():
        if person[attr_name] == attr_value:
            target[identifier] = person

    return target


print(search_person_by_attr_in_dict("name", "Elena"))
print(search_person_by_attr_in_dict("group", "АСУ4-23-1мз"))
print(search_person_by_attr_in_dict("surname", "Gagarin"))

"""Задание 3:

Сделать запрос данных от пользователя

"""

searchAttr = input("Введите аттрибут по которому будем искать человека?: ")
searchAttrValue = input("Введите значение аттрибута которое ищем?: ")

print(search_person_by_attr_in_list(searchAttr, searchAttrValue))
print(search_person_by_attr_in_dict(searchAttr, searchAttrValue))
