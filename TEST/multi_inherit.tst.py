# https://www.cnblogs.com/yuanrenxue/p/10750624.html
# https://www.cnblogs.com/anovana/p/8143064.html


class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Lef Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subcalss")
        self.num_sub_calls += 1


son = Subclass()
mros = eotl.get_mros(son)

>>> parr(mros)
<__main__.Subclass object at 0x7fa8ab6b9e48>
<class '__main__.Subclass'>
<class '__main__.LeftSubclass'>
<class '__main__.RightSubclass'>
<class '__main__.BaseClass'>
<class 'object'>
>>>




class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Lef Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subcalss")
        self.num_sub_calls += 1


>>> son = Subclass()
>>> parr(eotl.get_mros(son))
<__main__.Subclass object at 0x7fa8ab4890b8>
<class '__main__.Subclass'>
<class '__main__.LeftSubclass'>
<class '__main__.RightSubclass'>
<class '__main__.BaseClass'>
<class 'object'>
>>>

>>> son.call_me()
Calling method on Base Class
Calling method on Right Subclass
Calling method on Lef Subclass
Calling method on Subcalss
>>>

