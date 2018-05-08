import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
text = "(14 + 6) * 2"
ast = parser.parse(text, lexer)

print ast
