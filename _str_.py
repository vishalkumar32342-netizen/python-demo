class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __str__(self):
        return "This is the stdent details with name:{} and with Rollno: {}".format(self.name,self.rollno)
    
s=Student('vishal',100)
s2=Student('Ravi',101)
print(s)
print(s2)


#diff betn str()  vs repr()
#"__str__() provides a user-friendly string representation of an object,
#  while __repr__() provides a developer-oriented, more detailed representation mainly used for debugging."





# import datetime

# today=datetime.datetime.now()
# s=str(today)
# print(s)

import datetime
today=datetime.datetime.now()
s=repr(today)
print(s)
d=eval(s)
print(d)
print(type(d))


class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance=self.balance-amount
        else:
            print('sorry , Insuffucient funds')

    def print_statement(self):
        print('Account Balance:',self.balance)

class CurrentAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)

    def __str__(self):
        return "{} 's Current Account Balance:{}".format(self.name,self.balance)


class SavingAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)

    def __str__(self):
        return "{} 's Saving Account Balance:{}".format(self.name,self.balance)

c=CurrentAccount('Vishal',10000)
print(c)
c.deposit(10000)
print(c)
c.withdraw(20900)
print(c)
    