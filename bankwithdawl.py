bal=10000
withdrawl=True

while withdrawl:

    amount=int(input("Enter amount to withdrawl:"))

    if amount<=bal:
        print("amount debited")
        bal=bal-amount
        print("Your current bal",bal)

    else:
        print("Insufficient bal")
        break
    choice=input("do you need to withdraw again:")
    if choice.lower()=="no":
        print("your current balance",bal)
        print("Thank you for using ATM services🥰")
        withdrawl=False