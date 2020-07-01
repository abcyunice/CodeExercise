class Person:
    pass


class Male(Person):
    def __init__(self):
        self.sex = "m"


class Female(Person):
    def __init__(self):
        self.sex = "f"


class Factory():
    def getperson(self, sex):
        if sex == "f":
            return Female()

        if sex == "m":
            return Male()

        raise Exception("sex = f or m !")


f = Factory()
p1 = f.getperson("f")
print(p1.sex)
