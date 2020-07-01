class Person:
    pass


class Male(Person):
    def __init__(self):
        self.sex = "m"


class Female(Person):
    def __init__(self):
        self.sex = "f"


class Factory():
    def getperson(self):
        pass


class FFactory(Factory):
    def getperson(self):
        return Female()


class MFactory(Factory):
    def getperson(self):
        return Male()


f = FFactory()
p1 = f.getperson()
print(p1.sex)
