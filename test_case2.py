
from controller import login


# 使用unittest框架来执行测试用例
import unittest

class TestLogin(unittest.TestCase):

    # @classmethod  # 类方法，标识一下
    # def setUpClass(cls) -> None:    # 在类前初始化工作
    #     print('----在类前初始化工作')
    # @classmethod  # 类方法，标识一下
    # def tearDownClass(cls) -> None:  # 在类后清除工作
    #     print('----在类后清除工作')
    #
    # # 在每个测试方法前初始化方法
    # def setUp(self) -> None:
    #     print("执行初始化工作")
    #
    # # 在每个测试方法后清空方法
    # def tearDown(self) -> None:
    #     print('执行清空工作')
    #
    # # assert '登录成功' == login('admin','123456')
    # # case1:验证正确的用户名和密码进行登录
    def test_login1(self):
        self.assertEqual('登录成功',login('admin','123456'))
        print('测试1')

    # case1:验证正确密码和空的用户名进行登录
    def test_login2(self):
        print('测试2')
        self.assertEqual('用户名不能为空',login('','12356'))

    # case1:验证正确的用户名和空的密码进行登录
    def test_login3(self):
        print('测试3')
        self.assertEqual('密码不能为空',login('admin',''))

'''
#  创建测试套件TestSuite，将测试用例放到套件中
suite = unittest.TestSuite()
# suite.addTest(TestLogin('test_login2'))
# suite.addTest(TestLogin('test_login3'))

case_list = [TestLogin('test_login2'),TestLogin('test_login3')]
suite.addTests(case_list)

# 调用运行器，运行测试用例
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
'''
