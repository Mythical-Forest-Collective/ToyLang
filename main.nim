import interpreter/[lexer]

proc runFromFile(f: string) =
  let tokens = readFile(f).lex
  echo tokens

runFromFile "main.tl"
