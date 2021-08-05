import unittest


# 在类中如果要使用unittest这个框架，那么类就必须继承unittest.TestCase

class UnitDemo(unittest.TestCase):
    def test_login(self):
        print("***** this is login function ****")
        # assert
        self.assertEqual("123", 123, msg="断言失败！")

if __name__ == '__main__':
    unittest.main()
