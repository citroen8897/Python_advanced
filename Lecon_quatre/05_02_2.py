class Functor:
    def __init__(self, n):
        self.n = n

    def call_1(self, func, *args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)

    def call_2(self, func, *args, **kwargs):
        func(*args, **kwargs)

    def __call__(self, func):
        def helper(*args, **kwargs):
            if self.n == 1:
                return self.call_1(func, *args, **kwargs)
            elif self.n == 2:
                return self.call_2(func, *args, **kwargs)
        return helper


@Functor(1)
class Test_1:
    def __init__(self, x):
        self.x = x

    def print_method(self):
        print(self.x ** 4)


t = Test_1(3)
t.print_method()
