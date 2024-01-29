import requests
from bs4 import BeautifulSoup
import json

# Target URL
url = "https://www.nocutnews.co.kr/news/6083928"

# download the target page
page = requests.get(url)

# parse the HTML document returned by the server
# soup = BeautifulSoup(page.text, "lxml-xml") #이 방법이 더 빠르지만, bs4의 selector들이 잘 안먹는 에러가 있다.
soup = BeautifulSoup(page.text, "html.parser")

# initialize the object that will contain the scraped data
news_item = {}

# Scraping logic
# title of the news
title_html = soup.select_one("h2")
title = title_html.get_text().strip()
# Editor's comment
note_html = soup.select_one(".summary_l p")
note = note_html.get_text().strip()
# Main img URL
main_img = soup.select_one(".fr-img-wrap img")["src"]

# Article
article_html = soup.find("div", attrs={"itemprop": "articleBody"})
# Delete trashs in Article
_trash = article_html.find_all(["span", "div"])

for tag in _trash:  # Iterate through found elements
    tag.decompose()
# Structure setting before strip tag
sub_titles = article_html.find_all("h3")

for h3 in sub_titles:
    text = h3.text
    text = "##" + text
    h3.string = text

article = article_html
print(article)
print(article_html)


# !pip install -quiet beautifulsoup4 requests
