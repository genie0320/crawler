

# mini Project : Title

## Overview
Desc.
Categoty : `input` `loop`


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
    tags = soup.find_all(["html_tag"], class_ = "example_class", data-type="important")

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


