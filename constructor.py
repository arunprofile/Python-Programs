'''
Constructors are used to initializing the object’s state. 
The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.

self: self is the instance of a class, we can change the name of self if we want (self is preferred ).
'''

# A sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Sample Method
    def say_hi(self):
        print("Hello, my name is", self.name, "and age", self.age)

        # The self parameter allows access to the object's attributes and other methods within the class.

    def welcome(self):
        print("Welcome this world !!..",self.name)

p = Person('Arun', 5)
d = Person('Sachi', 4)
p.say_hi()
p.welcome()
d.say_hi()
d.welcome()