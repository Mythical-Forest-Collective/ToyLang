import std/[strutils]

const operators = @["+", "-", "*", "/"]

type UndefinedValueError* = object of Exception

type TokenType* = enum
  Number, # TODO: When feelibg better, make sure to replace the generic number
    # with floats and integers
  Integer,
  Float,
  String,
  Identifier,
  Null,
  True,
  False,
  Undefined,
  Operator,
  LParen,
  RParen,
  LBracket,
  RBracket,
  EOF

type Token* = object
  tpe: TokenType
  repr: string
  startPos: int


proc lex*(input: string): seq[Token] =
  var pos = 0
  var maxLen = input.len
  var tokens = newSeq[Token]()

  while pos < maxLen:
    let startPos = pos
    let cc = input[pos]
    if cc.isSpaceAscii:
      pos += 1

    elif cc.isDigit:
      var lexmeme = ""
      while pos < maxLen and (input[pos].isDigit or input[pos] == '.'):
        lexmeme &= $input[pos]
        pos += 1
      if '.' in lexmeme:
        tokens.add Token(tpe: TokenType.Float, repr: lexmeme, startPos: startPos)
        continue
      tokens.add Token(tpe: TokenType.Integer, repr: lexmeme, startPos: startPos)

    elif $cc in operators:
      tokens.add Token(tpe: TokenType.Operator, repr: $cc, startPos: startPos)
      pos += 1

    else:
      raise UndefinedValueError.newException("Can't lex this!")

  return tokens
