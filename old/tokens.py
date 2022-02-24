from enum import Enum, auto

class TokenType(Enum):
    False_:int = auto()
    True_:int = auto()
    Plus:int = auto()
    Times:int = auto()
    Identifier:int = auto()
    Integer:int = auto()
    Float:int = auto()
    String:int = auto()
    LBracket:int = auto()
    Semicolon:int = auto()
    RBracket:int = auto()
    EOF:int = auto()


class Token(object):
    def __init__(self, _type:int, value:str, start_pos:int):
        self.type = _type
        self.value = value
        self.start_pos = start_pos

    def __repr__(self):
        #return f"({self.type}:`{self.value}`)"
        return f"Token({self.type}, \'{self.value}\', {self.start_pos})"
