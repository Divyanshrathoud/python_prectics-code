# functions quesdtion 
# Q 1   check  string is pallindrome or not 

def p (st):
    rev =""

    for i in range(len(st)-1,-1,-1):
     if rev == st:
        print(f"it is pallindromic{st} ")

    else:
       print (f"not a pallindromic {st}")


p("naam")
p("vi")
p("nisha")
    