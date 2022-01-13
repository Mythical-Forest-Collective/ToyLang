from typing import List

from tokens import TokenType, Token

class Interpreter:
    def __init__(self):
        pass

    def lex(self, input:str) -> List[Token]:
        tokens:List[Token] = []
        current_pos:int = 0
        while current_pos < len(input):
            token_start_pos:int = current_pos
            lookahead:str = input[current_pos]

            if lookahead.isspace():
                current_pos += 1

            elif lookahead == '{':
                current_pos += 1
                tokens += [Token(TokenType.LBracket, lookahead, token_start_pos)]

            elif lookahead == ';':
                current_pos += 1
                tokens += [Token(TokenType.Semicolon, lookahead, token_start_pos)]

            elif lookahead == '}':
                current_pos += 1
                tokens += [Token(TokenType.RBracket, lookahead, token_start_pos)]

            elif lookahead == '+':
                current_pos += 1
                tokens += [Token(TokenType.Plus, lookahead, token_start_pos)]

            elif lookahead == '*':
                current_pos += 1
                tokens += [Token(TokenType.Times, lookahead, token_start_pos)]

            elif lookahead.isdigit():
                lexmeme = ''
                is_float = False
                while current_pos < len(input) and (input[current_pos].isdigit() or input[current_pos] == '.'):
                    if not is_float and input[current_pos] == '.':
                        is_float = True
                    lexmeme += input[current_pos]
                    current_pos += 1
                if not is_float:
                    tokens += [Token(TokenType.Integer, lexmeme, token_start_pos)]
                else:
                    tokens += [Token(TokenType.Float, lexmeme, token_start_pos)]

            elif lookahead == '"':
                current_pos += 1
                lexmeme = '"'
                while current_pos < len(input) and input[current_pos] != '"':
                    lexmeme += input[current_pos]
                    current_pos += 1
                lexmeme += '"'
                current_pos += 1
                tokens += [Token(TokenType.String, lexmeme, token_start_pos)]

            elif lookahead.isalpha():
                while current_pos < len(input) and input[current_pos].isalnum():
                    lexmeme += input[current_pos]
                    current_pos += 1
                if lexmeme == "true":
                    tpe = TokenType.True_
                elif lexmeme == "false":
                    tpe = TokenType.False_
                else:
                    tpe = TokenType.Identifier
                tokens += [Token(tpe, lexmeme, token_start_pos)]

            else:
                raise SyntaxError(f"Unknown character `{lookahead}` at position {current_pos}")
        tokens += [Token(TokenType.EOF, "<EOF>", current_pos)]
        return tokens

    def parse(self, tokens:List[Token]):
        ast_tree = []
