# loops  : python allow as to execute a block of code multiple time  without rewring it 

#types of loops (1) for loop   (2)while loop

# range function :  before understanding for loops you should know how range function works 
#range function is used to generate a sequence of numbers which is commonly used in loops

"""
syntax 
range(start , stop , step )

"""
print("==============================for loop ==================================================")

#to  print 1 to 19 
for i in range(1,20):
    print(i)

f=  range(1,16,1)
for i in f:
    print(i)

#=========================================================================================]
#============ 20  ----->  50=========================================
print("20 to 50")
g= range(20,51,1)
for s in g:
 print(s)


# ============================== 50 to  20 ===================================
print("reverse order ")
for i in range (50,19,-1):
    print(i)








