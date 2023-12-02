"""Задание 1:

Опишите себя используя список

"""

personList = [
    ["surname", "Meresii"],
    ["name", "Aleksandr"],
    ["age", 30],
    ["birthdate", "21.09.1993"],
    ["passport", "89 78 567892"],
    ["address", "Perm, Lenina street, 44-88"],
    ["group", "АСУ4-23-1мз"],
    ["course", 1],
    ["role", "group leader"]
]

print(personList)

"""Задание 2:

Опишите себя используя словарь

"""

personDict = {
    "fullName": {"name": "Aleksandr", "surname": "Meresii"},
    "age": {"yearsOld": 30, "dayBirth": 21, "monthBirth": 9, "yearBirth": 1993},
    "passport": {"series": "89 78", "number": "567892", "issueDate": "23.04.2017"},
    "studyDate": {"group": "АСУ4-23-1мз", "course": 1, "role": "group leader"}
}

print(personDict)

"""Задание 3:

Обьясните какое описание удобнее с точки зрения обработки информации и почему

С точки зрения обработки информации удобнее описание в виде словаря так как 
информация структурирована, доступ к ней проще, возможен поиск и изменение 
значения по ключу, который не привязан к индексу.

Пример Список:
Мы должны знать какому индексу соответствуют те или иные данные, либо
изобретать костыльные решения, например как в данном примере, где
первое значение из словаря является условным ключем

"""

print("Пример list:\n", "ФИО:", personList[0][1], personList[1][1])
print(" Группа:", personList[6][1])
print(" Курс обучения:", personList[7][1])
personList[7][1] = 2
print(" Курс обучения на который перейду:", personList[7][1])

# Пример Словарь:

print("Пример dict:\n", "ФИО:", personDict["fullName"])
print(" Группа:", personDict["studyDate"]["group"])
print(" Курс обучения:", personDict["studyDate"]["course"])
personDict["studyDate"]["course"] = 2
print(" Курс обучения на который перейду:", personDict["studyDate"]["course"])
