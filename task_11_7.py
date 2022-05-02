class ComplexNum:

    def prop(self, *args):
        self.num = complex(*args)

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


a = ComplexNum()
b = ComplexNum()
a.prop(4, 5)
b.prop('2+3j')
print(a + b)
print(a * b)
