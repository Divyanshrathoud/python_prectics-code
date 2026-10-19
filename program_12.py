# question 5
print("accept name and age from the user check if the user is valod voter ")
name = input("enter your full name : -")
age = int(input("enter your age :- "))

if age >=18:
    print(f"{name} your valid for vote")

else:
    print(f"{name}your not valid for vote")