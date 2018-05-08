class Expression(object):
    def evaluate(self):
        # Aca se implementa cada tipo de expresion.
        raise NotImplementedError

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class BinaryOperation(Expression):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator
        
    def evaluate(self):
        res_l = self.left.evaluate()
        res_r = self.right.evaluate()
        return self.operator(res_l, res_r)
