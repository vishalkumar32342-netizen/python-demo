# Abstract method:-method not having proper implementation.
# how to declare ABSTRACT METHOS:-By using @abstractmethod decorator
# child class are responsible to provide implementation for parent class abstract methods

#Abstract class:--If implementaion of a class is not complete (partially implemented class)
#how to declare abstract class explicitly :--We have to extend ABC class 
# class Test(ABC):
    #  pass
#  Test is child class and ABC is parent class.Test class is extending ABC class.Hence it is abstract class.  
# ABC class is present in abc module
#Abstract class vs Abstract method
# Abstract class can contain any number of abstact methods including zero number also.
# Abstract class can contain normal methods also.

#____When an object creation is not possible:
# _If class is abstract and it contain atleast one abstrtact method then only instantiation is not possible.

# ____HOWEVER object creaation is possible in following ways:
# __1.Class is not abstract but contains one abstract method.
# __2.class is abstract but it does not contain any abstract method.

# from abc import *
# class Test:
#     @abstractmethod
#     def m1(self):
#         print('Hello')

# t=Test()
# t.m1()

from abc import *
class Vehicle(ABC):
    pass
    # @abstractmethod                it is compulsory
    # def get_no_of_wheels(self):
    #     pass

class Bus(Vehicle):
    def get_no_of_wheels(self):
        return 6

class Auto(Vehicle):
    def get_no_of_wheels(self):
        return 3
b=Bus()
print(b.get_no_of_wheels())

a=Auto()
print(a.get_no_of_wheels())



from abc import *
class P(ABC):
    @abstractmethod
    def m1(self):pass

    @abstractmethod
    def m2(self):pass

class C(P):
    def m1(self):
        print('m1 implementation')

class CC(C):
    def m2(self):
        print('m2 implementation')
c=CC()
c.m1()
c.m2()


#
from abc import *
class P(ABC):
    @abstractmethod
    def m1(self):
        pass

    def m2(self):
        print('m2 implementation')

class C(P):
    def m1(self):
        print('m1 implementation')

c=C()
c.m1()
c.m2()


