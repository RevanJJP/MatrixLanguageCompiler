from collections import defaultdict
import AST
from SymbolTable import *

LOOP_COUNT = 0


ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
for op in ['+', '-', '*', '/', '%']:
    ttype[op]['int']['int'] = 'int'

for op in  ['<', '>', '<=', '>=', '==', '!=']:
    ttype[op]['int']['int'] = 'bool'
    ttype[op]['int']['float'] = 'bool'
    ttype[op]['float']['int'] = 'bool'
    ttype[op]['float']['float'] = 'bool'

for op in ['+', '-', '*', '/']:
    ttype[op]['int']['float'] = 'float'
    ttype[op]['float']['int'] = 'float'
    ttype[op]['float']['float'] = 'float'

for op in ['<', '>', '<=', '>=', '==', '!=']:
    ttype[op]['int']['float'] = 'int'
    ttype[op]['float']['int'] = 'int'
    ttype[op]['float']['float'] = 'int'

ttype['+']['string']['string'] = 'string'
ttype['*']['string']['int'] = 'string'

for op in ['<', '>', '<=', '>=', '==', '!=']:
    ttype[op]['string']['string'] = 'int'

for op in ['.+', '.-', './', '.*']:
    ttype[op]['matrix']['matrix'] = 'matrix'

for op in ['*', '/']:
    ttype[op]['matrix']['int'] = 'matrix'
    ttype[op]['matrix']['float'] = 'matrix'
    ttype[op]['int']['matrix'] = 'matrix'


def get_type(operation, left_operand_type, right_operand_type) -> str:
    return ttype[operation][left_operand_type][right_operand_type]


def log(msg, node, msg_type=None):
    if msg_type:
        pass
    else:
        print("At " + node.line_no.__str__() + ": " + msg.__str__())


class NodeVisitor(object):

    def visit(self, node, table=None, args=None):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        if args is None:
            return visitor(node, table)
        else:
            return visitor(node, table, args)

    def generic_visit(self, node, table):
        if isinstance(node, list):
            for elem in node:
                self.visit(elem, table)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item, table)
                elif isinstance(child, AST.Node):
                    self.visit(child, table)
                else:
                    print(node)


