# Lists in python
#are equivalent to arrays in c++

#1 Initialization and Indexing
marks= [99,80,45,31,77,66]
print(marks[0])  #99
print(type(marks))  #lists
print(len(marks)) #fetch the length of the list

#2 In a single list we can store multiple dataTypes unlike c++
#3 In python, strings are immutable(i.e there values can only be accessed but can't be manipukated)
# but on the other hand, lists can be mutable 

student= ["Karan",95.4,17, "Delhi"] 
student[0]= "arjun" #mutating 

#3 Slicing in List
#return sublist
#exactly similar to string slicing
#syntax=> list_name[starting_index:ending_index] #ending idx is not included

print(marks[1:3])
print(marks[1:])
print(marks[:len(marks)])
print(marks[:3])
print(marks[-1:-3]) #empty array (review)
print(marks[-3:-1]) #31, 77

#4 List_Methods

#A list.append()
#B list.sort()  #sorts the list in ascending order
#C list.sort(reverse= true)  #descending order
#D list.reverse()
#E list.insert(idx,elem) #insert the element at particular index

# list= [2, 1, 3, 4]
list= ["banana","litchi","apple"]

#list.append(5)  # 2 1 3 4 5
list.sort() 
list.sort(reverse= True)
list.reverse()
list.insert(100,"omogreanate")
print(list)

####################################  TUPLES IN PYTHON #####################################################

#1 TUPLES: built in datatype that let us create immutable sequence of values
#2 almost equivalent to lists but are different in a way that they can't be mutated i.e u can't change any values and can't
# assign new values

#3 Initialization
tup = (1,2,3,4,5,2,1)
print(type(tup))  #class "tuple"
print(tup[0])

#4 empty tupple
tup1= ()
print(tup1)
#5 single value tupple
tup1=(1,)  #note the ',' in the end if u remove this ',' then python will interperet this as integer
print(tup1)

tup1= (1)
print(tup1)
print("the type of tup1 when ',' is not included",type(tup1))  #int

#Note in case of multiple values giving "," at the end is completely optional
#for ex tup=(1,2,3,4) => this will still be percieved as tupple

#5 Slicing 
tup2= (1,2,7,8,9,34,5,4,4,4,4,4,)
print(tup2[0:5])

#Tuple methods
#A index-method => tup.index(el) #returns index of first occurence 
#B tup.count(el) #count the total occurences

print(tup2.index(2))
print(tup2.count(4))

#################################### Practice Questions #########################################

#1 WAP to ask the user to enter names of their 3 fav movies and store them in list.

# print("Enter the name of your 3 favourite movies")

# movie1= input("Movie1 :")
# movie2= input("Movie2 :")
# movie3= input("Movie3 :")

# movieList= [movie1, movie2, movie3]
# print("your fav movies are as follows :", movieList)


#2 WAP to check if a list contains palindrome of elements.(Hint: use copy() method)
#[1,2,3,2,1]    
#[1, "abc", "abc", 1]

list1= [1,2,3,2,1,]
temp= list1.copy()
print(temp)
temp.reverse()
print(temp)

if(list1 == temp):
    print("pallindrome")
else:
    print("not a pallindrome")

#3 WAP to count the number of students with grade "A" in the following tuple
tup= ["C","D","A","A","B","B","A"]
print(tup.count("A"))




