class tst():
    '''
        will not tab any attribute begin with _
        >>> t = tst()
        >>> t.u
        >>> dir(t)
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_u', 'u']
    '''
    def __init__(self):
        self._u = 100
        self.u = 200


