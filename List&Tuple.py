s1 =["prithwi", 183, 444, "guys", 7878, "Upper", 841]
#print(s1[0])
#print(s1)
s1[0]="honey"
#print(s1)
# Note: Lists are mutable but strings are not(they are immutable).
# we can change value in any list.
s2=[44,55,14,74,78,"tt"]

# LIST SLICING

#print(s2[0:4])
#print(s2[0:len(s2)])
#print(s2[0:])

# NOTE: print(s2[0:len(s2)]) = print(s2[0:]), both are same different approach to indicate same thing.

#print(s2[-4:-1]) # To write a LIST in  reverse order

# Append Method
s3 =[45,12,47,71,55]
s3.append(69)
#print(s3)


# NOTE:
#  The given below method is not right way to append any element.
# print(s3.append(69)), it returns the NONE.

# Sorting method(mainly ascending order)
s3.sort()
#print(s3) 

# TO DO SORTING IN REVERSE ORDER (IN DESCENDING ORDER ) 

s3.sort(reverse=True)
#print(s3)

s4=['b','a','r','g','c','d']
s4.sort()
#print(s4)
s4.sort(reverse=True)
#print((s4))

# To reverse the original list
s5=['a',2,'c',4,'e',5]
s5.reverse()
#print(s5)

s5.reverse()
s5.insert(4,'x')
#print(s5)

# TO DO INSERT FOLLOW THE BELOW MENSION PROCESS
l1=[1,2,3]
l1.insert(0,9)
#print(l1)

#remove methode : to remove any element
#  WE NEED TO ENTER THE SPECIFIC ELEMENT
l2=[1,2,3,4]
l2.remove(2)
#print(l2)

#POP method: to pop any element
#WE NEED TO ENTER THE SPECIFIC ELEMENT INDEX VALUE

l3=[4,5,6,7]
l3[1]=9
#print(l3)
l3.pop(1)
#print(l3)
l3.pop(2)
#print(l3)
#print(l3[2])
L5=[111,22,33,44.55,66]
L5.insert(3,99) #placed the element '99' at the place of 44
#print(L5)

#---------------------------------------------------------------------------------------
#----------------------------------TUPLE------------------------------------------------
#---------------------------------------------------------------------------------------
#HOW TO MAKE TUPLE WATCH BELOW

T1=(2,1,4,8,6,3,7)
print(T1[0:3])
#print(type(T1))
#print(T1[3])
print(T1.index(8)) # this shows that the element '8' is placed at the index 3.
print(T1.index(7))
print(T1.count(8))#here, after counting 8 is found only for once

# Q1
# take 3 movie names and store into list

movies = []
m1=input("Enter the 1st movie: ")
m2=input("Enter the 2nd movie: ")
m3=input("Enter the 3rd movie: ")

movies.append(m1)
movies.append(m2)
movies.append(m3)
#print("The movies are: ",movies)

#instead of using different variables (m1,m2,m3) we can use a single variable(example: mov).
# Process is given below with name of fruits.

fruits=[]
f=input("Name1: ")
fruits.append(f)
f=input("Name2: ")
fruits.append(f)
f=input("Name3: ")
fruits.append(f)
#print("names are: ",fruits)

# WE CAN ALSO DO>
cars=[]
cars.append(input("car1: "))
cars.append(input("car2: "))
cars.append(input("car3: "))
#print("The cars are: ",cars)


# HOW TO CHHECK PALINDROME OR NOT.

#LIST1=[input("entr the list")]
#print(LIST1)
list1 =[1,2,1]

COPY_list1=list1.copy()
COPY_list1.reverse()

 if(COPY_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

# create a list
numbers = [2, 3,2,2,2, 5, 2, 11, 2, 7]

# check the count of 2
#count = numbers.count(2)

print('Count of 2:', numbers.count(2))




















