from tokens import TokenType, Token

class Node:  ...
class Statement(Node): ...
class Expression(Node): ...

class Literal(Expression):
    def __init__(self, token:Token, _type:TokenType, value:str):
        self.token =token
        self.type = _type
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def type_casting(self):
        if self.type == TokenType.Integer:
            return int(self.value)
        elif self.type == TokenType.Float:
            return float(self.value)
        elif self.type ==  TokenType.String:
            return str(self.value)[1:-1]
        elif self.type == TokenType.True_:
            return True 
        elif self.type == TokenType.False_:
            return False
        return None
        
    def eval(self):
        try:
            out = self.type_casting()
        except ValueError:
            raise(f"Error converting {self.value} to {self.type}")
        return out

class IntegerLiteral(Literal): ...