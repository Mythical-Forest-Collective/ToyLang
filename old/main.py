from interpreter import Interpreter

interpreter = Interpreter()

input = "\"Test\"682"
tokens = interpreter.lex(input)

print(*tokens, sep='\n')
