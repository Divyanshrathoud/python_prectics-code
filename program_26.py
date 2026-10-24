# print all the factors of a numbers
"""
example for 12  = 1,2,3,4,6,12
"""
n= int(input("enter your numbers :_  "))
for i in range (1,n+1):
    if n%i==0:
        print(i)