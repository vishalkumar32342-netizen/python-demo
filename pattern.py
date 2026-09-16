# word=input("Enter some word:")
# if word==word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindromme")

#___* * * * * *
#___* * * * * *
# for i in range(1,3):
#     for j in range(1,3):
#         print("*",end=" ")
#     print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# * * * * * * *
# r=6
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# * * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * 
# * * * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# r=10
# for i in range(r,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 

# r=int(input("enter numbers:"))
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#           * 
#          ** 
#         *** 
#        **** 
#       ***** 
#      ****** 
#     ******* 
# n=int(input("Enter no of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-1),"*"*i,end="")
#     print()

# A A A A A A A A A A 
# B B B B B B B B B B 
# C C C C C C C C C C 
# D D D D D D D D D D 
# E E E E E E E E E E 
# F F F F F F F F F F 
# G G G G G G G G G G 
# H H H H H H H H H H 
# I I I I I I I I I I 
# J J J J J J J J J J

# n=int(input("Enter no.of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 

# n=int(input("Enter some rows:"))
# for i in range(1,n+1):
#     print("  "*(n-i),"* "*(2*i-1))



#          1 
#        2 2 2 
#      3 3 3 3 3 
#    4 4 4 4 4 4 4 
#  5 5 5 5 5 5 5 5 5 

# n=int(input("Enter the number of rows: "))   
# for i in range(1,n+1):   
#    print("  "*(n-i),(str(i)+" ")*(2*i-1))  


# 4 
# 3 4 
# 2 3 4 
# 1 2 3 4 
# 0 1 2 3 4 
# 1 2 3 4 
# 2 3 4 
# 3 4 
# 4 
num=int(input("Enter a number:"))   
for i in range(1,num+1):   
     for j in range(1,i+1):   
         print(num-i+j-1,end=" ")   
     print()  
for a in range(1,num+1):   
     for k in range(0,num-a):   
         print(k+a,end=" ")   
     print()  

# 4 
# 4 3 
# 4 3 2 
# 4 3 2 1 
# 4 3 2 1 0 
# 4 3 2 1 
# 4 3 2 
# 4 3 
# 4

num=int(input("Enter a number:"))   
for i in range(1,num+1):   
     for j in range(1,i+1):   
         print(num-j,end=" ")   
     print()   
for a in range(1,num+1):   
     for k in range(1,num+1-a):   
      print(num-k,end=" ")   
     print()   