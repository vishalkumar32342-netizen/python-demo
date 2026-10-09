# class Test:
#     a=10
#     def __init__(self):
#         Test.b=20

#     def m1(self):
#         Test.c=30
       
#     @classmethod
#     def m2(cls):
#         Test.d=50
#         cls.e=60

#     @staticmethod
#     def m3():
#         Test.f=70

# t=Test()
# t.m1()
# Test.m2()
# Test.m3()
# Test.g=80

# print(Test.__dict__)

# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks

#     def display(self):
#         print("Student name is: {}\nRollno is:{}\nMarks is:{}".format(self.name,self.rollno,self.marks))

# s1=Student("vishal",101,89)
# s1.display()

#  Write a Python program to create a Student class and Creates an object to it. Call the 
# method talk() to display student details

class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print("Hello My name is:",self.name)
        print("My roll no is:",self.rollno)
        print("My marks is:",self.marks)

s1=Student("Vishal",101,78)
s1.talk()

# Program to demonistrate constructor will execute only once per object: 
# class Test:
#     def __init__(self):
#         print("Constructor execution.....")

#     def m1(self):
#         print("Method Execution...")
# t1=Test()
# t2=Test()
# t3=Test()
# t3.m1()

# class Student():

#     '''This is student class with required data...'''
#     def __init__(self,x,y,z):
#         self.name=x
#         self.rollno=y
#         self.marks=z

#     def display(self):
#         print("Student Name:{}\nRollNo:{}\nMarks:{}".format(self.name,self.rollno,self.marks))

# s1=Student("Vishal",1,90)
# s1.display()
# s2=Student("Rohit",2,89)
# s2.display()


class Employee():

    def __init__(self):
        self.eno=100
        self.ename='Vishal'
        self.esal=100000

e=Employee()
print(e.__dict__)


class Test():

    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30
t=Test()
t.m1()
t.d=40
t.e=50
print(t.__dict__)

#How to access Instance Variable and delete
class Test():
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

    def m1(self):
        del self.d

t=Test()
t1=Test()
t.m1()
print(t.__dict__)
print(t1.__dict__)

#Instance Variable vs Static Variable:

class Test:
    x=10
    def __init__(self):
        self.y=20

t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
# Test.x=100
# Test.y=30
# t1.y=999
# print('t1:',t1.x,t1.y)
# print('t2:',t2.x,t2.y)
Test.x=30
t2.y=40
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)


# Various places to declare static variables: 
class Test:
    a=10
    def __init__(self):
        Test.b=20
    def m1(self):
        Test.c=30

    def m2(self):
        Test.d=40

    @classmethod
    def m3(cls):
        cls.e1=40
        Test.e2=50
    @staticmethod
    def m4():
        Test.f=60
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.m4()
print(Test.__dict__)
Test.g=70
print(Test.__dict__)

#How to access static variable
class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print(Test.a)
t=Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()


#####
class Test:
    a=666
    @classmethod
    def m1(cls):
        cls.a=777
    @staticmethod
    def m2():
        Test.a=888
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)

######
class Test:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999
t1=Test()
t2=Test()
t1.m1()
print(t1.a,t1.b)
print(t2.a,t2.b)
print(Test.a,Test.b)