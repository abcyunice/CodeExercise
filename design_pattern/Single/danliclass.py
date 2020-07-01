class Singleton(object):
    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if hasattr(Singleton, "_instance"):
            return Singleton._instance
        Singleton._instance = Singleton()
        return Singleton._instance


for i in range(10):
    a = Singleton.instance()
    print(id(a))
