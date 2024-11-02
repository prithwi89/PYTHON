
# HOW TO store 2 meaning of same word

dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}

print(dictionary)
print(dictionary["cat"])

# 2ND PRACTICE QUESTION : HOW MANY CLASSES WE NEED FOR DIFFERENT STUDENTS OF SAME SUBJECT.

SUB={"PYTHON","JS","JAVA","C++","C","PYTHON","JS","JAVA","C++"}
print(SUB)
print(len(SUB))


# QUESTION 3: STORE THE DATA ABOUT THE #MARKS OF 3 SUBJECTS IN A DICTIONARY.
#MARKS={}
#p=int(input("Enter the marks of physics: "))
#MARKS.update({"PHY":p})

#m=int(input("Enter the marks of maths: "))
#MARKS.update({"MATHS":m})

#c=int(input("Enter the marks of chemistry: "))
#MARKS.update({"CHEM":c})

#print(#MARKS)


# QUESTION 4: MAKE DIFFERENCE BTW 9 AND 9.0 .  

N1={9,9.0} # {9}
print(N1) # HERE, BOTH WILL BE TREATED LIKE SAME.
 #BUT IF WE STORE IT AS A "STRING" THEN THE CASE IS DIFFERENT.
N2={8,"8.0"}
print(N2) #{8, '8.0'}

N3={8,"8"}#{8, '8'}
print(N3)

#WE CAN ALSO DO THE SAME BY USING DICTIONARY.

VALUES = {
    ("float",9.0),
    ("int",9)
}
print(VALUES)
