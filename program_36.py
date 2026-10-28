# types of argument :

"""
1> positional argument 
2> default argument 
3>keyword argument 

"""

print("positional argument ")
def hello(name): #passing the parameter
    print(f"hi {name} how are you i  hope your fine")

def sum(a,b,c):
    c= a+b+c
    print(f"your sum is {c}")
    

hello("divyansh") # passing the argument 
sum(1,2,3)

print("\n")
print("key word argument ")

def info(name,age): # passing the parametter 
    print(f"your name is {name}\n",f"and your age is {age}")

def collage(name , age , branch ):
    print(f"your name is {name} your age is {age} and you select branch {branch}")



info(name ="divyansh", age = 22)
info(age =22,name = "nisha")

collage(name = "nisha patel ", age = 22, branch= "data science (ds)")
collage(name = "divyasnh rathoud ", age = 22, branch= "data science (ds)")

print("\n")
print("default agrument ")

def g(a,B=15):
    print(a+B)

g(5)

def student(name,age , branch="data science"):
    print(f"student namre is {name},age is {age} ,your branch is  branch  {branch}")


student("divyansh",22)



