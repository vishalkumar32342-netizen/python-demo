# ________Break statements________________
#  __We can use break statement inside loops to break loop execution based on some 
# condition. 

for i in range(10):
    if i==6:
        print("processing is enough:")
        break
    print(i)

cart=[10,30.65,200.560,450,563,600]
for item in cart:
    if item>500:
        print("To place this order insurance must be required")
        break
    print(item)

#_______Continue__________
# We can use continue statement to skip current iteration and continue next iteration.

#To print odd numbers in the range 0 to 9.
for i in range(10):
    if i%2==0:
        continue
    print(i)

cart=[10,40,57,865,345,564,324]
for item in cart:
    if item>=500:
        print("We cannot process this item:",item)
        continue
    print(item)

#______Pass statements______
#pass is a keyword in Python. 
 
#In our programming syntactically if block is required which won't do anything then we can 
#define that empty block with pass keyword.

#print number which is divisible by 9.
for i in range(100):
    if i%9==0:
        print(i)
    else:pass