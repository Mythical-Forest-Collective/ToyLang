import std/[strutils,strformat]

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


proc lex*(sinput: string): seq[Token] =
  let input = sinput.strip(chars={'\n'})
  var pos = 0
  var maxLen = input.len
  var tokens = newSeq[Token]()

  while pos < maxLen:
    let startPos = pos
    let cc = input[pos]
    var tmp = cc
    if cc == '\n':
      echo "Character: `<Newline>`\nPosition: {pos}".fmt
    else:
      echo "Character: `{cc}`\nPosition: {pos}".fmt

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

    elif cc == ';':
      pos += 1
      tokens.add Token(tpe: TokenType.Semicolon, repr: ";", startPos: startPos)

    else:
      raise ValueError.newException(fmt"Can't lex character at position {startPos}! Character `{input[startPos]}`")

  return tokens
