import requests

params = {'symbol': 'SH000001,SZ399001,SZ399006,HKHSI,HKHSCEI,HKHSCCI,.DJI,.IXIC,.INX'}
url = 'https://stock.xueqiu.com/v5/stock/batch/quote.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Cookie': 'xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd'
}
res = requests.get(url=url, params=params,headers=headers)
print(res.text)
