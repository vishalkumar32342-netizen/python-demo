#Types of inheritnce
#_1.Single inhertance
class P:
    def m1(self):
        print('Parent method')
class C(P):
    def m2(self):
        print('class method')

c=C()
c.m1()
c.m2()

#__2.Multilevel inheritance
class P:
    def m1(self):
        print('class method')
class C(P):
    def m2(self):
        print('child method')
class CC(C):
    def m3(self):
     print('sub child method')
c=CC()
c.m1()
c.m2()
c.m3()

#__3.Hierarchical Inheritance
#__single class multiple child classes.
class P:
    def m1(self):
        print('class method')
class C1(P):
    def m2(self):
        print('child method')
class C2(P):
    def m3(self):
        print('sub chile method')

# c1=C1()
# c1.m1()
# c1.m2()
c1=C2()
c1.m1()
c1.m3()

#_4.Multiple inheritance:
#multiple parent class but sinngle child class.
class P1:
    def m1(self):
        print('p1 method')
class P2():
    def m1(self):
        print('P2 method')
class C(P1,P2):
    def m3(self):
        print('child method')
c=C()
c.m1()

c.m3()

#_5.Hybrid Inheritance
#If we take More than one type of inheritance is called hybrid inheritance.
class A:pass
    # def m1(self):
    #     print('A class method')
class B:
    def m1(self):
        print('B class method')
class C:
    def m1(self):
        print('C class method')
class X(A,B):pass
    # def m1(self):
    #     print('X class method')
class Y(B,C):
    def m1(self):
        print('Y class method')
class P(X,Y,C):pass
    # def m1(self):
    #     print('P class method ')
p=P()
p.m1()
 


#_6.Cyclic inheritance. --- not required
# #class A(A):
#     pass     not support cyclic inheritance


#__Method resolution order____
#(class.mro())


