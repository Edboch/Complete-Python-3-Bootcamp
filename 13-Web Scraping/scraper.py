import bs4
import requests
import lxml

resp= requests.get('https://en.wikipedia.org/wiki/Jonas_Salk')
# print(resp.text)
soup = bs4.BeautifulSoup(resp.text,'lxml')
print(soup.select('title')[0].getText())

