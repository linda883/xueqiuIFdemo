# -*- coding:utf-8 -*-
import unittest2,requests
from ddt import ddt,file_data,unpack


@ddt
class TestSearch(unittest2.TestCase):

    @file_data("test.yml")
    @unpack
    def test_search(self, **kwargs):
        url = kwargs.get("url")
        method = kwargs.get("method")
        payload = kwargs.get("payload")
        headers = kwargs.get("header")
        # print(headers)
        # 验证的响应返回的（json），dict字典
        validate = kwargs.get("validate")
        print(validate)
#     必须所有接口用一个方法发送并验证
#         request方法是带session发送的
# verify=False是charles代理引起的
        res = requests.request(method=method, url=url, params=payload, headers=headers)
        # res_json = res.json()
        for k, v in validate.items():
            self.assertEqual(v, res.status_code)




