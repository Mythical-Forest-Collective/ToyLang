from interpreter import Interpreter

interpreter = Interpreter()

input = "3 * 2 + 1.12;\n"
tokens = interpreter.lex(input)

print(tokens)