import requests
from bs4 import BeautifulSoup
import smtplib
re=requests.get('http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')

res=re.content

soup=BeautifulSoup(res, 'html.parser')
price=soup.find('p', class_='price_color').text[1:]
if price< 60:
  smt=smtplib.SMTP('smtp.mail.yahoo.com', 587)
  smt.ehlo()
  smt.starttls()
  smt.login(('sachinnaik964@gmail.com',''))
  smt.sendmail('sachinnaik964@gmail.com',
              ' sachin.d.naik964@gmail.com'
               f'Subject: Headphones price notifier\n\n, Hi price has dropped')
  smt.quit()



