# if -elif ladder

temprecher = int(input("planse tell temprecher :- "))

if temprecher<0 and temprecher<10:
    print("freezing pont")

elif temprecher>=10 and temprecher<20:
    print("very cold")

elif temprecher>=20 and temprecher<30:
    print("pleasant")

elif temprecher>=30 and temprecher<40:
    print("hot")

else:
    print("denger ")
