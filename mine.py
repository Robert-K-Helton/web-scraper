import requests
from bs4 import BeautifulSoup

def smarty(links):
    text = []
    def posts_link(url):
        if posts in url:
            text.append(url)



    for link in links:
        print(link[' href '])


    return text

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')

print(smarty(links))