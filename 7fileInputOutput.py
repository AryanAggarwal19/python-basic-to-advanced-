#1 reading a file in python

# f= open("demo.txt","r")

# # data= f.read() #to read the entire file
# # data= f.read(7) #to read the file upto 7 char

# line1= f.readline() #to read file one line at a time

# line2= f.readline()

# # print(data)
# print(line1)
# print(line2)

# f.close()

#2 writing a file in python

# f= open("demo.txt","w") #overwrite the data
# f= open("demo.txt","a") #append the data at the end

# # f.write("I want to learn js. 123")
# f.write("then I'll move to react")
# f.write("\n then nodejs")

# f.close()

#3 combining modes in python=> r+, w+, a+

# 3.1 r+ mode=> read+overwrite(pointer at start)- no truncate

# f= open("demo.txt","r+")
# f.write("mera naam geeyan hai \n")
# f.write("mein hu bada takatwar")
# f.write("mere awaaz hai bahut sundar")

# print(f.read())
# f.close()

#3.2 w+ mode=> read+ overwrite(ptr at start)=> truncate

# f= open("demo.txt","w+")
# f.write("I'm me \n")
# f.write("he is him \n")

# print(f.read())

#3.3 a+ mode => read+ append(ptr at end)- no truncate

# f= open("demo.txt","a+")
# f.write("this is aryan from I/O file")

# print(f.read())

#4 with syntax
# with open("demo.txt","r") as f:
#     data= f.read()
#     print(data)

# 5 deleting a file
#require module for this

# import os #(os=> built in module)
# os.remove("demo.txt")

#6 practice questions

#6.1 create a new file "practice.txt" using python. Add the following data to it
# f= open("practice.txt","a+")
# f.write("Hi everyone \n we are learning file I/O \n using Python\n I like programming in python")

#6.2 WAF THAT replace all occurence of "python" with "c++" in above file
# with open("practice.txt","r") as f:
#         data= f.read()


# new_data= data.replace("python","c++")
# print(new_data)

# with open("practice.txt","w") as f:
#         f.write(new_data)

#6.3 Search if the word learning exist or not
        
# with open("practice.txt","r") as f:
#         data= f.read()
#         if(data.find("learning") != -1):
#                 print("found")
#         else:
#             print("Not found")

#6.4 WAF to find in which line of the file does the word learning occurs first
# print -1 if word not found


# def checkforLine(file):
#     data= True
#     word= "pyq"
#     line_no= 1
#     with open(file, "r") as f:
#         while data:
#             data= f.readline()
#             if(word in data):
#                 print("found At line_no: ",line_no)
#                 return
#             else:
#                 line_no += 1
#     return -1


# print(checkforLine("practice.txt"))

#6.5 from a file containing numbers seperated by comma, print the count of even no

with open("practice.txt","r") as f:
    data= f.read()
    print(data)
    print(type(data))

nums= data.split(',')
print(nums)
print(type(nums))

count=0
for num in nums:
    if(int(num) % 2==0):
        count+=1

print("THE TOTAL COUNT OF EVEN NUMBERS IS: ",count)

        




       



