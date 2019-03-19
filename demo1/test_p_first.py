import requests
from bs4 import BeautifulSoup
import lxml
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
param = {'q':'中国平安'}
url = 'https://xueqiu.com/k'
html = requests.get(url=url, headers=headers, params=param).text

# 使用自带的html.parser解析，速度慢但通用
soup = BeautifulSoup(html, "html.parser")
soupl = BeautifulSoup(html, "lxml")
print(soupl)
assert '中国平安' in soupl.title.get_text()


