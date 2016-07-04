class B:
    pass


class Meta(type):

    def __new__(cls, name, bases, attr):
        print('in 1...')
        print(cls)
        print(name)
        print(bases)
        name = "cambio_" + name
        bases = (B, )
        attr['new'] = 1
        return super().__new__(cls, name, bases, attr)

    def __init__(cls, name, bases, attr):
        print('in 2...')
        print(cls)
        print('name: ', name)
        print('bases: ', bases)
        print('attr: ', attr)
        print(cls.__name__)
        return super().__init__(name, bases, attr)

if __name__ == '__main__':

    class A(metaclass=Meta):
        pass

    print(A.__mro__)

# Output:

# >> in 1...
# >> <class '__main__.Meta'>
# >> A
# >> ()
# >> in 2...
# >> <class '__main__.A'>
# >> name:  A
# >> bases:  ()
# >> attr:  {'__module__': '__main__', 'new': 1, '__qualname__': 'A'}
# >> cambio_A
# >> (<class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
