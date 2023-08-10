import unittest
from BeautifulReport import BeautifulReport
import os
from datetime import datetime
from testCase import test_login  # 导入包含测试用例的模块

if __name__ == '__main__':
    # 创建测试套件
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_login.MyTestCase))  # 将测试用例类添加到测试套件中

    # 获取当前时间
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 指定生成的 HTML 报告文件名，添加时间戳
    report_file = f"testCase_report_{current_time}.html"

    # 运行测试套件并生成 BeautifulReport 报告
    result = BeautifulReport(suite)
    result.report(filename=report_file, description='Test Report')

    # 指定报告的目标路径
    target_path = 'reports'

    # 如果目标路径不存在，则创建
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # 移动报告文件到目标路径
    os.rename(report_file, os.path.join(target_path, report_file))