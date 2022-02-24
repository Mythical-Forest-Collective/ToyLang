import std/[strutils]

const operators* = @["+", "-", "*", "/"]

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
  Semicolon,
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

    if cc.isSpaceAscii or cc == '\n':
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
      var lexmeme = ""
      while pos < maxLen and $input[pos] in operators:
        lexmeme &= $input[pos]
        pos += 1
      tokens.add Token(tpe: TokenType.Operator, repr: lexmeme, startPos: startPos)
      pos += 1

    elif cc == '"':
      var lexmeme = ""
      while pos < maxLen:
        lexmeme &= $input[pos]
        pos += 1
        if cc == '"' and startPos != pos-1:
          break
      tokens.add Token(tpe: TokenType.String, repr: lexmeme, startPos: startPos)
      pos += 1

    else:
      raise ValueError.newException("Can't lex this!")

  return tokens
