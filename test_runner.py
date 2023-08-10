import unittest
from BeautifulReport import BeautifulReport
import os
from datetime import datetime
from testCase import test_login  # 测试用例模块
from  jenkinsCon import configure_jenkins

target_path = 'reports'

def run_tests():
    # 创建测试套件
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_login.MyTestCase))

    # 生成报告
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(target_path, f"report_{current_time}.html")

    result = BeautifulReport(suite)
    result.report(filename=report_file, description='Test Report')

    return report_file

if __name__ == '__main__':
    report_file = run_tests()
    configure_jenkins(report_file)