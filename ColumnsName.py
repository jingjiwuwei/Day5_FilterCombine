from enum import Enum
class Property(Enum):
    COMPANYNAME = 'companyName'
    NAME = 'name'
    TITLE = 'title'
    COUNTRY = 'country'
from BaseCondition.baseCondition import *

test = EqualCondition("name","amy")
print(test.getExpression_sin())
test1 = EqualCondition("name","amy")
test2 = EqualCondition("name","bob")
test3 = AndCondition(test,test1,test2)

print(test3.getExpression_sin())