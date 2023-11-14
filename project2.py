#1- thousand  separator

def sep(num):
    print(f"{num:,}")
sep(2000000)

# #palindrom
# a=input("enter a word : ").lower().replace(" ","")
# b=a[::-1]
# if(a==b):
#     print("yay its a palindrome")
# else:
 #   print("nay its not a palindrom")
#
# #leap year
#
def leap(year):
 if year %4==0 and (year % 100 !=0 or year % 400 == 0):
     print("its a leap year")
 else:
     print("not a leap year")
n=int(input("enter the year : "))
leap(n)


