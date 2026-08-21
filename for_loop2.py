# #Print numbers from 1 to 10 using a for loop.
for x in range(11):
     print(x)

# #Print numbers from 10 to 1 using a for loop.
for x in range(10,0,-1):
     print(x)

#Print all even numbers from 1 to 20.
for x in range(1,21):
    if x % 2 ==0:
        print(x)

#Print all odd numbers from 1 to 20.
for x in range(21):
     if(x%2!=0):
          print(x)

#Print the multiplication table of 5:
for x in range(1,11):
     print(5*x)

#Print the multiplication table of 9:
for x in range(1,11):
     print(9*x)

#Enter any number multiplication
n=int(input("Enter any number:"))
for i in range(1,11):
     print(n*i)

#Enter any number multiplication and output in list
n=int(input("Enter any number:"))
table=[]

for i in range(1,11):
     table.append(n*i)
print(table)

#Find the sum of numbers from 1 to 100 using a for loop.

total=0

for i in range(1,101):
     total=total+i

print(total)

#Find Factorial of n numbers:
n=int(input("Enter a number:"))

factorial=1

for i in range(1 , n+1):
     factorial=factorial*i

print(n ,"! =",factorial)

#Count how many numbers between 1 and 100 are divisible by 2.
count=0

for i in range(1,101):
     if i%2==0:
          count=count+1

print(count)