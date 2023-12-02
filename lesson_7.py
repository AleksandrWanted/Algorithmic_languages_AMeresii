from pprint import pprint
from itertools import product
from utils import compare, int_val, remove_symbols

"""
Задание 1:
Добавить вывод неподходящих запросов и отладки

Задание 2:
Найти ошибку в коде

Задание 3:
Сделать аналогично для ФИО и адреса, разбитых на поля

"""

ADDRESS_WORDS = {'дом', 'д', 'улица', 'улице', 'ул', 'квартира', 'кв', 'живет'}
NAME_WORDS = {'имя', 'зовут', 'фамилия', 'отчество'}
AGE_WORDS = {'старше', 'младше', 'возраст'}

SURNAME_WORDS = {'фамилия'}
FIRST_NAME_WORDS = {'имя'}
SECOND_NAME_WORDS = {'отчество'}

HOUSE_WORDS = {'дом', 'д'}
STREET_WORDS = {'улица', 'улице' 'ул'}
ROOM_WORDS = {'квартира', 'кв'}


class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)

    def fuzzy_compare(self, query):
        query = remove_symbols(query)
        query_words_set = set(query.split())
        score = 0
        for m, f in zip(
                [ADDRESS_WORDS, NAME_WORDS, AGE_WORDS],
                [self.by_address, self.by_name, self.by_age]
        ):
            if m & query_words_set:
                score += f(query_words_set)

        return score > 0.51

    def by_address(self, Q):

        for q in Q:
            if q in STREET_WORDS:
                score = self.by_street(Q)
                return score > 0.51

            elif q in HOUSE_WORDS:
                score = self.by_house(Q)
                return score > 0.51

            elif q in ROOM_WORDS:
                score = self.by_room(Q)
                return score > 0.51

            elif q in ADDRESS_WORDS:
                score = self.by_street(Q)
                return score > 0.51

    def by_age(self, Q):
        q_age = max([int_val(q) for q in Q])

        if 'старше' in Q:
            if q_age < self.age:
                return 1.0
            else:
                return 0
        if 'младше' in Q:
            if q_age > self.age:
                return 1.0
            else:
                return 0
        if 'возраст' in Q:
            if q_age == self.age:
                return 1.0
            else:
                return 0

        return 0

    def by_name(self, Q):
        for q in Q:
            if q in SURNAME_WORDS:
                score = self.by_surname(Q)
                return score > 0.51

            elif q in FIRST_NAME_WORDS:
                score = self.by_first_name(Q)
                return score > 0.51

            elif q in SECOND_NAME_WORDS:
                score = self.by_second_name(Q)
                return score > 0.51

            elif q in NAME_WORDS:
                score = self.by_first_name(Q)
                return score > 0.51

    def by_surname(self, Q):
        Q = Q - SURNAME_WORDS
        W = self.name.split()
        W = [W[0]]

        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a, b), a, b)]
        return max(rez)[0]

    def by_first_name(self, Q):
        Q = Q - FIRST_NAME_WORDS
        W = self.name.split()
        W = [W[1]]

        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a, b), a, b)]
        return max(rez)[0]

    def by_second_name(self, Q):
        Q = Q - SECOND_NAME_WORDS
        W = self.name.split()
        W = [W[2]]

        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a, b), a, b)]
        return max(rez)[0]

    def by_street(self, Q):
        Q = Q - STREET_WORDS
        W = self.address.split()
        W = [W[0]]

        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a, b), a, b)]
        return max(rez)[0]

    def by_house(self, Q):
        Q = Q - HOUSE_WORDS
        W = self.address.split()
        W = [W[1]]

        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a, b), a, b)]
        return max(rez)[0]

    def by_room(self, Q):
        Q = Q - ROOM_WORDS
        W = self.address.split()

        int_W = int_val(W[2])

        if int_W > 0:
            for q in Q:
                if (int_val(q) > 0) and (int_W == int_val(q)):
                    return 1
                else:
                    return 0

        else:
            W = [W[2]]
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]
            return max(rez)[0]

    def __eq__(self, obj):
        if type(obj) == Person:
            return

        elif type(obj) == str:
            Q = set(obj.split())
            for q in Q:
                if q in ADDRESS_WORDS:
                    score = self.by_address(Q)
                    return score > 0.51

                elif q in NAME_WORDS:
                    score = self.by_name(Q)
                    return score > 0.51

                elif q in AGE_WORDS:
                    score = self.by_age(Q)
                    return score > 0.51

        else:
            return print("Введенное значение с типом [%s] не распознано,"
                         " попробуйте еще" % type(obj))

    def __repr__(self):
        return "Person('%s',%s,'%s')" % (self.name, self.age, self.address)


if __name__ == '__main__':
    lena = Person("Петрова Елена Сергеевна", 30, "Пушкина, 14, 115")
    oleg = Person("Чижиков Олег Иванович", 34, "Ленского, 10, 11")
    olga = Person("Бузова Ольга Михайловна", 28, "Онегина, 11, 12")
    nata = Person("Ростова Наташа Михайловна", 17, "Ростова, 16, 15")

    quares = [
        'имя Ольга',
        'фамилия Ростова',
        'отчество Михайловна',
        'зовут нташа'
        'возраст 30',
        'старше 20',
        'младше 20',
        30,
        'живет на Пушкина',
        'живет на улице Онегина',
        'дом 10',
        'квартира 15',
        None,
        "Ольга"
    ]

    people = {
        lena.key: lena,
        oleg.key: oleg,
        olga.key: olga,
        nata.key: nata
    }

    for query, person in product(quares, people.values()):

        if person == query:
            print(query, person)
