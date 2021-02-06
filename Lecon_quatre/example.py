import time


def time_decorator(method):
    """
    Функция - декоратор, в которую оборачиваются методы класса
    :param method: метод декорируемого класса
    :return:
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = method(*args, **kwargs)
        end = time.time()
        print(
            f"\nВремя выполнения метода {method.__name__} {end - start} "
            f"секунд"
        )
        return return_value
    return wrapper


def timeit_all_methods(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            attr = self._obj.__getattribute__(s)
            if isinstance(attr, type(self.__init__)):
                return time_decorator(attr)
            else:
                return attr
    return NewCls


@timeit_all_methods
class Test:
    def method_1(self):
        print('slow method start')
        time.sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        time.sleep(0.1)
        print('fast method finish')


t = Test()

t.method_1()
t.method_2()
