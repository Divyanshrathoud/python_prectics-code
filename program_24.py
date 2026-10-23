# factorial of a numbers
# 5*4*3*2*1 =5!

n= int(input("enter your fectorial "))
fact =1
for i in range(1,n+1):
    fact =fact*i
    print(fact)