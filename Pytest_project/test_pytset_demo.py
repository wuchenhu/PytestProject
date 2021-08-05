import pytest

'''
    Pytest中模块的名字必须以test开头命名test*.py，否则运行程序时找不到文件。
    pytest将在当前目录及其子目录中运行所有格式为test_*.py或者*._test.py文件
    Pytest 框架中的用力也是test开头或者test结尾的。
    最后回实现要给错误截图上传的功能。
'''


def test_01():
    print("**** this is test 01 ****")
    assert 1 ==1

if __name__ == '__main__':
    pytest.main(['-sv','test_pytest.demo.py'])