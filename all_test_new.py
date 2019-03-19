from HTMLTestRunner import HTMLTestRunner
import unittest
import os, time

case_path = os.path.join(os.path.dirname(__file__), 'demo_unittest')
report_path = os.path.join(os.path.dirname(__file__), 'report')


def create_suite():
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
    print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTests(test_case)
    return suite


now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
filename = report_path+"/"+now+"_result.html"

with open(filename, 'wb') as fp:

    runner = HTMLTestRunner(
        stream=fp,
        title='接口测试报告',
        description='搜索用例执行情况：')

    runner.run(create_suite())
# fp.close()

