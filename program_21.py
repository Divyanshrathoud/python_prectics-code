# print the natural numbers up to n time
n = int(input("enter you number : -"))
for i in range(1, n+1):
    print(i)
print("\n")
# print the table 
t = int(input("you want to print table : "))
for i in range (t ,t*10+1):
    print(i)

print("\n")
t = int(input("you want to print table : "))
for i in range (1,11):
    print(f"{t}*{i} ={t*i}")