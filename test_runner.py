import unittest
import HtmlTestRun
import test

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMath))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestSearch))
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    runner.run(suite)