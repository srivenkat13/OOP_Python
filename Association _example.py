# two classes are said to associated if there is relation between classes without any rule
# be it aggregation , association and composition the object of one class is 'owned' by other class, this is the common point
# In composition they work together but, if one classes dissapears other will also sieze to exist
class A(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums(self):
        self.b + self.c


class B(object):
    def __init__(self, d, e):
        self.d = d
        self.e = e

    def addAllNums(self, Ab, Ac):
        x = self.d + self.e + Ab + Ac
        return x


first = A("Hi", 2, 3)
second = B(3, 4)

print(second.addAllNums(first.b , first.c))


# this example demonstrates association between two classes ( object is shared here)