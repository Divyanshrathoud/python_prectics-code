# check string is pallindrome or not

a= "mayank"
b=""
for i in range(len(a)-1,-1,-1):
    b= b+a[i]

if b==a:
    print("your string is pelendrom",{b})

else:
    print("your string is not peledrom ",{b})
