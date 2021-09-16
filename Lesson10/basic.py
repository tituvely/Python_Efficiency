import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

SEARCH_URL = "https://www.google.co.kr/search?tbm=nws&q=%s"

def main():
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' }
    
    search_keyword = quote("컴퓨터")
    url = SEARCH_URL % search_keyword

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html5lib")
    titles = soup.select("#rso > div > div > div > div > h3 > a")

    for title in titles:
        subject = title.text
        link = title.get("href")
        print ("%s\n - %s" % (subject, link))

if __name__ == '__main__':
    main()