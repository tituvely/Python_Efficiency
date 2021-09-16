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
    items = soup.select("#rso > div > div")
    
    for item in items:
        title = item.select("div > div > h3 > a")
        subject = title[0].text
        link = title.get("href")
        print ("%s\n - %s" % (subject, link))
        
        info = item.select("div > div.gG0TJc > div.slp")
        print ("%s" % info[0].text)

        content = item.select("div > div.gG0TJc > div.st")
        print ("%s" % content[0].text)

        print ("")

if __name__ == '__main__':
    main()