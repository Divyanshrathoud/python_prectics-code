#------------------------opreters in pyhton ---------------------------------------------
"""
operators are symbols that perform oprections on variables and values

1> Arithmetic opereators 
(1) addition  ( 1+1)
(2) Subtraction (4-4)
(3)Multiplication(5*5)
(4)division(4/2)
(5)flor division  (2//5)
(6)modulus  %(yaad rakhata hai remender)
(7)Exponention (5**2) power 
"""
print("===================================arithmetic operetors===============================")
print(1+1,"(addition)")
print(10-5, "(subtraction)")
print(10*5,"(multipicATION )")
print(10/5,"(DIVISION)")
print("\n")

print(4//2,"(flore division)") #floating ko int me convert 
#4/2 = 2.0 > 4//2 = 2

print(50/5)

print(45%5,"modulus") # rementder ko alg karta hai 
print(5**5, "exponentiation 5*5*5*5*5") 

print("\n ==============================Assignment opreters====================== ")
print("""
Assignment opreter are used to assogn valuesn to variables 
a=45
n= 44
name = divyansh
ager 22
""")
a= 45
d=44 

print("===================compound assignment =========================")
print("\n compound assignement oprator combines arithmetic oprator with assignment  ")

"""
+= add and assign
-=subtract and assign
*= multiply and assign
/=divide ans assign
//= flor and assign
%=modulurs and assign
**=exponention and asign
"""
a=2
a+=2
a+=2
print(a)


print("===============================comparsion opretor=============================")
"""
comparison operator also called relation operator are ueed to compare to values 

1> ==
2> !=
3> >
4> <
5> >=
1> <=
"""
a= 50
b=20
c="divyansh"
print(a==b)
print(a!=b)
print(a==c)

print(45<40,"greter then")
print(45>40)
print(a>=20)
print(b>=a)



