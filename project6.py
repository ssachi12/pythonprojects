#capital indexes
# def capital_indexes(x):
#     up=[]
#     for i in range(len(x)):
#         if x[i].isupper():
#             up.append(i)
#     return up
#
#
# upper=capital_indexes("HeLlO")
# print(upper)
##middle letter
# def mid(x):
#     if len(x)%2!=0:
#         l=len(x)//2
#         return x[l]
#     return "";
# s=mid("sachi")
# print(s)
##dictionary
# def online_count(x):
#     number=0
#     for i in x.values():
#        if i== 'online':
#            number+=1
#     return number
# dict={
#     "Alice":"online",
#     "bob":"offline",
#     "Eve":"online"
# }
# s=online_count(dict)
# print(s)
##randamness
# import random
# def random_number():
#     return random.randint(1,100)
# s=random_number()
# print(s)
##typecheck
# def only_ints(x,y):
#     return type(x)== int and type(y)== int
#
# s=only_ints(1,2)
# print(s)

##anagrams
def is_anagram(x,y):
    x1=list(x)
    y1=list(y)
    x1.sort()
    y1.sort()
    if x1== y1:
        return True
    else:
        return False
s=is_anagram("mad","dam")
print(s)