# Interface in  Python
#____Interface is an abstract class which contains only abstract methods.
#abstract class can contain both abstract and concrete methods but interface contains only abstract methods.


from abc import *
class Interface(ABC):
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m2(self):pass
    @abstractmethod
    def m3(self):pass

#inerface vs abstract class vs concrete class:
# ______________________________________________
#1.if we dont know anything about implementation just we have requirement specification (SRS) then we should go for intrface.

#2.If we etalking about implementation but not completely (partial implementation) then we should go for abstact class.

#3.If we talking about implementation completely and ready to provide service then we should go for concrete class.

from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):pass

    @abstractmethod
    def disconnect(self):pass

class Oracle(DBInterface):
    def connect(self):
        print('connecting to the  oracle database')

    def disconnect(self):
        print('disconnecting from oracle databases')

class MySql(DBInterface):
    def connect(self):
        print('connecting to MySql database')

    def disconnect(self):
        print('disconnecting form MySql databases')

o=MySql()
o.connect()
o.disconnect()


#__Public, private and protected members:
# _________________________________________
# x=10---public
# _x=10---protected variable
#         but outside of the class only in child classes.
# __x=10  private members
#         we cant access outside of the class.but there is a special way print(t._Test__y)--for object related  and print(Test._Test__x)---for class related.