class TypeChecker(NodeVisitor):
    def __init__(self):
        self.isValid = True

    def visit_Start(self, node, table=None):
        table = SymbolTable(None, 'start')
        self.visit(node.instruction_set, table)

    def visit_Instruction(self, node, table):
        self.visit(node.expr, table)

    def visit_InstructionSet(self, node, table):
        if node.instruction:
            self.visit(node.instruction, table)
        if node.instruction_rest:
            self.visit(node.instruction_rest, table)

    def visit_Expression(self, node, table):
        self.visit(node.expr, table)

    def visit_Identifier(self, node, table, fail_if_not_exist=True):
        if type(node.identifier) is AST.Address:
            var = table.get(node.identifier.identifier.identifier)

            if var is not None:
                return var.matrix_type, var
            elif fail_if_not_exist is True:
                log("Variable {0} doesn't exist!".format(node.identifier), node)
                self.isValid = False
            else:
                return None, None
        else:
            var = table.get(node.identifier)

            if var is not None:
                return var.type, var
            elif fail_if_not_exist is True:
                log("Variable {0} doesn't exist!".format(node.identifier), node)
                self.isValid = False
            else:
                return None, None

    def visit_Assignment(self, node, table):
        if node.identifier.type == 'identifier':
            _id = node.identifier
        else:
            log("Assignment to a non-variable!", node.identifier)
            self.isValid = False
            return None

        var_type, var = self.visit(_id, table, False)

        if node.operand is not None:
            r_type = self.visit(node.operand, table)
        else:
            log("Assignment to nothing!", node)
            self.isValid = False
            return None

        if var is None:
            if node.operator == '=':
                if r_type == 'matrix':
                    r_type, matrix = self.visit(node.operand, table, True)
                    matrix.name = _id.identifier
                    table.put(_id.identifier, matrix)
                elif r_type is not None:
                    table.put(_id.identifier, VariableSymbol(_id, r_type))
                else:
                    log("Wrong assignment!", _id)
                    self.isValid = False
            else:
                log("Variable not assigned.", _id)
                self.isValid = False
        else:
            if node.operator == '=':
                if var_type == r_type:
                    pass
                else:
                    log("Bad assignment of {0} ({1}). Types don't match.".format(_id.identifier, var_type), _id)
                    self.isValid = False
            else:
                _op = self.visit(node.operator, table)

                return_type = None

                if _op.type == "assignoperation":
                    if _op.operator == "+=":
                        return_type = get_type('+', var_type, r_type)
                    elif _op.operator == "-=":
                        return_type = get_type('-', var_type, r_type)
                    elif _op.operator == "*=":
                        return_type = get_type('*', var_type, r_type)
                    elif _op.operator == "/=":
                        return_type = get_type('/', var_type, r_type)
                else:
                    return_type = get_type(_op, var_type, r_type)

                if return_type is None:
                    log("Bad assignment. Wrong assign operation.", _op)
                    self.isValid = False
                elif return_type != var_type:
                    log("Bad assign operation in {0} ({1}). Types don't match.".format(_id.identifier, var_type), _id)
                    self.isValid = False
                else:
                    pass

    def visit_Operation(self, node, table, require_tuple=False):
        _op = self.visit(node.operator, table)
        if node.operator.type == 'reservedoperation':
            pass
            return None

        op_type = None
        l_type = None
        r_type = None

        if _op.type:
            op_type = _op.type

        if node.left_operand:
            l_type = self.visit(node.left_operand, table)
        if node.right_operand:
            r_type = self.visit(node.right_operand, table)

        if op_type == "selfoperator":
            if node.left_operand is not None and _op.operator == "'":
                if node.left_operand.value.type == 'identifier':
                    var = table.get(node.left_operand.value.identifier)
                    if var.type == 'matrix':
                        if require_tuple is False:
                            return 'matrix'
                        else:
                            return 'matrix', MatrixSymbol("none", 'int', var.column, var.row)
                    else:
                        log("Variable {0} ({1}) has to be a matrix!".format(l_type.identifier, var.type), l_type)
                        self.isValid = False
                elif l_type == 'matrix':
                    pass
                else:
                    log("Transpose operator requires matrix!", _op)
                    self.isValid = False
            else:
                log("Self operator requires operand!", _op)
                self.isValid = False
        elif op_type == "function":
            if _op.operator == 'eye' or 'zeros' or 'ones':
                if node.left_operand is not None:
                    if l_type != 'int':
                        log("Matrix init function requires int type argument!", _op)
                        self.isValid = False
                    else:
                        size = node.left_operand.value.number
                        if require_tuple is False:
                            return 'matrix'
                        else:
                            return 'matrix', MatrixSymbol("none", 'int', size, size)
                else:
                    log("Function requires argument!", _op)
                    self.isValid = False
            pass
        elif op_type == "relation":
            log("Relation operator", _op)
        elif op_type == "matrixoperator":
            if l_type == 'matrix' and r_type == 'matrix':
                _temp, l_matrix = self.visit(node.left_operand, table, True)
                _temp, r_matrix = self.visit(node.right_operand, table, True)
                if l_matrix.matrix_type != r_matrix.matrix_type:
                    log("Matrixes types ({0})({1}) aren't compatible!".format(l_matrix.matrix_type, r_matrix.matrix_type), _op)
                    self.isValid = False
                elif l_matrix.row != r_matrix.row or l_matrix.column != r_matrix.column:
                    log("Matrixes must have same size!", _op)
                    self.isValid = False

                if self.isValid:
                    if require_tuple is False:
                        return 'matrix'
                    else:
                        return 'matrix', MatrixSymbol("none", 'int', l_matrix.row, l_matrix.column)
            else:
                log("This operator requires two matrixes!", _op)
                self.isValid = False

        elif op_type == "operator":
            if l_type is None or r_type is None:
                log("Operator {0} requires two operands!".format(_op.operator), _op)
            else:
                return get_type(_op.operator, l_type, r_type)
        else:
            log("Unknown operator.", _op)

    def visit_AssignOperation(self, node, table):
        return node

    def visit_Operand(self, node, table, require_tuple=False):
        if require_tuple:
            return self.visit(node.value, table)
        else:
            ret = self.visit(node.value, table)
            if type(ret) is tuple:
                return ret[0]
            else:
                return ret

    def visit_Operator(self, node, table):
        return node

    def visit_MatrixOperator(self, node, table):
        return node

    def visit_SelfOperator(self, node, table):
        return node

    def visit_Function(self, node, table):
        return node

    def visit_ReservedOperation(self, node, table):
        _op = node.operator
        if _op == 'break' or _op == 'continue':
            if LOOP_COUNT <= 0:
                log("Operator '{0}' used outside loop.".format(_op), node)
                self.isValid = False
        elif _op == 'return':
            if node.left_operand:
                _type = self.visit(node.left_operand, table)
                if _type is None:
                    log("Returning unexisting type.", node)
                    self.isValid = False
        elif _op == 'print':
            if node.left_operand:
                self.visit(node.left_operand, table)
            else:
                log("'print' function requires attribute", node)
                self.isValid = False

    def visit_Relation(self, node, table):
        return node

    def visit_Condition(self, node, table):
        l_type = self.visit(node.left_operand, table)
        r_type = self.visit(node.right_operand, table)

        if node.operator and node.operator.operator:
            _type = get_type(node.operator.operator, l_type, r_type)
            if _type != 'bool':
                log("Condition must return boolean type", node.operator)
                self.isValid = False
        else:
            log("Unexisting operator in condition!", node)

    def visit_Conditional(self, node, table):
        self.visit(node.condition, table)
        if node.true_instruction:
            self.visit(node.true_instruction, table)
        if node.false_instruction:
            self.visit(node.false_instruction, table)

    def visit_LoopConditional(self, node, table):
        global LOOP_COUNT
        if node.condition:
            self.visit(node.condition, table)
        else:
            remove_i_var = True
            self.visit(node.iteration_range, table)
            i_var_type, i_var = self.visit(node.iteration_variable, table, False)
            if i_var_type is None and node.iteration_variable and node.iteration_variable.identifier:
                _id = node.iteration_variable.identifier
                table.put(_id, VariableSymbol(_id, 'int'))
            elif i_var_type == 'int':
                _id = i_var.name
                remove_i_var = False
            else:
                log("Incompatible iteration variable", node)
                self.isValid = False
                remove_i_var = False

            LOOP_COUNT += 1
            self.visit(node.loop_instruction, table)
            LOOP_COUNT -= 1

            if remove_i_var:
                table.delete(_id)

    def visit_Range(self, node, table):
        l_type = self.visit(node.left_operand, table)
        r_type = self.visit(node.right_operand, table)

        if node.left_operand and node.left_operand.value:
            child_node = node.left_operand.value
        elif node.right_operand and node.right_operand.value:
            child_node = node.right_operand.value
        else:
            child_node = node

        if l_type != 'int' or r_type != 'int':
            log("Range requires two integers operands!", child_node)
            self.isValid = False

    def visit_Structure(self, node, table):
        if type(node.structure) == str:
            return 'string'
        else:
            return self.visit(node.structure, table)

    def visit_Matrix(self, node, table):
        _type, rows, columns = self.visit(node.rows, table)

        if rows > 1 and node.one_dimensional is True:
            log("Declaring multidimensional matrix requires brackets []!", node.rows)
            self.isValid = False
        if _type is None:
            log("Matrix hasn't consistent type!", node.rows)
            self.isValid = False
        if columns is None:
            log("Matrix hasn't consistent length!", node.rows)
            self.isValid = False

        return 'matrix', MatrixSymbol("none", _type, rows, columns)

    def visit_Rows(self, node, table):
        rows_amount = 0
        series_length = 0
        _type = None

        if node.series is not None:
            rows_amount += 1
            _type, series_length = self.visit(node.series, table)

        if node.rows is None:
            return _type, rows_amount, series_length
        else:
            nx_type, nx_rows_amount, nx_series_length = self.visit(node.rows, table)
            rows_amount += nx_rows_amount

            if _type != nx_type:
                _type = None

            if nx_series_length is None:
                return _type, rows_amount, None
            elif series_length != nx_series_length:
                return _type, rows_amount, None
            else:
                return _type, rows_amount, series_length

    def visit_Series(self, node, table):
        length = 0
        _type = None

        if node.operand is not None:
            length += 1
            _type = self.visit(node.operand, table)

        if node.series is None:
            return _type, length
        else:
            nx_type, nx_length = self.visit(node.series, table)
            length += nx_length
            if _type != nx_type:
                return None, length
            else:
                return _type, length

    def visit_IntegerSeries(self, node, table):
        pass

    def visit_Number(self, node, table):
        if node.number is not None:
            _type = type(node.number)
            if _type == int:
                return 'int'
            elif _type == float:
                return 'float'
            else:
                log("Couldn't recognize type: " + _type.__str__(), node)
                return _type

    def visit_Address(self, node, table):
        return self.visit(node.identifier, table)

    def visit_Error(self, node, table):
        pass

