from lexer_rules import tokens
from expressions import *

def p_expression_plus(subexpr):
    'expression : expression PLUS term'
    subexpr[0] = subexpr[1] + subexpr[3]

def p_expression_term(subexpr):
    'expression : term'
    subexpr[0] = subexpr[1]

def p_term_times(subexpr):
    'term : term TIMES factor'
    subexpr[0] = subexpr[1] * subexpr[3]

def p_term_factor(subexpr):
    'term : factor'
    subexpr[0] = subexpr[1]

def p_factor_num(subexpr):
    'factor : NUMBER'
    subexpr[0] = subexpr[1]

def p_factor_expr(subexpr):
    'factor : LPAREN expression RPAREN'
    subexpr[0] = subexpr[2]

def p_error(subexpr):
    raise Exception("Syntax error.")
