# check wether number is prime or not
# (a prime number is a whole number greate then 1 whose only factors 1 and itself ) 
n= int(input("check ypur mumber is prime or not : "))
count =0

for i in range(1, n+1):
    if  n%i==0:
        count =count+i

    if count==2:
        print("prime")
else:
        print("is a not prime ")
