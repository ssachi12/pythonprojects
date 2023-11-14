from bs4 import BeautifulSoup
import pandas as pd
import requests

url="https://pythonology.eu/what-is-syntax-in-programming-and-linguistics/"

res=requests.get(url).text
soup= BeautifulSoup(res, 'html.parser')
bad =[]
good= []
keywords=[]
title= soup.find('title')
if title:
    good.append(f"Title exists: {title}")
else:
    bad.append(("no title"))

#meta
meta_d=soup.find('meta', attrs={'name':'description'})['content']
if meta_d:
    good.append(f"meta description exists: {meta_d}")
else:
    bad.append(("no meta description"))

#headings
hs=['h1','h2','h3']
h_tags=[]
for h in soup.find_all(hs):
    good.append(f"{h.name}-->{h.text.strip()}")
    h_tags.append(h.name)
if 'h1' not in h_tags:
    bad.append("no h1 found")

#images alt

for i in soup.find_all('img', alt=''):
    bad.append(f"No Alt: {i}")
print(good)
print("==========")
print(bad)
