#-------------------------------------/Data types/-------------------------------------------
"""
DATA TYPES :data type are the things we store in variables and it define whtat data types vaeiables.
python has bulit -in data type for different kinds of data .

--------------------------------------------------------------------------------------------

1. Numbers
2. strings
3.type conversion 
"""

#--------------------------------------------/numbers /----------------------------------
"""
(a)Integer datatype: all the  numbers excluding decimal places and fraction 
 
       a= 45+45
       print(a)                

(b)Float datatype ;  all the decimal numbers and frection valuse are float

        b=2.2
        print("this valuse is a float data types",type(b))

        c =12/2
        print("this valuse is a float data types",type(c),c)


(c)complex data types ; numbers with a real and imaginary part
     
 s= 3+4j


(d)String datatypes ; this is used to store anything in python 
, litearlly anthings that available on your keyboed

data = ("my name is divyansh rathoud i am 22 year old ")
stuuudy = (''' i curntly studdy  betch from data science''')


(e)boolean data types ; there are nothings much to say this is the data types 
which will and always give the result of thr true and false 

a= true 
b = false 

"""


#-------------------------string indexing---------------------------------------------
"""
you must have thought there are so many characters in a string but can you access every one .


               [0, 1, 2, 3, 4, 5, 6, 7]
   indexing =>  d  i  v  y  a  n  s  h
              [-0,-7,-6,-5,-4,-3,-2,-1]

----------------------(positive indexing)-----------------------------------------

h ="hello"      [0, 1, 2, 3, 4]

print(h[0])
print(h[1])
print(h[2])
print(h[3])
print(h[4])

-----------------------(negativr indexing)-------------------------------------------


name = "divyansh"    [-0,-7,-6,-5,-4,-3,-2,-1]

print(name[0])
print(name[-7])
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

"""

#----------------------------------string slicing -------------------------------------------

"""
you know how to access characters in string but there are slicing option as well
slicing means cuttung out a slice from and this is also done using indexing value 

d= "hello"
print(d[0:4:1]) => [start : stop : step ]




"""

#---------------------------------------type conversion ---------------------------------------
"""
[1]int()
[2]float()
[3]str()
[4]bool()

a=  45
d =str(a)
d= bool(a)
d= float(a)

print(type(d))

"""
#--------------------------------------types of types conversion types -------------------------------
"""
 there are 2 types of conversiom  "imolicit" and "explicit"
 
"""
