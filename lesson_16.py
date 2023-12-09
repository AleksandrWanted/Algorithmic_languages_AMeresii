class Person:
    def checkin(self, address):
        address.move_in(self)

    def __init__(self, a_name):
        self._name = a_name


class Male(Person):
    def __repr__(self):
        return "♂(%s)" % self._name


class Female(Person):
    def __repr__(self):
        return "♀(%s)" % self._name


class Address:
    __tenants = []  # делаем «скрытым»

    def move_in(self, person):  # собственно метод заселения
        if len(self.__tenants) < 2:
            self.__tenants += [person]
        else:
            raise ValueError('too many people!')

    def is_occupied(self):
        return len(self.__tenants) > 0

    def people(self):
        return self.__tenants


if __name__ == '__main__':
    a_person = Male("Вася")
    b_person = Female("Лена")
    c_person = Female("Катя")
    an_address = Address()
    a_person.checkin(an_address)
    print(1, an_address.is_occupied())
    print(2, an_address.people())
    b_person.checkin(an_address)
    print(3, an_address.is_occupied())
    print(4, an_address.people())
    c_person.checkin(an_address)
    print(4, an_address.people())  # третий - лишний?