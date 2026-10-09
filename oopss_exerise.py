import sys
class Customer:
    '''Customer class with bank operation'''
    bankname='SBI Bank'

    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
            self.balance=self.balance+amount
            print('The Balance after Deposit:',self.balance)

    def withdraw(self, amount):
            if amount > self.balance:
                print('Insufficient Balance....Cannot perform this operation')
                sys.exit()
            self.balance=self.balance-amount
            print('The balance after Withdraw:',self.balance)

print('Welcome to',Customer.bankname)
name=input('Enter your name:')
c=Customer(name)
while True:
    print('d-Deposit \nw-Withdraw \ne-Exit')
    option=input('Choose your Option:') .lower()
    if option=='d' :
        amount=float(input('Enter amount to deposit:'))
        c.deposit(amount)
    elif option=='w':
        while True:
            amount=float(input('Enter amount to withdraw:'))
            if not(amount>0 and amount%100==0):
                 print('Amount should be multiples of 100')
            else:
                 break
        c.withdraw(amount)
    elif option=='e':
        print('Thanks for Banking')
        sys.exit()
    else:
        print('Invalid option.....Please choose valid option')
