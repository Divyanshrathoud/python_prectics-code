#accept a number and check its  revers 
a=  int (input("enter the value  "))
rev = 0
while a>0:
    rev =rev*10+ a%10
    a=a//10
    print(rev)


# and check your numbers is pallindromic or not

n= int(input("to check your number is pallindromic"))
copy =n
add =0

while n>0:
    add =add*10 + n%10
    n=n//10

if copy==add:
    print("yes it is pallindromic")

else:
    print("not a pallindromic")