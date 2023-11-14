import random
number =random.randint(1,50)

guess=0
count=1
while guess != number and count<6:
    guess=int(input("Make a guess between 1 to : "))
    if(guess>number):
        print("too high")
        count+=1
    elif(guess<number):
        print("too low")
if count<6:
    print(f"you made it in {count} times")
else:
    print('Oooops.....You ran out of guess')
