
# 1、放在当前的项目下，为了导包

import unittest
# 2、导入 HTMLTestRunner 类
from HTMLTestRunner import HTMLTestRunner

# 1、创建套件 E:\pythonProject\html_python
# suite = unittest.TestLoader().discover('../html_python', pattern='test*.py')
suite = unittest.TestLoader().discover(r'E:\pythonProject\html_python', pattern='test*.py')
# 生成文件
flname = 'test_report.html'
''' 
# 第一种写法
f = open(flname,'wb')
# 2、创建运行器
runner = HTMLTestRunner(f,title='测试报告',description='v1.0')
runner.run(suite)
# 关闭运行器
f.close()
'''
# 第二中写法，关键字：with 运行完自动关闭
with open(flname,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='v1.0')
    runner.run(suite)
