import lexer_rules
from ply.lex import lex
text = "4 * (14 + 6) / (2 + 1)"
lexer = lex(module=lexer_rules)
lexer.input(text)
token = lexer.token()
while token is not None:
    print(token.type, token.value)
    token = lexer.token()
