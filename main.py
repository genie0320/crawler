from bs4 import BeautifulSoup
import requests
import time
import random

def go_to_page(url, head_info): 
    # random_sec = random.uniform(3,10)
    # time.sleep(random_sec)
    URL = url
    HEADERS = head_info
    response = requests.get(URL, timeout=5, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')
    return [response.status_code, URL, soup]

---

print(soup_pot[0], soup_pot[1])
print(soup_pot[2].h1)
soup = soup_pot[2]