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