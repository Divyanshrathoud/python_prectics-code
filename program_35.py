# function in pythom
"""
function in python group reusable code into a block that can 
be executre by calling the function name  this help avoid repelition 
and makse program modular and readable 

there  are many in -build function in python like 
print(), input (),len() ,etc

"""

def  hi ():
    print("this a functions  and this name is hi")

def table ():
    n= int(input("enter the number to print table"))

    for i in range(n,n*11,n):
        print(i)


hi() # calling the function
table() # calling the function using its name

print("--------------------------------------===111----------------111--------------------------")

# parameteress and argument in python function

"""
first thing i want to talk about is parameter, parameters are variables listed inside the  function definr 


parameter: variables defined in the function definition
argument: the actual values passed to the function when it is called
"""

def sum(a,b):# a and b are parameters
    c=a+b
    print("the sum of two numbers is ",c)

sum(5,10) # 5 and 10 are arguments

def multi(a,b,c):
    d=a*b*c
    print("the multiplication of three numbers is ",d)

multi(2,3,4) # 2, 3, and 4 are arguments


def greet(name):
    print("hello",name)     

greet("divyansh") # passing the argument  this called positional argument 
