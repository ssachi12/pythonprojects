from builtins import print

import pyinputplus as pyip
print("Largest city: ")
c1=pyip.inputMenu(['Tokyo','Paris','Amsterdam'],numbered=True)

print("Fastest animal: ")
c2=pyip.inputMenu(['Cheetah','Tiger','Elephant'],numbered=True)

print("largest country: ")
c3=pyip.inputMenu(['Russia','Canada','Japan'],numbered=True)

correct=['Tokyo', 'Cheetah', 'Russia']
user=c1,c2,c3#tuple

total =zip(correct,user)

score=0

for i, j in total:
    if i==j:
        score+=1
    else:
        continue
    print("Your score is: ",score)


