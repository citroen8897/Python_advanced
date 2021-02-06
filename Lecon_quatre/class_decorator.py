import time


class Functor:
    def __init__(self, n):
        self.n = n

    def time_decorator(method, t):
        def wrapper(*args, **kwargs):
            start = time.time()
            return_value = method(*args, **kwargs)
            end = time.time()
            print(
                f"Время выполнения метода {method.__name__} {end - start} "
                f"секунд"
            )
            if end - start > t:
                print(f'ВНИМАНИЕ! {method.__name__} медленный...')
            return return_value
        return wrapper

    def __call__(self, cls):
        t = self.n

        class NewCls:
            def __init__(self, *args, **kwargs):
                self.t = t
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
                    return Functor.time_decorator(attr, t)
                else:
                    return attr
        return NewCls


@Functor(0.45)
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
