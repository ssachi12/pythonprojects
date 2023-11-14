import random

rolls= [
    '''
-----
|   |
| o |
|   |
-----
    ''',
    '''
    
-----
|o  |
|   |
|  o|
-----
    
    ''',
    '''
    
-----
|o  |
| o |
|  o|
-----
    
    ''',
    '''
    
-----
|o o|
|   |
|o o|
-----
    
    ''',
    '''
    
-----
|o o|
| o |
|o o|
-----
    
    ''',
    '''
    
-----
|o o|
|o o|
|o o|
-----
  
    '''
]
while True:
    input("press enter to start")

    dice1= random.randint(0,5)
    dice2= random.randint(0,5)
    print(f"player one: \n {rolls[dice1]}\nplayer two:\n {rolls[dice2]}")

    if dice1>dice2:
        print("player 1 is the winner")
    elif dice2>dice1:
        print("player 2 is the winner")
    else:
        print("drawn")