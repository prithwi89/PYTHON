d1={
    "name": "Prithwiraj Saha",
    "Subbjects":["Boy","male",21],
    "age":21
}

#print(d1)
#print(type(d1))

#NOT ACCEPTED "print(d1[name])".

#print(d1["age"])
d1["age"]="22"
#print(d1["age"])
#print(d1)

null_d1={}
null_d1["name"]="Samarpita"
null_d1[12]=69.69

#print(null_d1)

d2={
    "name":"Fanindra Mohan Saha",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":96
    },
    "roll":11,
    "address": "Khardah"

}

#    print(d2["subjects"]["chem"])

# HOW TO FIND KEY VALUES
#    print(d2.keys())
# Length of dictionary=Total key points 
#    print(len(d2.keys()))

# TYPECAST THE DICTIONARY INTO THE LIST

#    print(list(d2.keys()))

# VALUES OF DICTIONARY
#    print(d2.values())

#  print(list(d2.items()))
#  print(d2["roll"])
#  print(d2.get("roll"))
# RETURNS NULLJ 
#  print(d2.get("rolll"))

s1={
    "name":"Prithwi",
    "clg":"AOT",
    "state":"WB",
    "age":21

}

# HOW TO UPDATE A DICTIONARY 
stu={
    "batch1":"cse",
    "batch2":"ece",
    "batch3": "me"
}

s1.update(stu)
print(s1)




