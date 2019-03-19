# -*- coding:utf-8 -*-
from parameterized import parameterized
import requests,unittest


class TestCaseSearch(unittest.TestCase):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Cookie': 'xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd;'
    }

    @parameterized.expand([
        ('pinyin', 'pdd'),
        ('hanzi', '拼多多'),
        ('4gezi', '阿里巴巴'),
        ('teshufuhao', '中国$@')
    ])
    def test_search2(self, _, data):
        url ='https://xueqiu.com/cube/search.json?q='+data+'&count=3&page=1'
        res = requests.get(url=url, headers=self.headers)
        assert 200 == res.status_code
        assert data in res.text
        assert 1 >= res.elapsed.total_seconds()

