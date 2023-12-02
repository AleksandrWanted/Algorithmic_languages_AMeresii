import string

"""Задание 1:

Оформить функцией поиск в списке
см. файл lesson_3.py, функция search_person_by_attr_in_list

"""

"""Задание 2:

Оформить функцией поиск в словаре
см. файл lesson_3.py, функция search_person_by_attr_in_dict

"""

"""Задание 3:

Сделать нечеткое сравнение элементов
Считаем что сравнивать необходимо элементы из списка и словаря persons

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


def compare_elements(elm1, elm2):
    if type(elm1) == type(elm2) and type(elm1) == list:
        main_elm = []
        secondary_elm = []

        if len(elm1) >= len(elm2):
            main_elm = elm1
            secondary_elm = elm2
        elif len(elm2) >= len(elm1):
            main_elm = elm2
            secondary_elm = elm1

        total = 0
        for p in range(len(secondary_elm)):
            if type(main_elm[p]) == type(secondary_elm[p]):
                if type(main_elm[p]) == string:
                    total += compare_str(main_elm[p], secondary_elm[p])
                else:
                    if main_elm[p] == secondary_elm[p]:
                        total += 1

        return total / len(main_elm)

    if type(elm1) == type(elm2) and type(elm1) == dict:
        main_elm = {}
        secondary_elm = {}

        if len(elm1) >= len(elm2):
            main_elm = elm1
            secondary_elm = elm2
        elif len(elm2) >= len(elm1):
            main_elm = elm2
            secondary_elm = elm1

        total = 0
        for p in secondary_elm.keys():
            if main_elm.__contains__(p):
                if type(main_elm[p]) == type(secondary_elm[p]):
                    if type(main_elm[p]) == string:
                        total += compare_str(main_elm[p], secondary_elm[p])
                    else:
                        if main_elm[p] == secondary_elm[p]:
                            total += 1

        return total / len(main_elm)


def compare_str(s1, s2):
    main_str = ""
    secondary_str = ""

    if len(s1) >= len(s2):
        main_str = s1
        secondary_str = s2
    elif len(s2) >= len(s1):
        main_str = s2
        secondary_str = s1

    counter = 0
    for i in range(len(secondary_str)):
        if main_str[i] == secondary_str[i]:
            counter += 1

    return counter / len(main_str)


print(compare_elements(personsList[0], personsList[0]))
print(compare_elements(personsList[3], personsList[4]))

print(compare_elements(personsDict["1"], personsDict["1"]))
print(compare_elements(personsDict["4"], personsDict["5"]))
