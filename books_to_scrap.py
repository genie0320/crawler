# %% [markdown]
# # 공통부분
# 목록 > 상세로 가면서 어차피 반복적으로 호출하게 될 코드를 함수로 만들었다.

# %%
from bs4 import BeautifulSoup
import requests


def go_to_page(url: str):
    URL = url
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
    return [response.status_code, soup]


# %%
start_url = "https://books.toscrape.com/index.html"
root_url = "https://books.toscrape.com/"  # 상세페이지 url이 상대경로인 경우 입력.

soup = go_to_page(start_url)
link_tags = soup[1].find_all("h3", limit=3)
links = []

#
for link in link_tags:
    link_ = link.find("a")["href"]
    links.append(root_url + link_)

for url in links:
    soup_detail = go_to_page(url)
    title = soup_detail[1].h1.text
    desc_tag = soup_detail[1].find("p", class_="")
    desc = desc_tag.text

    print(title)
    print(desc)
    print("*******************")
