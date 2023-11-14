import random
print('welcome to unscrambler!')
print('unscramble the following word!')
input('Press Enter to start')
print()

words = ['alive', 'arise', 'beach', 'board', 'cheer', 'chest', 'horse', 'learn']
newword=''
count=0


for word in range(len(words)):
    scrambled= "".join(random.sample(words[word],len(words[word])))
    print(f"Unscramble this: {scrambled}")
    guess=input("write here: ")

    if guess == words[word]:
        print("correct")
        count+=1
    else:
        print("wrong")
print(f"you scored {count}!")
if count<=len(words)/2:
    print("you're terrible")
else:
    print("you are good")