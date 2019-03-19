import requests
from bs4 import BeautifulSoup

url = 'https://xueqiu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Cookie': 'xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd'
}
html = requests.get(url=url, headers=headers).text
p_html = BeautifulSoup(html, 'lxml')
assert '雪球' in p_html.title.get_text()

