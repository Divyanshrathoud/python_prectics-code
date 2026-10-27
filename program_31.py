# count all letters digits and special symbols from a given string 

a= "p@#$%^&*())_gff3232"
char=0
dig =0
sp_char =0

for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1

    else:
        sp_char +=1

print(f""""
    your digits are {dig}\n
    your char is {char}\n
    your sp_char {sp_char}
      """)
     