# %%
# import _scapAngel as sa
import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# from fake_useragent import UserAgent


# %%
def go_to_page(url, head_info):  # by requests
    URL = url
    HEADERS = head_info
    response = requests.get(URL, timeout=5, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
    return [response.status_code, URL, soup, f"type: {type(soup)}"]


def get_page_html(url, *args):  # by selenium
    result = []
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)  # 암시적 대기

    if args:
        for arg in args:
            # print(f'arg : {arg}')
            itms = driver.find_elements(By.CSS_SELECTOR, f"{arg}")
            res = [itm.text for itm in itms]
            result.append(res)
        return result, driver
    else:
        html = driver.page_source
        save_html_to_txt(html, f"{url[:-5]}.txt")
        return html, driver


def bs_converter(html, url):
    title_tag = html.select_one(".prod_title")
    if title_tag:
        title = title_tag.text
        table_tag = html.find_all(class_="book_contents_list")
        _tt = table_tag[0].text
        content_table = str(_tt).split("<br/>")
        content_table_cleand = list(filter(lambda x: x.strip(), content_table))
        return [title, content_table_cleand]
    else:
        print(f"error : {url}")
        return [f"●●●●●● error : {url}"]


def sl_converter(itms):
    title = itms[0][0]
    content_table = itms[1][0].split("\n1")
    content_table_cleand = list(filter(None, content_table))
    return [title, content_table_cleand]


def save_html_to_txt(content, file_name):
    now = time.time()
    # formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(now))
    # formatted_time = time.strftime("%H:%M:%S", time.gmtime(now))

    with open(f"{file_name}_{now}.txt", "w", encoding="utf-8") as file:
        file.write(str(content))


# %%
keyword = ""
start_url = (
    f"https://search.kyobobook.co.kr/search?keyword={keyword}&gbCode=TOT&target=total"
)
root_url = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

options = Options()
options.headers = headers
options.add_experimental_option("detach", True)

# %%
soup_pot = go_to_page(start_url, headers)

# print(soup_pot[0], soup_pot[1])
# print(soup_pot[2].h1)

soup = soup_pot[2]

# %%
best_books = soup.find_all(class_="prod_info", limit=1)
books_url = []

for book in best_books:
    url = book["href"]
    books_url.append(url)

# print(books_url)
# %%
books = []
for url in books_url:
    random_sec = random.uniform(3, 5)
    time.sleep(random_sec)

    books_info = []
    content = go_to_page(url, headers)

    if not content[2].contents:
        s_books, browser = get_page_html(url, ".prod_title", ".book_contents_item")
        converted = [sl_converter(s_books)]
        # browser.close()
    else:
        converted = [bs_converter(content[2], url)]

    converted.append(url)
    books.append(converted)
    print(converted[1], converted[0], "************************************")

browser.quit()

save_html_to_txt(books, "books")
