import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

def go_to_page(url, head_info): #by requests
    URL = url
    HEADERS = head_info
    response = requests.get(URL, timeout=5, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')
    return [response.status_code, URL, soup, f'type: {type(soup)}']

def get_page_html(url, *args):
    result = []
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)  # 암시적 대기

    if args:
        for arg in args :
            # print(f'arg : {arg}')
            itms = (driver.find_elements(By.CSS_SELECTOR, f"{arg}"))
            res = [itm.text for itm in itms]
            result.append(res)
        return result, driver
    else : 
        html = driver.page_source
        save_html_to_txt(html, f"{url[:-5]}.txt")
        return html, driver

def bs_converter(html):
    title_tag = html.select_one('.prod_title')
    title = title_tag.text
    table_tag = html.find_all(class_='book_contents_list')
    _tt = table_tag[0].text
    content_table = str(_tt).split('<br/>')
    content_table_cleand = list(filter(lambda x: x.strip(), content_table))
    return [title,content_table_cleand]

def sl_converter(itms):
    title = itms[0][0]
    content_table = itms[1][0].split('\n1')
    content_table_cleand = list(filter(None, content_table))
    return [title,content_table_cleand]

def save_html_to_txt(content, file_name):
    now = time.time()
    # formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(now))
    # formatted_time = time.strftime("%H:%M:%S", time.gmtime(now))
    
    with open(f'{file_name}_{now}.txt', "w", encoding="utf-8") as file:
        file.write(str(content))

# _____________________________________ 설정 ______________________________________

# TODO: 변수명 정리하기
# TODO: 컨버터들 > 클래스사용할 수 있을지 알아보기

# _____________________________________ 스크랩시작 ______________________________________

soup_pot = go_to_page(start_url, headers)

soup = soup_pot[2]

# _____________________________________ 링크추출 ______________________________________

best_books = soup.find_all(class_='prod_info', limit=3)
books_url = []

for book in best_books:
    url = book['href'] 
    books_url.append(url)


# _____________________________________ 흐름제어 ______________________________________

books = []
for url in books_url:
    random_sec = random.uniform(3,5)
    time.sleep(random_sec)
        
    books_info = []
    content = go_to_page(url, headers)

    if not content[2].contents:
        s_books, browser= get_page_html(url, '.prod_title', '.book_contents_item')
        converted = sl_converter(s_books)
        # browser.close()
    else :
        converted = bs_converter(content[2])

    books.append(converted)
    print(converted,'************************************')

browser.quit()

# save_html_to_txt(books, 'books')

# _____________________________________ 인쇄설정 ______________________________________

# print(books_url)