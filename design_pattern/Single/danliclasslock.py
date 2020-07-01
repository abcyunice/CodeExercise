import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        import time
        time.sleep(1)

    @classmethod
    def instance(cls):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton()
        return Singleton._instance


def task():
    s = Singleton.instance()
    print(s)


for i in range(10):
    ti = threading.Thread(target=task)
    ti.start()
