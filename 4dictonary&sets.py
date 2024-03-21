# ###################################### Dictonary_In_Python ############################################
# 
#info= {
#     "key":"value",
#     "name":"thor", #string
#     "age": 10, #int
#     "is_adult": True,  #boolean
#     "subjects":["python","excel","mySql"], #list
#     "hobby":("cricket","reading"), #tuple
# }

# print(type(info))

# #2 accessing key-value pairs in dictonary
# # square notation is used to  access different key-values like,
# print(info["age"])
# print(info["name"])

# #3 assigning new values and adding new keys
# info["name"]= "harry"
# info["surname"]= "potter"
# print(info["name"],info["surname"])

# #4 Empty_dictonary
# null_dict= {}

# null_dict["name"]= "Aman Gupta",
# null_dict["surname"]= "Saraswat"
# print(null_dict["name"],null_dict["surname"])

# #5 nested_dictonary

# student={
#     "name": "Rahul kumar",
#     "score":{
#         "phy":100,
#         "chem":23,
#         "maths": 88.77,
#     }
# }

# print(student["score"]["phy"])

#6 dictonary_methods

# #1.1 mydict.keys();   # Returns all the keys in the dictonary
# print(list(student.keys()))
# #1.2 print the total number of keys in dictonary
# print(len(student)) #or 
# #first get all the keys from student.keys() method then use len()method to find the length of that key list
# print(len(list(student.keys())))


# #2 mydict.values(); #returns the collection of all the values
# print(list(student.values()))


# #3.1 mydict.items();  #returns all (key, value) pairs as tuple
# print(list(student.items())) #typecast to list
# #3.2 accessing individual values
# pairs= list(student.items())
# print(pairs[0]) #this access the first tuple


#4 mydict.get("key") #return the values acc to key
# print(student["name"]) # error if key wrong
# print(student.get("name")) #no error--> None


#5 mydict.update(new Dict) #inserts the specified items to the dictonary

# student.update({"city":"delhi"})

# print(student)


################################# SETS_In_Python ################################################

#1 basics

# collection= {1, 2,2,3,3, 3, 4,"hello","world",True}

# print(collection)

#2 empty set syntax
# collection= {} #this is the syntax of empty dictonaty
# collection = set()

#3 set_methods

# collection= set()
# collection.add(1)
# collection.add(2)
# collection.add("radhika")
# collection.add((1,2,3))


# collection.remove(2) 
# # collection.clear() #empties the set

# collection.pop() #POP THE random value from the set

# print(len(collection))
# print(collection.pop())


# set1= {1,2,2,4,6}
# set2= {10,11, 2}

# print(set1.union(set2)) #{1,2,4,6,10,11}
# print(set1.intersection(set2)) #{2}


#PRACTICE QUESTIONS

#1 STORE the following word meanings in python dictonary

# dictonary= {}
# dictonary["table"]=["a piece of furniture", "list of facts and figures"]
# dictonary["cat"]="a small animal"

# print(dictonary)

# #2 you are given a list of subjects for students.Assume one classroom is required for 1 subject.
# #how many classrooms are needed by all students

# givenCollection= {"python","java","C++","javascript","java","python","java","C++","C"}

# print("classrooms required will be :", len(givenCollection))

#3 
student= {}

marks= {
    input("Enter subj1 name : ") : int((input("Enter subj1 marks : "))),
    input("Enter subj2 name : ") : int((input("Enter subj2 marks : "))),
    input("Enter subj3 name : ") : int((input("Enter subj2 marks : "))),
    
}
print(marks)

student.update(marks)
print(student)

#4 figure out a way to store 9 and 9.0 as seperate value in the set.
#YOU can take help of built in datatypes

# collection= set()
# num1= (9)
# num2= "9.0"
# collection.add(num1)
# collection.add(num2)
# print(collection)

# #pair in the form of tuples

# values={
#     ("float", 9.0),
#     ("int", 9)
# }