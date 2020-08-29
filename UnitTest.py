import unittest
from ColumnsName import *
from BaseCondition.baseCondition import *

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('所有测试用例已结束')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('\n测试开始')

    """
    单一功能模块测试用例 ： 5 个
    testcase1: equal功能测试
    testcase2: not equal 功能测试
    testcase3: contain 功能测试
    testcase4: and 功能测试
    testcase5: or 功能测试
    """
    def test_equal(self):
        input = EqualCondition(Property.NAME.value, "'NSW'")
        print(input.getExpression_sin())
        self.assertEqual("SELECT * FROM info_table WHERE name='NSW'", input.getExpression_sin())  # 测试用例

    def test_notequal(self):
        input = NotEqualCondition(Property.NAME.value, "'NSW'")
        print(input.getExpression_sin())
        self.assertEqual("SELECT * FROM info_table WHERE name!='NSW'", input.getExpression_sin())

    def test_contain(self):
        input = ContainCondition(Property.NAME.value, "'NSW'")
        print(input.getExpression_sin())
        self.assertEqual("SELECT * FROM info_table WHERE CONTAINS(name,'NSW')", input.getExpression_sin())

    def test_and(self):
        input1 = EqualCondition(Property.NAME.value, "'NSW'")
        input2 = NotEqualCondition(Property.COMPANYNAME.value, "'APPLE'")
        input = AndCondition(input1,input2)
        print(input.getExpression_sin())
        self.assertEqual("SELECT * FROM info_table WHERE name='NSW' AND companyName!='APPLE'",input.getExpression_sin())

    def test_or(self):
        input1 = EqualCondition(Property.NAME.value, "'NSW'")
        input2 = NotEqualCondition(Property.COMPANYNAME.value, "'APPLE'")
        input = OrCondition(input1, input2)
        print(input.getExpression_sin())
        self.assertEqual("SELECT * FROM info_table WHERE name='NSW' OR companyName!='APPLE'", input.getExpression_sin())
    """
    组合功能模块测试用例 ：
    testcase6: 多个条件通过AND链接
    testcase7: 多个条件通过OR 链接
    testcase8:  
    """
    def test_and_multi(self):
        input1 = EqualCondition(Property.NAME.value, "'NSW'")
        input2 = EqualCondition(Property.COMPANYNAME.value, "'APPLE'")
        input3 = EqualCondition(Property.TITLE.value,"'ENGINEER'")
        input4 = EqualCondition(Property.COUNTRY.value,"'CHINA'")
        input = AndCondition(input1,input2,input3,input4)
        print(input.getExpression_sin())
        self.assertEqual("SELECT * FROM info_table WHERE name='NSW' AND companyName='APPLE' AND title='ENGINEER' AND country='CHINA'",input.getExpression_sin())

    def test_or_multi(self):
        input1 = EqualCondition(Property.NAME.value, "'NSW'")
        input2 = EqualCondition(Property.COMPANYNAME.value, "'APPLE'")
        input3 = EqualCondition(Property.TITLE.value, "'ENGINEER'")
        input4 = EqualCondition(Property.COUNTRY.value, "'CHINA'")
        input = OrCondition(input1, input2, input3, input4)
        print(input.getExpression_sin())
        self.assertEqual(
            "SELECT * FROM info_table WHERE name='NSW' OR companyName='APPLE' OR title='ENGINEER' OR country='CHINA'",
            input.getExpression_sin())

    def test_comb_contain_and(self):
        input = ContainCondition()
        

if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
