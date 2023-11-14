from newspaper import Article
import nltk
nltk.download('punkt')

url = input('enter the url here: ')
article=Article(url)
article.download()
article.parse()
author=article.authors
print(author)

