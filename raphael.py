from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Raphael_(archangel)"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

for link in soup.find_all('a'):
    print("Link name: {} has appeared {} times".format(link.get('href'), str(len(link)+1)))
    