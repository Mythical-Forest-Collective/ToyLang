from tokens import TokenType, Token

_operator = {
   "!" : lambda a: not a,
   "-" : lambda a: -a,
}


class Node: ...
class Statement(Node): ...
class Expression(Node): ...


class UndefinedLiteral(Expression):
    def __init__(self, token:Token):
        self.token = token

    def __repr__(self) -> str:
        return str(self.token.value)

    def __call__(self):
        return None

    def eval(self):
        try:
            return self()
        except ValueError:
            raise(f"Error converting {self.token.value} to {self.token.type}")


class NullLiteral(UndefinedLiteral):
    def __call__(self):
        return int(self.token.value)


class IntegerLiteral(UndefinedLiteral):
    def __call__(self):
        return int(self.token.value)


class FloatLiteral(UndefinedLiteral):
    def __call__(self):
        return float(self.token.value)


class StringLiteral(UndefinedLiteral):
    def __call__(self):
        return str(self.token.value)[1:-1]


class BooleanLiteral(UndefinedLiteral):
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

    def eval(self):
        try:
            return _operator[self.operator](self.right.eval())
        except TypeError:
            raise TypeError(f"can't perform `{self.operator}` on {self.right.token.type}")


type_literal_map = {
  TokenType.Integer:IntegerLiteral,
  TokenType.Float:FloatLiteral,
  TokenType.String:StringLiteral,
  TokenType.True_:BooleanLiteral,
  TokenType.False_:BooleanLiteral,
}

def literal(token:Token):
    return type_literal_map.get(token.type, UndefinedLiteral)(token)
