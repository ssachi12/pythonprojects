while True:
    q=input('Add (a) search (s) Quit (q)')
    if  q=='a':
        with open('contact.txt', 'a') as f:
            name= input('Name: ')
            phone =input('phone: ')
            f.writelines((name,':',phone,'\n'))
    elif q=='s':

       with open('contact.txt', 'r') as f:
          search=input('search: ')
          for i in f:
            if search in i:
               print(i)

