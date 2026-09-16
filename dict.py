# word=input("Enter some word:")
# d={}
# for x in word:
#     d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print("{} occurred {} times".format(k,v))


# ###########
# word=input("enter some word:")
# vowels={"a","e","i","o","u"}
# d={}
# for x in word:
#     if x in vowels:
#         d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print("{} occurred {} times".format(k,v))



# n=int(input("Enter the number of students:"))
# d={}
# for i in range(n):
#     name=(input("Enter student name:"))
#     marks=int(input("Enter student marks:"))
#     d[name]=marks
# print(d)
# while True:
#     name=input("Enter student name to get marks:")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("student not found")
#     else:
#         print("The marks of {}:{}".format(name,marks))
#     option=input("Do you want to find another students marks[yes|No]:")
#     if option=="No":
#         break
#     print("Thank you for using our application")



#Dict comprehension
square={x:x*x for x in range(1,6)}
print(square)
doubles={x:2*x for x in range(1,6)}
print(doubles)