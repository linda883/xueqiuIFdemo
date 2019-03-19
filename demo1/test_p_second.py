import requests
from bs4 import BeautifulSoup
import lxml
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Cookie': 'xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd;'
}
param = {'q': '中国平安', 'count': 3, 'page':1}
url = 'https://xueqiu.com/cube/search.json'
res = requests.get(url=url, headers=headers, params=param)
print(res.request.headers.get("Cookie"))
print(res.headers)
print(res.headers.get('Set-Cookie'))
result = res.json()
print(result['totalCount'])
assert 227 == result['totalCount']
print(result['list'][0]['name'])
assert '中国平安' in result['list'][-1]['name']




