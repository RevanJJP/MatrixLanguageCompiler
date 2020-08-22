import scanner
import ply.yacc as yacc
from AST import *

reserved = scanner.reserved
tokens = scanner.tokens
lexer = scanner.lexer

precedence = (
    ("nonassoc", 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
    ('left', 'IF'),
    ('left', 'ELSE')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_start(p):
    """start : instruction_set"""
    p[0] = Start(p.lineno(1), p[1])


def p_instruction(p):
    """instruction : expression
                | conditional
                | loopconditional"""
    p[0] = Instruction(p.lineno(1), p[1])


def p_instruction_set(p):
    """instruction_set : instruction instruction_set
                    | '{' instruction_set '}'
                    | """
    if len(p) == 3:
        p[0] = InstructionSet(p.lineno(1), p[1], p[2])
    elif len(p) == 4 and p[1] == '{' and p[3] == '}':
        p[0] = InstructionSet(p.lineno(1), None, p[2])
    else:
        p[0] = InstructionSet(p.lineno(0), None, None)


def p_identifier(p):
    """identifier : ID
                | address"""
    p[0] = Identifier(p.lineno(1), p[1])


def p_expression(p):
    """expression : assignment ";"
                | operation ';'"""
    p[0] = Expression(p.lineno(1), p[1])


def p_assignment(p):
    """assignment : identifier '=' operand
                | identifier '=' operation
                | identifier assignoperation operand
                | identifier assignoperation operation"""
    p[0] = Assignment(p.lineno(1), p[2], p[1], p[3])


def p_operation(p):
    """operation : operand operator operand
                | operand operator operation
                | function '(' operand ')'
                | function '(' operation ')'
                | reservedoperation
                | operand selfoperator"""
    if len(p) == 4:
        p[0] = Operation(p.lineno(1), p[2], p[1], p[3])
    elif len(p) == 5 and p[2] == '(' and p[4] == ')':
        p[0] = Operation(p.lineno(1), p[1], p[3], None)
    elif len(p) == 2:
        p[0] = Operation(p.lineno(1), p[1], None, None)
    elif len(p) == 3:
        p[0] = Operation(p.lineno(1), p[2], p[1], None)


def p_assignoperation(p):
    """assignoperation : ADDASSIGN
                        | SUBASSIGN
                        | MULASSIGN
                        | DIVASSIGN"""
    p[0] = AssignOperation(p.lineno(1), p[1])


def p_operand(p):
    """operand : identifier
            | number
            | structure
            | '-' operand %prec UMINUS
            | address"""
    if len(p) == 2:
        p[0] = Operand(p.lineno(1), p[1])
    elif p[1] == '-':
        p[0] = Operand(p.lineno(1), -p[2])


def p_standard_operators(p):
    """operator : '+'
                | '-'
                | '*'
                | '/'"""
    p[0] = Operator(p.lineno(1), p[1])


def p_dot_operators(p):
    """operator : DOTADD
                | DOTSUB
                | DOTMUL
                | DOTDIV"""
    p[0] = MatrixOperator(p.lineno(1), p[1])


def p_selfoperator(p):
    """selfoperator : "'" """
    p[0] = SelfOperator(p.lineno(1), p[1])


def p_function(p):
    """function : ZEROS
                | ONES
                | EYE"""
    p[0] = Function(p.lineno(1), p[1])


def p_reserved_operation(p):
    """reservedoperation : RETURN operation
                    | RETURN operand
                    | RETURN
                    | PRINT series
                    | PRINT operation
                    | PRINT operand
                    | BREAK
                    | CONTINUE"""
    if len(p) == 2:
        p[0] = ReservedOperation(p.lineno(1), p[1], None, None)
    elif len(p) == 3:
        p[0] = ReservedOperation(p.lineno(1), p[1], p[2], None)


def p_relation(p):
    """relation : EQ
                | NOTEQ
                | LESS
                | LESSEQ
                | MORE
                | MOREEQ"""
    p[0] = Relation(p.lineno(1), p[1])


def p_condition(p):
    """condition : operand relation operand
                | operation relation operand
                | operand relation operation
                | operation relation operation"""
    p[0] = Condition(p.lineno(1), p[2], p[1], p[3])


def p_conditional(p):
    """conditional : IF '(' condition ')' instruction
    | IF '(' condition ')' '{' instruction_set '}'
    | IF '(' condition ')' instruction ELSE instruction
    | IF '(' condition ')' '{' instruction_set '}' ELSE instruction
    | IF '(' condition ')' instruction ELSE '{' instruction_set '}'
    | IF '(' condition ')' '{' instruction_set '}' ELSE '{' instruction_set '}'"""

    if len(p) == 6:
        p[0] = Conditional(p.lineno(1), p[3], p[5], None)
    elif len(p) == 8 and p[5] == '{' and p[7] == "}":
        p[0] = Conditional(p.lineno(1), p[3], p[6], None)
    elif len(p) == 8 and p[6].upper() == 'ELSE':
        p[0] = Conditional(p.lineno(1), p[3], p[5], p[7])
    elif len(p) == 10 and p[8].upper() == 'ELSE' and p[5] == '{' and p[7] == "}":
        p[0] = Conditional(p.lineno(1), p[3], p[6], p[9])
    elif len(p) == 10 and p[6].upper() == 'ELSE' and p[7] == '{' and p[9] == "}":
        p[0] = Conditional(p.lineno(1), p[3], p[5], p[8])
    elif len(p) == 12 and p[8].upper() == 'ELSE' and p[5] == '{' and p[7] == "}" and p[9] == '{' and p[11] == "}":
        p[0] = Conditional(p.lineno(1), p[3], p[6], p[8])


def p_loopconditional(p):
    """loopconditional : WHILE '(' condition ')' instruction
    | WHILE '(' condition ')' '{' instruction_set '}'
    | FOR identifier '=' range instruction
    | FOR identifier '=' range '{' instruction_set '}' """
    if len(p) == 6 and p[1].upper() == 'WHILE':
        p[0] = LoopConditional(p.lineno(1), p[3], p[5], None, None, "WHILE")
    elif len(p) == 8 and p[1].upper() == 'WHILE' and p[5] == '{' and p[7] == "}":
        p[0] = LoopConditional(p.lineno(1), p[3], p[6], None, None, "WHILE")
    if len(p) == 6 and p[1].upper() == 'FOR':
        p[0] = LoopConditional(p.lineno(1), None, p[5], p[2], p[4], "FOR")
    if len(p) == 8 and p[1].upper() == 'FOR' and p[5] == '{' and p[7] == "}":
        p[0] = LoopConditional(p.lineno(1), None, p[6], p[2], p[4], "FOR")


def p_range(p):
    """range : operand ':' operand"""
    p[0] = Range(p.lineno(1), p[1], p[3])


def p_structure(p):
    """structure : matrix
                | STRING"""
    p[0] = Structure(p.lineno(1), p[1])


def p_matrix(p):
    """matrix : rows
            | '[' rows ']'"""
    if len(p) == 2:
        p[0] = Matrix(p.lineno(1), p[1], True)
    if len(p) == 4:
        p[0] = Matrix(p.lineno(2), p[2])


def p_rows(p):
    """rows : '[' series ']'
    | '[' series ']' ',' rows"""
    if len(p) == 4:
        p[0] = Rows(p.lineno(1), p[2], None)
    elif len(p) == 6 and p[4] == ',':
        p[0] = Rows(p.lineno(1), p[2], p[5])


def p_series(p):
    """series : operand
            | operand ',' series"""
    if len(p) == 2:
        p[0] = Series(p.lineno(1), p[1], None)
    elif len(p) == 4 and p[2] == ',':
        p[0] = Series(p.lineno(1), p[1], p[3])


def p_integer_series(p):
    """integer_series : number
                    | number ',' integer_series"""
    if len(p) == 2:
        p[0] = IntegerSeries(p.lineno(1), p[1], None)
    elif len(p) == 4 and p[2] == ',':
        p[0] = IntegerSeries(p.lineno(1), p[1], p[3])


def p_number(p):
    """number : INTNUM
            | FLOATNUM"""
    p[0] = Number(p.lineno(1), p[1])


def p_address(p):
    """address : identifier '[' integer_series ']'"""
    p[0] = Address(p.lineno(1), p[1], p[3])

parser = yacc.yacc()
