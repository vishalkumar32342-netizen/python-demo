s=input("Enter some string:")
i=1
for x in s:
    print("the character present at positive index : {} and at neegative index :{} is {}" .format (i,i-len(s),x))
    i=i+1

# s="123456789"
# print(s[2:-5:-4])
