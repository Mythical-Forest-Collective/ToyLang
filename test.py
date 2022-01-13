from interpreter import Interpreter
from nodes import *

interpreter = Interpreter()

def test_literal(data, expected):
    token = interpreter.lex(data)[0]
    res = literal(token)
    print(f"{token}\n`{res}`")
    assert res() == expected, f"Got `{res()}` but expected `{expected}`"

test_literal('3', 3)
test_literal('"Yeet"', 'Yeet')
test_literal('3.3', 3.3)
