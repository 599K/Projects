'''
Web scraper that extracts information from: https://www.nytimes.com/ and retrieves news in main page
'''

import requests
from bs4 import BeautifulSoup

def main():
    scrapper()


def scrapper():
    url = 'https://www.nytimes.com/'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    #first find the main container
    results = soup.find(id="site-content")
    #then find with the header, div... and the class id
    news_title = results.find_all('h3', class_ ="indicate-hover")

    for x, new in enumerate(news_title):
        print(f"News {x}: {new.text}.")


main()
