import requests
import bs4

response = requests.get('http://quotes.toscrape.com/')
print(response)
soup = bs4.BeautifulSoup(response.text,'lxml')
authors = set()
for author in soup.select('.author'):
    authors.add(author.get_text())
# print(authors)

quotes = []

for quote in soup.select('.text'):
    quotes.append(quote.text)
# print(quotes)

tags = []
for tag in soup.select('.tag-item'):
    tags.append(tag.select('.tag')[0].getText())
# print(tags)

class LastPageException(Exception):
    "Raised when there are no more pages to explore"

page_count = 1
while True:
    try:
       response = requests.get('http://quotes.toscrape.com/page/{}'.format(page_count)) 
       if "No quotes found!" in response.text:
           raise LastPageException
       soup = bs4.BeautifulSoup(response.text,'lxml')
       for author in soup.select('.author'):
           authors.add(author.get_text())
    except LastPageException:
        print('reached the end')
        break
    finally:
        page_count+=1
print(authors)