import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)

        return Singleton._instance


def task():
    s = Singleton()
    print(id(s))


for i in range(10):
    ti = threading.Thread(target=task)
    ti.start()
