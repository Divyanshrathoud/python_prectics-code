"""
while loop repeats a block of code as long as a condition is true it is useful when the number of inerations is unknown before execution 


while condition :
       code to execute

"""

# a= 1
# while a<10:
#     print(a)

a=2
while a<=20:
    print(a)
    a= a+2

n=  1
while n<=100:
    print(n)
    n = n+1

print("\n")
#separate eatch digit of a number and print it on the new linw 

print("separate eatch digit of a number and print it on the new linw ")
s=  int (input("enter the value "))
while s>0:
    print(s%10)
    s=s//10
