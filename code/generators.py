__author__ = 'aramu'


def generator_func(n):
    "this is generator_func"
    for i in range(1, n):
        yield i * i

class myclass:
    "this class is an example"
    def __init__(self, val1):
        self.my_value = val1
    def __next__(self):
        if self.my_value < 10:
            self.my_value += 2
            return self.my_value
        else:
            return 0
    def __str__(self):
        return str(self.my_value)
    def __iter__(self):
        return self

m1 = myclass(1)
print(m1)
print(generator_func.__doc__)
print(myclass.__doc__)
