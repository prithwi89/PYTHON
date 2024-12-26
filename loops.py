# using of while loops
#c="hello guys"
#w = 1
#while w <= 5 : 
 #   print("Heloo")
   # w = w+1 #increases "w" by 1

# another example

#i=12
#while i>=1:
   # print(i)
   # i-=1
    
#print("loop ends here")    

# PRINT 1 TO 100.
#a=1
#while a<=100:
   # print(a)
   # a+=1

#print("Loop ends here for a")     

# PRINT 100 TO 1.
#b=100
#while b>=1:
    #print(b)
    #b-=1
#print("Loop ends here for b")   

# PRINT THE MULTIPLICATION TABLE OF NUMBER N.



#color = input("What color is rose?: ")
#print(color)

#m=int(input("Enter the m : "))
#i=1
#while i<=10 :
   #print(m*i)
   #i+=1

#a=["Apple","Banana","Guava","Mango"]
#i=0
#while i<len(a):
 #  print(a[i])
 #  i+=1

#a=(11,2,33,43,234,546,455)
#x=int(input("Enter the searched item: "))
#i=0
#while (i<len(a)):
  # if(x==a[i]):
   #   print("Element found at index : ",i)
  # i+=1

# BREAK AND CONTINUE:

#a=0
#while a<=7:
#   print(a)
#   if(a==5):
#      break
#   i+=1

#a=0
#while a <= 9:
    #print(a)
#    if(a==4):
     #   break
    #a+=2

# TO PRINT ODD VALUES
#print("FOR ODDS")
#i=1
#while i<=20:
 #  if(i%2==0):
  #    i+=1
   #   continue
   #print(i)
   #i+=1 

# TO PRINT even VALUES
#print("FOR EVEN")
#i=1
#while i<=20:
 #  if(i%2!=0):
  #    i+=1
   #   continue
   #print(i)
   #i+=1 

num=[1,2,3,4,5,6,"mango", "banana","abc" ]
for b in num:
   if(b==2):
      print
print(" ")

string="Prithwiraj_Saha"
for n in string:
   print(n)
   
##|||| USES OF RANGE ||||##

print(" ")
print(" RANGE ")
print(" ")
seq=range(6)
for i in seq:
   print(i)
print(" ")

print(" RANGE 1st to last item ")
s1=range(4,10)
for i in s1:
   print(i)

print(" RANGE 1st to last item with giiven increasing steps")
s2=range(1,10,2)
for i in s2:
   print(i)

print(" 1 to 100 even numbers")
s3=range(2,100,2)
for i in s3:
   print(i)

print("")
print("|| TO AVOID ANY LOOP FROM PROCESSING ||")
for i in range(90):
   pass
print("USE 'PASS COMMNAD' TO AVOID ANY LOOP FROM PROCESSING ")   

print(" USES OF 'PASS' ")   
for i in range(8):
   if i==6:
      pass
   print(i)
   

n1=9
p=1
p1=0
while p<=n1:
    p1=p1+1
print(p1)    




