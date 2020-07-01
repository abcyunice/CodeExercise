import threading


class Single(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Single._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = type(cls, *args, **kwargs)
                    # cls._instance = super(Single, cls).__call__(*args, **kwargs)
        return cls._instance


class ExampleClass(metaclass=Single):
    def __init__(self):
        import time
        time.sleep(1)


def task():
    a = ExampleClass()
    print(id(a))


for i in range(10):
    ti = threading.Thread(target=task)
    ti.start()
