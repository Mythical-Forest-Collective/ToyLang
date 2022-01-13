from tokens import TokenType, Token

_operator = {
   "!" : lambda a: not a,
   "-" : lambda a: -a,
}


class Node: ...
class Statement(Node): ...
class Expression(Node): ...


class NullLiteral(Expression):
    def __init__(self, token:Token, value:str):
        self.token = token
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def __call__(self):
        return None

    def eval(self):
        try:
            return self()
        except ValueError:
            raise(f"Error converting {self.value} to {self.type}")


class IntegerLiteral(NullLiteral):
    def __call__(self):
        return int(self.value)


class FloatLiteral(NullLiteral):
    def __call__(self):
        return float(self.value)


class StringLiteral(NullLiteral):
    def __call__(self):
        return str(self.value)[1:-1]


class BooleanLiteral(NullLiteral):
    def __call__(self):
        if self.token.type == TokenType.False_:
            return False
        else:
            return True


class PrefixExpression(Expression):
    def __init__(self, operator:Statement, right:Expression):
        self.operator = operator
        self.right = right

    def __repr__(self) -> str:
        return f"({self.operator}{self.right})"

    def get_type(self) -> str:
        return self.right.token.type

    def eval(self):
        try:
            return _operator[self.operator](self.right.eval())
        except TypeError:
            raise TypeError(f"can't perform {self.operator} between {self.left_type()} and  {self.left_type()}")


def literal(token:Token, type:TokenType, value:str):
    if token
