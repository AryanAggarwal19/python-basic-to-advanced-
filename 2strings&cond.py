#strings =>is a datatype that stores a sequence of characters

str1= "this is a string \twe we are creating in python" #\n,nwe to break the line #twe => tab
str2= 'this is a string'
str3= """this is a string"""
#use of triple quotes
"""this is apna's college "tutorial" """

## basic operations

#1 concatenation
print("hello"+"world") # helloworld

#2 length of str
print(len(str1))

#3 Indexing
str= "Apna College"
str[0] #A
str[9] #e
#keypoint => python mein index ke through hum sirf characters ko access krskte hai but usko modify/manipulate nhi kr skte

#4 Slicing
#implies accessing part of string
#syntax: str[starting_index : ending_index] #ending_index not included
#For ex=> 
str="Mera College"
print(str[1:4]) #era
print(str[1:]) #"Mera College"
print(str[:9])  #"Mera Coll"
print(str[1:len(str)])

#5 Functions related to string
test_str= "Iam studying python by Apna College"
print(
  len(test_str), #prints the length of string
  test_str.endswith("College"), #check if a string endswith provided substring
  test_str.capitalize(), #returns new string
  test_str.find("A"), #return first occurenece of the provide word
  test_str.count("s"), #count the total number of occurenece of substring
  test_str.replace("o","a")
  )

#6 Practice questions

#1 (Ref notes for problem statement)
# firstName= input("Enter ur first name:")
# print(len(firstName)) 

#2 
# temp= "String"
# print(temp.find("S"))


########################################################################################

# CONDITIONAL STATEMENTS IN PYTHON

#1 Syntax--> if-elif-else
# if(condition): statement1
# elif(condition): statement2
# else: statementN

age= int(input("Enter your age:"))

if(age>= 18 and age<=60):
    print("Can vote and apply for license")
elif(age<= 18):
    print("nhi ho rhe pdhai")
else:
    print("nhi ho rhe bhajan")

#Grade students based on marks
marks= int(input("Enter ur marks:"))
if(marks >= 90):
    print("Grade A")
elif(marks<90 and marks>=80):
    print("Grade B")
elif(marks<80 and marks>=70):
    print("Grade C")
else:
    print("Grade D")

#2 nesting
#3 indentation , in python indentation act like a block and thus become very imp syntax wise

# Practice questions
#1 write a program to check if a number is even or odd

nums= int(input("Enter the number:"))
if(nums%2==0):
    print("The number is even")
else:
    print("The number is odd")

#2 write a program to find the greatest of 3 nums entered by user

num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
num3= int(input("Enter the third number"))

if(num1 > num2 and num1> num3):
    print("the greatest number is: ", num1)
elif(num2> num1 and num2>num3):
    print("the greatest number is:", num2)
else:
    print("the greatest number is:", num3)

#3 WAP to check if a number is multiple of 7 or not

number= int(input("Enter the number to be checked"))
if(number%7==0):
    print("The given no is divisible by 7")
else:
    print("The given no is not divisible by 7")
    









