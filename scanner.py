import ply.lex as lex
import sys

reserved = {
    'if': 'IF',
    'else': 'ELSE',

    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',

    'return': 'RETURN',

    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',

    'print': 'PRINT',
}

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

tokens = ['INTNUM', 'FLOATNUM', 'ID', 'STRING', 'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV', 'NOTEQ', 'LESSEQ', 'MOREEQ',
          'EQ', 'LESS', 'MORE', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'] + list(reserved.values())

t_EQ = r'=='
t_NOTEQ = r'!='
t_LESSEQ = r'<='
t_MOREEQ = r'>='
t_LESS = r'<'
t_MORE = r'>'
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'\-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='

literals = "=';()+-*/<>:[]{},"

def t_error(t):
    print("Error: Illegal character ->'%s'!" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_FLOATNUM(t):
    "\d+\.\d+|\.\d+|\d+\."
    try:
        t.value = float(t.value)
    except ValueError as err:
        if t.value.__str__().startswith('.'):
            t.value = float('0' + t.value.__str__())
        elif t.value.__str__().endswith('.'):
            t.value = float(t.value.__str__() + '0')
        else:
            raise err
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    "\".+\" | \'.+\'"
    t.value = str(t.value)
    t.value = t.value[1:len(t.value) - 1]
    return t


lexer = lex.lex()


def scan(text):
    lexer.input(text)
    return lexer


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "example.m"
    try:
        file = open(filename, "r")
        lexer.input(file.read())
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    for token in lexer:
        print("line %d: %s(%s)" % (token.lineno, token.type, token.value))
