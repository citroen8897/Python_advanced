class AttrSquare:
    def __init__(self, start):
        self.start = start

    def __getattr__(self, attr):
        if attr == 'X':
            return self.start ** 2
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = value
        self.__dict__[attr] = value


A = AttrSquare(3)
B = AttrSquare(32)

print(A.X)
print(B.X)
print(B.Y)
