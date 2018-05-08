tokens = ['NUMBER','PLUS','TIMES','LPAREN','RPAREN']

t_PLUS = r"\+"
t_TIMES = r"\*"
t_LPAREN = r"\("
t_RPAREN = r"\)"

def t_NUMBER(token):
    r"[1-9][0-9]*"
    token.value = int(token.value)
    return token

t_ignore_WHITESPACES = r"[ \t]+"

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

def t_error(token):
    message = "Token desconocido:"
    message = "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
