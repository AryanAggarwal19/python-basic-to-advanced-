#1 While loop

#syntax
# while condition:
    #do something

#1 print hello 5 times
# count= 1
# while count<= 5:
#     print("hello")
#     count+= 1

#2 print no from 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i+=1 

#3 print no from 5 to 1
# i= 5
# while i>0:
#     print(i)
#     i-=1

#4 print the multiplication table of no n

# n= int(input("Enter the number: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# 5 print the elements of following list using loop
# list= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i=0
# while(i<len(list)):
#     print(list[i])
#     i+=1

#6 search for a number x in the tuple using loop

# tup= (1,4,9,16,25,36,49,64,81,100)

# x= int(input("Enter the no u want to search in the tuple: "))
# i=0
# while(i<len(tup)):
#     if(tup[i]== x):
#         print("Search successful at index: ", i)
#         break
    
#     else:
#         print("finding..")   
#     i+=1

# print("end of loop")


###2 for loop in python
        # In Python, the for loop is used to iterate over a sequence (such as a list, tuple, string, or range), or any iterable object. 
        # The syntax of the for loop in Python is straightforward:
        #for item in sequence:
            # Code block to be executed for each item in the sequence

# Here's what each part of the for loop syntax represents:

    # for: This keyword indicates the start of the loop.
    # item: This is a variable that represents the current item in the iteration. You can choose any valid variable name.
    # in: This keyword separates the variable name from the sequence or iterable object over which you're iterating.
    # sequence: This is the sequence or iterable object over which the loop iterates. It can be a list, tuple, string, range, or any other iterable object.


# list= [1, 2, 3, 4, 5]


# for num in list:
#     print(num)

#q1 

# list= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

# for num in list:
#     print(num)

#q2 search for a number in list

# x= int(input("Enter the no: "))

# IDX=0
# for num in list:
#     if(num== x):
#         print("found at idx", IDX)
#         break
#     IDX+=1
# else: #(imp)--> optional else in for loop
#     print("NOT FOUND")

# range function in python

# In Python, the range() function generates a sequence of numbers. It's commonly used in combination with loops, particularly for loops, to iterate a specific number of times. The syntax of the range() function is as follows:
# range([start], stop, [step])
# Here's what each argument represents:

# start (optional): The starting value of the sequence. If omitted, it defaults to 0.
# stop: The end value of the sequence. The sequence will go up to, but not include, this value.
# step (optional): The step or increment between each number in the sequence. If omitted, it defaults to 1.
# The range() function returns a sequence object that generates numbers on-the-fly, rather than generating the entire sequence upfront, which makes it memory-efficient for large ranges.
    
#practice questions
#using for & range

#1 Print numbers from 1 to 100
    
    # for num in range(1,101,1):
    #     print(num)

#2  Print numbers from 1 to 100(in reverse)
    
# for num in range(100,0,-1):
#      print(num)

#3 print the multiplication table of number n

n= input("Enter the required no:")

for num in range(1,11,1):
    print(num*n)
    

     
   





