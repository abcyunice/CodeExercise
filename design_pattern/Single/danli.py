def singleton(cls):
    _instance = {}

    def single_(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single_


@singleton
class A(object):
    def __init__(self, A):
        self.A = A


a = A(1)
b = A(2)

print(id(a), id(b))
