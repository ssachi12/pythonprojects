email=input("enter your email: ")
ind=email.index('@')
if email.count('@')==1 and len(email[:ind])>0 and len(email[ind+1:]>3):
    print("your username is: ", email[:ind])
    print("your domain ID is: ",email[ind+1:])

else:
    print("invalid email")