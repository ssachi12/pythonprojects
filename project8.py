#datamuse ap
import requests

user=input("enter the word: ")
parameter={}
parameter['rel_rhy']=user;

request= requests.get('https://api.datamuse.com/words',
                   parameter)
words=request.json()
for i in words[0:3]:
    print(i['word'])


