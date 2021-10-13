
from controller import login

# 使用unittest框架来执行测试用例
import unittest

class TestLogin(unittest.TestCase):

    # case1:验证正确的用户名和密码进行登录
    def test_login1(self):
        self.assertEqual('登录成功',login('admin','123456'))
        print('测试4')

    # case1:验证正确密码和空的用户名进行登录
    def test_login2(self):
        print('测试5')
        self.assertEqual('用户名不能为空',login('','12356'))

    # case1:验证正确的用户名和空的密码进行登录
    def test_login3(self):
        print('测试6')
        self.assertEqual('密码不能为空',login('admin',''))

