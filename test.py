from nodes import *

def test_literal(data, expected):
    received = Literal(*data)
    typ, string, value = expected
    if typ != received.get_type():
        assert False, f"name error: expected: {typ}, Received:{received.get_type()}" 
    if value != received.eval():
        assert False, f"value error: expected: {value}, Received:{received.eval()}" 
    if string != received.__repr__():
        assert False, f"value error: expected: {string}, Received:{received}"
