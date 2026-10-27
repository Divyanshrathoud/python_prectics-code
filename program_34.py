# create a random number guessing game with python
import random
num =random.randint(1,10)

tries =0
while True:
    guess =int(input("plase tell your number between 1 to 10 :-"))
    tries += 1
    if num == guess:
        print("your write")
        break
    elif num < guess:
        print("go a litte lower")
        tries+=1
    
    elif num>guess: 
        print("g0 a littel higher")
        tries+=1

    else:
        print("sorry try agen")
