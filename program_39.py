"""Python me List ek bahut hi powerful aur commonly use hone wala data structure hai, 
jiska use ek hi variable me multiple items (values) ko store karne ke liye kiya jata hai. 
List ko square brackets ([ ]) ke andar banaya jata hai aur elements ko comma (,) se separate kiya jata hai.

"""

# Python List ki 4 Main Characteristics:
"""
1> Mutable (Can be changed after creation):
List banne ke baad aap uske elements ko modify (change), 
add, ya remove kar sakte hain.
Matlab yeh immutable nahi hoti, isme badlaav possible hai.

______________________________________________
|fruits = ["apple", "banana", "cherry"]      |
|fruits[1] = "mango"                         |
|print("Change ke baad:", fruits)            |
|____________________________________________|

2>Ordered (Maintains the order of insertion)
Jab aap list me elements daalte hain, toh list unka wahi order fix rakhti hai jis order me unhe insert kiya gaya tha.
Isme har element ka ek fixed index hota hai jo 0 se start hota hai.

_________________________________________________________________
|  numbers = [10, 20, 30, 40]                                    |
|  # Har item ka ek fixed index hota hai (0 se shuru hota hai)   |                                           |
|  print("Pehla item (Index 0):", numbers[0])  # Output: 10      |
|  print("Dusra item (Index 1):", numbers[1])  # Output: 20      |
|  print("Aakhri item (Index 3):", numbers[3])  # Output: 40     |                                      |
|                                                                |
|________________________________________________________________|

3> Duplicates (Can have multiple same values)
List me same value ya element ko aap ek se zyada baar (multiple times) store kar sakte hain. 
Yeh duplicate values ko allow karti hai.
____________________________________________________________________________-__________
|                                                                                      |
|   duplicate_list = ["apple", 10, "banana", "apple", 10, "apple"]                      |                           |
|     print(duplicate_list)                                                             |
| # Count check kar sakte hain                                                          |
|     print("'apple' kitni baar aaya:", duplicate_list.count("apple"))  # Output: 3     |                                   |
|                                                                                       |
|__________________________________________________                                     |

4>Heterogeneous (Can have different data types)

Ek hi list ke andar aap alag-alag data types ki values ko ek sath rakh sakte hain—jaise integer,
 float, string, boolean, yaani sabhi ko ek sath.

 ____________________________________________________
| mixed_list = ["Divyansh", 21, 5.9, True, [10, 20]]                                                 |
|                                                  |
|                                                  |
|                                                  |
|__________________________________________________|
"""
# 0,1,2,3,4,5,6,7,8,9 indexing 
a= [1,2,3,4,5,6,7,8,9,10]
print(a)
print(a[0])  # Accessing the first element
print(a[1])  # Accessing the second element
print(a[0:5])  # Accessing elements from index 0 to 4
print(type(a))  

l = ["divyansh", 12,10,11,11,10,0.2,00.2,True,False]
print(l[0:6])
print(l[1:-5])   