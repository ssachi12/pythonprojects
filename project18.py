import random

sletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("welcome to password generator")
n_sletters=int(input("how many smaller case letters"))
n_cletters=int(input("how many capital case letters"))
n_number=int(input("how many numbers"))
n_symbols=int(input("how many symbols"))

password=''
for i in range(1, n_sletters+1):
    ran_sletters=random.choice(sletters)
    password+=ran_sletters

for i in range(1, n_cletters+1):
    ran_cletters=random.choice(cletters)
    password+=ran_cletters

for i in range(1, n_number+1):
    ran_numbers=random.choice(numbers)
    password+=ran_numbers

for i in range(1, n_symbols+1):
    ran_symbols=random.choice(symbols)
    password+=ran_symbols


print(password)

pass1=random.sample(password, len(password))

finalpass=''.join(pass1)

print(f"here is your password:\n{finalpass}")