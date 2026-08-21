n1=int(input("enter First number:"))
n2=int(input("enter Second number:"))
n3=int(input("enter Third number:"))
if n1>n2 and n1>n3:
    print("Biggest number is:",n1)
elif n2>n3:
    print("Biggest number is:",n2)
else:
    print("Biggest number is:",n3)