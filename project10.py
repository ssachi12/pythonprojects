import random
hand={
    "rock":
        '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

        '''
    ,"paper":
    '''
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    
    ''',

    "scissors":
    '''
    
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    
    '''
}
choice=input('rock, paper or scissors? : ').lower()
ran=random.choice(list(hand.keys()))
print("computer choice",hand[ran])
print("your choice",hand[choice])
if choice==ran:
    print("Drawn")
elif choice=='paper' and ran=='scissors':
    print("computer wins")


elif choice=='rock' and ran=='paper':
    print("computer wins")


elif choice=='scissors' and ran=='rock':
    print("computer wins")

else:
    print("you have won")



