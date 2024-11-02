#syntax of SET
collection={"Name",45,"Address"}
##(collection)
##(type(collection))

# SET is nothing but a unorder list. and duplicate values are ignored.

collection1={"Name",45,"Address",55,"city","city",55}
##print(collection1)
##print(len(collection1))

# For creatiing a dictionary
c1={}
##(type(c1))

#For creating empty set
c2= set()
#print(type(c2))
#collection1.add(69)
#print(collection1)
#collection1.remove(69)
#print(collection1)

#can't passed the list.Below given proogram is not valid.
#collection1.add([1,2,22])
#print(collection1)

# pop removes the value randomly, no need to mension any element. 
collection1.pop()
#(collection1)

# SETS ARE MUTABLE BUT ITS ELEMENTS ARE IMMUTABLE.
# WE CAN PASSED THE TUPLE BUT CAN'T PASSED THE DICTIONARY.

set1 = {1,2,4,5}
set2 = {2,5,7,9}
#JUST FOR ADD TWO SETS AND ELEMENTS WILL BE SAME
print(set1.union(set2))
# NO CHANGE IN ORIGINAL SETS
print(set1)
print(set2)
#INTERSECT THE SAME VALUES
print(set1.intersection(set2))




