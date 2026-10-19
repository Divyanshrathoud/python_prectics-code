# question 6
print("accept a year and check if it a leap yesar ")
# 2000 , 1800 , 1900 /400
#2001 , 2005 ,... /4

year = int (input("enter your year:"))

if year%4== 0 and year%400==0:
    print(f"{year} is is a leep year")
else:
    print(f"{year} it is normal year")