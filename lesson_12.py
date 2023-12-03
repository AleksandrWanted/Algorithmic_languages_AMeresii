import random

"""Задание 1:

В терминах ООП описать предметную область,
которую вы ранее описали словарем

"""


class People:
    def __init__(self, full_name, gender, age):
        self.full_name, self.gender, self.age = full_name, gender, age
        self.key = (full_name, age)

    def say_yours_name(self):
        print("%s: Привет! Меня зовут %s" % (self.full_name, self.full_name))

    def go_sleep(self):
        if self.gender == "мужской":
            print("%s: Ушел спать" % self.full_name)
        elif self.gender == "женский":
            print("%s: Ушла спать" % self.full_name)
        else:
            print("%s: Ушел(а) спать" % self.full_name)

    def buy_beer(self):
        if self.age < 18:
            print("%s: Не могу купить пиво, мне еще нет 18 лет" % self.full_name)
        else:
            print("%s: Пойду куплю пиво" % self.full_name)


class Student(People):
    def __init__(self, full_name, gender, age, university, group, course, role):
        People.__init__(self, full_name, gender, age)
        self.university, self.group, self.course, self.role = university, group, course, role

    def say_your_study_place(self):
        print("%s: Я учусь в %s на %s курсе в группе %s" % (self.full_name, self.university, self.course, self.group))

    def pass_exam(self, subject):
        grade = random.randrange(3, 5)
        print("%s: Экзамен по предмету %s сдан на оценку %s" % (self.full_name, subject, grade))


class Employee(People):
    def __init__(self, full_name, gender, age, company, department, project, specialization, position):
        People.__init__(self, full_name, gender, age)
        self.company, self.department = company, department
        self.project, self.specialization, self.position = project, specialization, position

    def say_your_place_of_work(self):
        print("%s: Я работаю в компании %s, в департаменте %s, на проекте %s, в должности %s. Моя специализация %s"
              % (self.full_name, self.company, self.department, self.project, self.position, self.specialization))

    def take_vacation(self, duration):
        print("%s: Я взял(а) отпуск на %s дней" % (self.full_name, duration))


lenaPeople = People("Пупкова Елена Михайловна", "женский", 16)
olegPeople = People("Николаев Олег Петрович", "мужской", 18)

fedorStudent = Student("Иванов Федор Григорьевич", "мужской", 25,
                       "ПНИПУ", "АСУ4-22-1мз", 2, "студент")
mashaStudent = Student("Третьякова Мария Александровна", "женский", 17
                       , "ПНИПУ", "АСУ4-23-1б", 1, "староста")

kirillEmployee = Employee("Федоров Кирилл Петрович", "мужской", 29, "МТС Диджитал",
                          "Рекламные технологии", "Омниканальная платформа", "Разработка ПО",
                          "Go разработчик")
aleksandrEmployee = Employee("Сидоров Александр Владимирович", "мужской", 40, "Постгресс профессиональный",
                             "Облачные технологии", "DBaaS", "Менеджмент",
                             "Технический руководитель")

"""Задание 2:

Придумать по 2-3 действия каждому представителю

"""

lenaPeople.say_yours_name()
olegPeople.go_sleep()
olegPeople.buy_beer()
lenaPeople.buy_beer()

fedorStudent.say_your_study_place()
mashaStudent.pass_exam("алгоритмические языки")

kirillEmployee.say_your_place_of_work()
aleksandrEmployee.take_vacation(14)

"""Задание 3:

Обосновать почему именно такая структура выбрана и такие имена даны

"""

"""

Выбрана иерарция Человек (People) -> Студент (Student) -> Сотрудник (Employee).
Такая структура выбрана основываясь на логической связанности описаемых классов и наличии общих атрибутов, таких
как full_name, gender, age, и общим методах say_yours_name, go_sleep, buy_beer. Студент и сотрудник являются людьми,
поэтому логично что они имеют такие же аттрибуты и методы как объект класса человек. Но вот сотрудник и студент
могут не иметь общих атрибутов и методов, да и к тому же сотрудник может не быть студентом, и наоборот.
Класс People является родительским для классов Student и Employee. Классы Student и Employee детализируют класс
People в своем направлении (работа, учеба), добавляя в объект спецефичные атрибуты и методы.

"""
