list1 =[input("Enter the input: ")]
c=list1.copy()
print(c)

list1.reverse()
print(list1)
if(c==list1):
    print("Palindrome")
else:
    print("Not palindrome")