# accept a number and check if it a perfect number or not 



# n=  int(input("check your number is perfect or not  : - "))
# sum= 0
# for i in range(1,n+1):
#     if n%i==0:
#         sum =sum+i
#     if sum==n:
#         print("your number is perfect ",sum)

#     else:
#         print("your number is not perfect ")



# you can try bettrt logic 

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Your number is Perfect Number")
else:
    print("Your number is Not Perfect Number")