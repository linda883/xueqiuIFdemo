from parameterized import parameterized_class
import unittest,requests


@parameterized_class([
   {"q": "拼多多", "count": 3, "page": 1},
   {"q": "中国平安", "count": 3, "page": 2},
])
class TestMathClassDict(unittest.TestCase):
    def setUp(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': 'xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd;'
        }

    def test_subtract(self):
        url = '''https://xueqiu.com/cube/search.json?q=%s&count=%s&page=%s''' % (self.q, self.count, self.page)
        res = requests.get(url=url, headers=self.headers)
        print(res.text)


