class Condition():
    def __init__(self):
        self.expression = ''

    def getExpression_sin(self):
        return "SELECT * FROM info_table WHERE " + self.expression

    def getExpression_comb(self):
        return self.expression


class EqualCondition(Condition):
    def __init__(self, property, input_string):
        Condition.__init__(self)
        self.expression = str(property) + "=" + input_string


class NotEqualCondition(Condition):
    def __init__(self, property, input_string):
        Condition.__init__(self)
        self.expression = str(property) + "!=" + input_string


class ContainCondition(Condition):
    def __init__(self, property, input_string):
        Condition.__init__(self)
        self.expression = "CONTAINS(" + str(property) + "," + input_string + ")"



class AndCondition(Condition):
    def __init__(self, *cond_list):
        Condition.__init__(self)
        self.expression = " AND ".join(i.getExpression_comb() for i in cond_list)


class OrCondition(Condition):
    def __init__(self, *cond_list):
        Condition.__init__(self)
        self.expression = " OR ".join(i.getExpression_comb() for i in cond_list)
