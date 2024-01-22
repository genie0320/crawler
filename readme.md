

# mini Project : Title

## Overview
Desc.
Categoty : `input` `loop`

## Roadmap
- [ ] 배포해본다.
- [ ] exe로 만든다.
- [ ] 웹서비스로 만들어본다.
- [ ] GUI를 만든다.
- [ ] 패키지로 만든다.
- [ ] 설정항목을 따로 빼서 모은다.
- [ ] OOP를 적용해본다.
- [ ] csv, xlsx로 결과를 누적시켜본다.
- [ ] json로 결과를 export 해본다.
- [ ] decorator로 실행속도를 측정해본다.
- [ ] LLM 이랑 연결해본다.
- [ ] pip3 install fake-useragent 적용(https://pypi.org/project/fake-useragent/)


## Flow
1. Desc

## Resources
* item

* Versions   
Python 3.12.1   


## Issue
- [ ] Item 
- [x] Item


## Tips
```python
CLEAR = "\033[2J" # Clear terminal
CLEAR_AND_RETURN = "\033[H" # Clear termimal repeatedly

#Usage
print(CLEAR)
print(f'{CLEAR_AND_RETURN}{vals}Hellow!')
```

## .
## find & select
### select : can use css selector. OMG!!
```python
books_best = soup.select('.prod_info')
books_best = soup.select_one('.prod_info')
```
### find : good for find html tag and navigating.
```python
# find <html_tag>
tag = soup.find("html_tag")
tags = soup.find_all("html_tag") # (["html_tag", "html_tag"]) 
tags = soup.find_all(["html_tag", "html_tag"], limit=n) #n개까지만 찾아와라.

#filter
    # with Parameters
    tags = soup.find_all("html_tag", class_ = "example_class", data-type="important")

    # with dict
        tags = soup.find_all('div', {
            'class': 'example_class', 
            'data-type': 'important'
            })

    # with function 
    def custom_filter(tag):
        return tag.has_attr('data-important')

    filtered_elements = soup.find_all(custom_filter)

    #etc.
    #정규식
    tags = soup.find_all(text=re.compile("\$.*")) # $뒤에 뭐가 있든, 일단 $를 찾아라는 정규식. 특문앞에는 \붙이기.
```
[!NOTE] text='Hello' v. string='Hello'
string은 해당 값을 가진 직계'자식'만.
text는 어디에 있든 해당 값을 가진 모든 놈.





```
tag['attr'] = 'value' # Also can add attr
tag.attr # Show all attrs in tag
tag.strip() # 앞뒤공백 날리기
```

### File handling in python
```python
with open('name_of_file.txt', "w") as file:
    file.write(str(doc))
```
#### options
- 'r': Read mode. It opens the file for reading. If the file doesn't exist, it raises an **error**.
- 'w': Write mode. It opens the file for writing. If the file already exists, it truncates the file to zero length. If the file doesn't exist, it creates a new file.
- 'a': Append mode. It opens the file for writing, but it does not truncate the file. If the file doesn't exist, it creates a new file.
- 'b': Binary mode. It can be added to any of the above modes to work with binary data (e.g., 'rb', 'wb', 'ab').
- 'x': Exclusive creation. It creates a new file, but if the file already exists, the operation will **fail**.

[!TIP] read & write --> 'r+', 'w+'**


### Troubleshooting
#### 1. 한글이 깨질때
```
soup = BeautifulSoup(html, 'html.parser',from_encoding='cp949')
```



```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")  # 첫 번째 브라우저 창 열기

driver.execute_script("window.open('https://www.naver.com')")  # 두 번째 브라우저 창 열기

driver.close()  # 현재 활성화된 브라우저 창만 닫힘 / # 팝업도 이걸로 닫을 수 있음.

driver.get("https://www.daum.net")  # 첫 번째 창에서 여전히 가능

driver.quit()  # 모든 브라우저 창이 닫히고 WebDriver 종료
```

### WebDriverWait
특정 조건을 만족할 때까지 기다리는 데 사용
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

element.send_keys("안녕하세요!")

# until(): 지정된 조건이 만족될 때까지 기다립니다.
# until_not(): 지정된 조건이 만족되지 않을 때까지 기다립니다.
# until_presence_of_element_located(): 지정된 요소가 DOM에 나타날 때까지 기다립니다.
# until_not_presence_of_element_located(): 지정된 요소가 DOM에 나타나지 않을 때까지 기다립니다.
# until_element_to_be_clickable(): 지정된 요소가 클릭 가능할 때까지 기다립니다.
# until_not_element_to_be_clickable(): 지정된 요소가 클릭 가능하지 않을 때까지 기다립니다.
# until_text_to_be_present_in_element(): 지정된 요소의 텍스트에 지정된 문자열이 포함될 때까지 기다립니다.
# until_not_text_to_be_present_in_element(): 지정된 요소의 텍스트에 지정된 문자열이 포함되지 않을 때까지 기다립니다.
# until_attribute_to_be_present_in_element(): 지정된 요소의 속성에 지정된 값이 포함될 때까지 기다립니다.
# until_not_attribute_to_be_present_in_element(): 지정된 요소의 속성에 지정된 값이 포함되지 않을 때까지 기다립니다.
```

### expected_conditions as EC
WebDriverWait 클래스의 until() 메서드에 사용되는 조건을 정의
```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

element.send_keys("안녕하세요!")

# presence_of_element_located(): 지정된 요소가 DOM에 나타날 때까지 기다립니다.
# visibility_of_element_located(): 지정된 요소가 화면에 나타날 때까지 기다립니다.
# element_to_be_clickable(): 지정된 요소가 클릭 가능할 때까지 기다립니다.
# text_to_be_present_in_element(): 지정된 요소의 텍스트에 지정된 문자열이 포함될 때까지 기다립니다.
# text_to_be_present_in_element_value(): 지정된 요소의 value 속성에 지정된 문자열이 포함될 때까지 기다립니다.
# element_to_be_selected(): 지정된 요소가 선택되었을 때까지 기다립니다.
# element_to_be_selected_by_value(): 지정된 요소의 value 속성이 지정된 값으로 선택되었을 때까지 기다립니다.
# element_to_be_selected_by_partial_link_text(): 지정된 요소의 partialLinkText 속성이 지정된 문자열로 부분 일치할 때까지 기다립니다.
# element_to_be_selected_by_link_text(): 지정된 요소의 linkText 속성이 지정된 문자열로 일치할 때까지 기다립니다.
# frame_to_be_available_and_switch_to_it(): 지정된 프레임이 사용할 수 있을 때까지 기다리고 해당 프레임으로 전환합니다.
# alert_is_present(): 알림이 나타날 때까지 기다립니다.

```
### By ★★★★★
웹 페이지의 요소를 식별하는 데 사용되는 로케이터(locator)를 정의

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

element = driver.find_element(By.ID, "search")

element.send_keys("안녕하세요!")

# ID: 요소의 id 속성을 사용하여 요소를 식별합니다.
# NAME: 요소의 name 속성을 사용하여 요소를 식별합니다.
# XPATH: XPath 표현식을 사용하여 요소를 식별합니다.
# CSS_SELECTOR: CSS 선택자를 사용하여 요소를 식별합니다.
# TAG_NAME: 요소의 태그 이름을 사용하여 요소를 식별합니다.
# LINK_TEXT: 요소의 linkText 속성을 사용하여 요소를 식별합니다.
# PARTIAL_LINK_TEXT: 요소의 partialLinkText 속성을 사용하여 요소를 식별합니다.

```

### Options
Chrome 웹 브라우저의 설정을 구성하는 데 사용되는 Options 클래스를 가져오는 코드
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # 헤드리스 모드 활성화
options.add_argument("--start-maximized")  # 최대화된 창으로 시작
options.add_extension("path/to/extension.crx")  # 확장 프로그램 추가

driver = webdriver.Chrome(options=options)


```
- 브라우저 창 크기 조정: 창의 너비와 높이를 설정할 수 있습니다.
- 헤드리스 모드 실행: 브라우저 창을 표시하지 않고 브라우저를 실행할 수 있습니다.
- 시작 시 최대화: 브라우저 창을 최대화하여 시작할 수 있습니다.
- 특정 프로필 사용: 특정 Chrome 프로필을 사용하여 브라우저를 시작할 수 있습니다.
- 확장 프로그램 사용: Chrome 확장 프로그램을 추가할 수 있습니다.
- 자바스크립트 비활성화: JavaScript 실행을 비활성화할 수 있습니다.
- 플러그인 비활성화: 플러그인 실행을 비활성화할 수 있습니다.
- 인터넷 사용 기록 저장 비활성화: 인터넷 사용 기록 저장을 비활성화할 수 있습니다.
- 캐시 및 쿠키 비활성화: 캐시 및 쿠키 저장을 비활성화할 수 있습니다.
- 프록시 설정: 프록시 서버를 설정할 수 있습니다.

### Request / Response
response.content를 사용하는 방법이 약간 더 빠르지만 response.text를 사용하는 방법이 더 작다.
from_encoding='utf-8' 디코딩시 추가적인 메모리가 사용되지만 한글사이트는 뭐... 

```python
# 방법 1 : 디코딩할 필요없다면 이걸쓰자.
response = requests.get(URL, timeout=5, headers=HEADERS)
soup = BeautifulSoup(response, "html.parser")

# 방법 2 : 한국인은 이걸 써야...ㅠㅜ
response = requests.get(URL, timeout=5, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')


```

![standard-way-of-representing-selection-in-flowcharts](res_flow.png)   
[출처바로가기](https://stackoverflow.com/questions/71020681/standard-way-of-representing-selection-in-flowcharts)