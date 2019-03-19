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
print(soupl.title, soupl.head, soupl.body)
# 或者soup = BeautifulSoup(html, "html5lib")
# 输出第一个 title 标签
# print(soup.title)
# # 输出第一个 title 标签的标签名称
# print(soup.title.name)
# # 输出第一个 title 标签的包含内容
# print(soup.title.string)
# # 输出第一个 title 标签的父标签的标签名称
# print(soup.title.parent.name)
# # 输出第一个  p 标签
# print(soup.p)
# # 输出第一个  p 标签的 class 属性内容
# print(soup.a['href'])
#
# # 输出第一个  a 标签
# print(soup.a)
# # 输出所有的  a 标签，以列表形式显示
# # print(soup.find_all('a'))
#
# # 输出第一个 id 属性等于  gz_gszze 的标签
# print(soup.find(id='app'))
# # 输出第一个 id 属性等于  gz_gszze 的标签的文本内容
# print(soup.find(id='app').get_text())
# print(soup.div)
# print(soup.div.get_text())
# print(soup.div.container.div['class'])
# app > div.container > div > div.search__hd
# print(soup.find(class_='search__hd').attrs)
# 第一个class = 'postlist'的div里的所有a 标签是我们要找的信息
# 注意：BeautifulSoup()返回的类型是<class 'bs4.BeautifulSoup'>
# 　 　find()返回的类型是<class 'bs4.element.Tag'>
# 　 　find_all()返回的类型是<class 'bs4.element.ResultSet'>
# 　 　<class 'bs4.element.ResultSet'>不能再进项find/find_all操作

# all_a = soup.find('div', class_='nav__dropdown__container').find_all('a', target='_blank')
# for a in all_a:
#     title = a.get_text()  # 提取文本
#     if (title != ''):
#         print("标题：" + title)

# #正则 re.findall  的简单用法（返回string中所有与pattern相匹配的全部字串，返回形式为数组），用法：findall(pattern, string, flags=0)
# #示例1：查找全部r标识代表后面是正则的语句
# str_1 = re.findall(r"com","http://www.cnblogs.com/lizm166/p/8143231.html")
# print (str_1)
# #输出结果：['com']
#
# #示例2：符号^表示匹配以http开头的的字符串返回,
# str_2 = re.findall(r"^http","http://www.cnblogs.com/lizm166/p/8143231.html")
# print (str_2)
# # 输出结果：['http']
#
# #示例3：用$符号表示以html结尾的字符串返回,判断是否字符串结束的字符串
# str_3 = re.findall(r"html$","http://www.cnblogs.com/lizm166/p/8143231.html")
# print (str_3)
# # 输出结果：['html']

#查找dl标签class为包含'ui-font-'字符的所有dl标签
# print(soup.find_all(class_=re.compile('search')))
# #app > div.container > div > div.search__hd
# for tagspan in soup.find_all("div", class_=re.compile('search_')):
#     print(tagspan.get_text())

