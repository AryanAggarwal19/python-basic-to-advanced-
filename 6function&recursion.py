#1 function definition

# def calc_sum(a,b): #parameters
#     sum= a+b
#     print(sum)
#     return sum


# sum= calc_sum(100,199) #function call; arguments

#average of 3 numbers
# def avg(a,b,c):
#     return (a+b+c)/3

# ans= avg(30,30, 30)
# print(ans)

# #2 default parameters in function

# def calc_prod(a,b=1):
#     print(a*b)
#     return a*b

# calc_prod(9)

#3 practice questions 

#3.1 WAF to print the length of a list(list is the parameter)

def print_list(list):
    print(len(list))
    return len(list)

#3.2 WAF to print the elements of a list in single line

def print_listelems(list):
    for elem in list:
        print(elem, end=" ")


#3.3 WAF to find the factorial of n

def calc_fact(n):
    i= n-1
    factorial= n
    while(i>=1):
        factorial= factorial*i
        i-=1
    print(factorial) 

    # factorial=1
    # for i in range(1,n+1):
    #     factorial*=i
    # print(factorial)
    # return(factorial)  

#3.4 WAF to convert USD to INR
    
# def calc_usdToInr(amount):
#     exchange_rate= 83.08
#     print(amount* exchange_rate)

       
# print_list([1,44,88,"shyam","ram",22,7])
# print_listelems([1,4,9,16,25,36,49,64])
# calc_fact(50)
# calc_usdToInr(20000)
    

##################### RECURSION #########################
    
#EX-1 factorial of a number
    
def calc_fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * calc_fact(n-1)
    
#EX-2 WARF to calculate the sum of first n natural numbers
    
def calc_sum(n):
    # base case 
    if(n==1):
        return 1
    else:
        return n+ calc_sum(n-1)
    
# sum= calc_sum(10)
# print(sum)
    
#Ex-3 WARF to print all elements in a list.
    
def print_list(list,idx):
    # base_case
    if(idx== len(list)):
        return 
    
    print(list[idx])
    return print_list(list,idx+1)

list= ["Mhatma Gandhi","Subhash Chandra Bose","Bhagat Singh","Chandra Shekhar"]
print_list(list,0)



   