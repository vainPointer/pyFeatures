class Student(object):
    __slots__ = ('_birth')

    def __init__(self):
        self._birth = 0

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


s = Student()
s.birth = 10
print(s.age)
