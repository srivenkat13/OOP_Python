# Difference between class variable and instance varible
# Class variable can be accessed by any method of the class,
# but the instance variables are not
class Dog:
    """
    The dog class
    """

    kind = "Canine"  # class variable is shared by all
    count = 0  # class variable

    def __init__(self, name):
        self.name = name  # instance variable and is unique to each other
        Dog.count += 1

d = Dog("Sheero")
e = Dog("Mucho")

print(d.kind)   #shared by all dogs
print(e.kind)

print(d.name)      # unique to d and e
print(e.name)

print(d.count)     # shared by all
print(e.count)
