from itertools import product
from sys import stderr
from utils import compare

"""Задание 1:

Описать иерархию классов своего проекта. Внутри классов комментарием указать
что он должен уметь

"""

"""Задание 2:

Написать текст к приложению. 3-5 предложений

Ответ: Приложение по продаже билетов в кино на различные фильмы.
Согласно условию, билеты продаются людям 
при условии наличия свободных мест в зале (вместимость зала 8 мест) и 
отсутствия у человека билелетов на другой фильм.
На фильмы некоторых жанров, в данном примере ужасы, допускаются только взрослые.

"""

"""Задание 3:

Описать исключения к проекту

"""

"""

FilmException основной класс исключений, показывающий что произошло исключение 
при попытке купить билет на фильм

"""


class FilmException(Exception):
    pass


"""

TooManyPeopleException дочерний класс исключений фильма, показывающий
что произошло исключение в связи с тем что зал заполнен

"""


class TooManyPeopleException(FilmException):
    pass


"""

FilmGenreException дочерний класс исключений фильма, показывающий
что произошло исключение в связи с тем что дети не допускаются на
некоторые жанры фильмов (ужасы)

"""


class FilmGenreException(FilmException):
    pass


"""

PersonAlreadyHasTicket дочерний класс исключений фильма, показывающий
что произошло исключение в связи с у человека приобреден билет на другой фильм

"""


class PersonAlreadyHasTicket(FilmException):
    pass


class Person:
    def __init__(self, a_name):
        self.name = a_name
        self.film = None
        self._has_ticket = 0

    # покупка билета на фильм
    def buy_ticket(self, film):
        if not self._has_ticket:
            film.occupy_place(self)
            self._has_ticket = 1
        else:
            raise PersonAlreadyHasTicket()

    # проверка возможности купить билет
    def can_buy_ticket(self, other, film):
        if len(other) >= 8:
            raise TooManyPeopleException()


class Adult(Person):
    def __repr__(self):
        return "adult(%s)" % self.name


class Children(Person):
    def __repr__(self):
        return "children(%s)" % self.name

    # проверка возможности купить билет
    def can_buy_ticket(self, other, film):
        super().can_buy_ticket(other, film)
        try:
            if type(self) == Children and compare(film.genre, "horror") > 0.6:
                raise FilmGenreException()
        except IndexError:
            pass


class Film:
    def __init__(self, genre):
        self.visitors = []
        self.genre = genre

    # занять место в зале
    def occupy_place(self, person):
        try:
            person.can_buy_ticket(self.visitors, self)
            self.visitors += [person]
        except Exception as e:
            raise e

    # узнать заполнен ли зал?
    def is_occupied(self):
        return len(self.visitors) >= 8

    # вернуть список зрителей фильма
    def return_film_visitors(self):
        return self.visitors


if __name__ == '__main__':
    films = (Film('horror'), Film('comedy'))
    persons = (Adult("Вася"),
               Adult("Паша"),
               Children("Лена"),
               Adult("Катя"),
               Children('Семен'),
               Adult('Миша'),
               Adult('Сергей'),
               Adult('Оля'),
               Adult('Света'),
               Adult('Максим'),
               Adult('Денис'))

    for film, person in product(films, persons):
        try:
            person.buy_ticket(film)
            print("%s [%s] купил(а) билет на фильм %s" % (person.name, type(person), film.genre))
        except Exception as e:
            print(type(e), person, film.genre, file=stderr)

    print("Зал где показывают фильм %s заполнен? [%s]" % (films[0].genre, films[0].is_occupied()))
    print("Список зрителей [%s]: %s" % (films[0].genre, films[0].visitors))

    print("Зал где показывают фильм %s заполнен? [%s]" % (films[1].genre, films[1].is_occupied()))
    print("Список зрителей [%s]: %s" % (films[1].genre, films[1].visitors))
