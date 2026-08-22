# To print numbers from 1 to 10 by using while loop 
x=1
while x<=10:
    print(x)
    x=x+1  

#To display the sum of first n numbers
n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum of First",n,"number is:",sum)

#write a program to prompt user to enter some name until entering Durga
name=""
while name!="vishal":
    name=input("Enter name:")
print("Thanks for confirmation")