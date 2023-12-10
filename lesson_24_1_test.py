import unittest
import names
import pytest
from lesson_17 import *

"""Задание 1:

Разработать тесты к своему проекту (lesson_24) на базе unittest.TestCase

"""


class TestBuyFilmTicket(unittest.TestCase):
    def test_buy_ticket_adult(self):
        a_person = Adult("Вася")
        a_film = Film('horror')
        b_person = Adult(names.get_first_name())
        b_film = Film('comedy')

        self.assertIsNone(a_person.buy_ticket(a_film))
        self.assertEquals(a_person._has_ticket, 1)
        self.assertIn(a_person, a_film.visitors)
        self.assertRaises(PersonAlreadyHasTicket, a_person.buy_ticket, b_film)
        self.assertNotIn(Adult(names.get_first_name()), a_film.visitors)

        while len(a_film.visitors) < 8:
            a_film.visitors += [names.get_first_name()]

        self.assertRaises(TooManyPeopleException, b_person.buy_ticket, a_film)
        self.assertEquals(len(a_film.visitors), 8)
        self.assertIsNone(b_person.buy_ticket(b_film))
        self.assertEquals(len(b_film.visitors), 1)
        self.assertTrue(a_film.is_occupied())
        self.assertFalse(b_film.is_occupied())

    def test_buy_ticket_children(self):
        a_person = Children("Света")
        a_film = Film('horror')
        b_person = Adult(names.get_first_name())
        b_film = Film('comedy')

        self.assertRaises(FilmGenreException, a_person.buy_ticket, a_film)
        self.assertNotIn(a_person, a_film.visitors)
        self.assertEquals(a_person._has_ticket, 0)
        self.assertIsNone(a_person.buy_ticket(b_film))
        self.assertEquals(a_person._has_ticket, 1)
        self.assertIn(a_person, b_film.visitors)
        self.assertIsNone(b_person.buy_ticket(b_film))

