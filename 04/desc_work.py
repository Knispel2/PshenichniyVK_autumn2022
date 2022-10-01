class Integer:

    def __get__(self, inst, owner):
        return self.num

    def __set__(self, inst, value):
        if isinstance(value, int):
            self.num = value
        else:
            raise ValueError('It is not int!')


class String:

    def __get__(self, inst, owner):
        return self.name

    def __set__(self, inst, value):
        if isinstance(value, str):
            self.name = value
        else:
            raise ValueError('It is not string!')


class PositiveInteger:

    def __get__(self, inst, owner):
        return self.price

    def __set__(self, inst, value):
        if isinstance(value, int) and value >= 0:
            self.price = value
        else:
            raise ValueError('It is not positive int!')


class Data:

    def __init__(self, num=0, name='', price=0):
        self.num = num
        self.name = name
        self.price = price

    num = Integer()
    name = String()
    price = PositiveInteger()
