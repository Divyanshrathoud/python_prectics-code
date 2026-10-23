# loop for string
#loops for string work slightly differently you can iterate through a string in two way
"""
a > using index value
b> iterating directly over the string
"""

a=  "divyansh"
for i in range(len(a)):
    print(a[i])

h= input("enter your name ")
for i in range(len(h)):
    print(h[i])

d="divyansh is good looking"
print(len(d))
for i in range(len(d)):
    print(d[i])


#secound way is simpler we can directily but using this method will give you the direct access to the characters instead of index values

f= "from"
for char in f:
    print(char)