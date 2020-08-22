import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)


class Interpreter(object):

    def __init__(self):
        self.memory = MemoryStack()

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Start)
    def visit(self, node):
        try:
            self.visit(node.instruction_set)
        except ReturnValueException as e:
            return e.value

    @when(AST.Instruction)
    def visit(self, node):
        self.visit(node.expr)

    @when(AST.InstructionSet)
    def visit(self, node):
        self.visit(node.instruction)
        if node.instruction_rest is not None:
            self.visit(node.instruction_rest)

    @when(AST.Expression)
    def visit(self, node):
        self.visit(node.expr)

    @when(AST.Identifier)
    def visit(self, node):
        if type(node.identifier) is AST.Address:
            return self.visit(node.identifier)
        else:
            return self.memory.get(node.identifier)

    @when(AST.Assignment)
    def visit(self, node):
        identifier = node.identifier.identifier
        value = self.visit(node.operand)

        if node.operator == '=':
            operator = '='
        else:
            operator = self.visit(node.operator)

        if type(identifier) is AST.Address:
            end_value = self.memory.get(identifier.identifier.identifier)
            if end_value is None:
                print("Matrix doesn't exist at line: " + identifier.identifier.line_no.__str__())
                return
            else:
                if_exist = True
                end_value = self.visit(identifier)

        else:
            end_value = self.memory.get(identifier)

            if end_value is None:
                if_exist = False
                end_value = 0
            else:
                if_exist = True

        try:
            if operator == '=':
                end_value = value
            elif operator == '+=':
                end_value += value
            elif operator == '-=':
                end_value -= value
            elif operator == '*=':
                end_value *= value
            elif operator == '/=':
                end_value /= value
            else:
                print("Unknown operator " + operator.__str__())
        except ArithmeticError as e:
            print("ARITHMETIC ERROR: " + e)
            exit()

        if type(identifier) is AST.Address:
            matrix = self.memory.get(identifier.identifier.identifier)
            address = self.visit(identifier.integer_series)

            if len(address) == 1:
                matrix[address[0]] = end_value
            elif len(address) == 2:
                matrix[address[0]][address[1]] = end_value
            else:
                print("Address is too long in line " + identifier.identifier.line_no.__str__())

            self.memory.set(identifier.identifier.identifier, matrix)

        else:
            if if_exist:
                self.memory.set(identifier, end_value)
            else:
                self.memory.insert(identifier, end_value)

    @when(AST.Operation)
    def visit(self, node):

        try:
            left_value = self.visit(node.left_operand)
            right_value = self.visit(node.right_operand)

            _op = self.visit(node.operator)

            if type(node.operator) is AST.Operator:
                if _op == '+':
                    return left_value + right_value
                elif _op == '-':
                    return left_value + right_value
                elif _op == '*':
                    return left_value + right_value
                elif _op == '/':
                    return left_value + right_value
                else:
                    print("Unknown operator \"" + _op.__str__() + "\" at line " + node.operator.line_no.__str__())
                    return None
            elif type(node.operator) is AST.Function:
                matrix = []

                if _op == 'zeros':
                    for i in range(left_value):
                        row = []
                        for j in range(left_value):
                            row.append(0)
                        matrix.append(row)

                elif _op == 'ones':
                    for i in range(left_value):
                        row = []
                        for j in range(left_value):
                            row.append(1)
                        matrix.append(row)

                elif _op == 'eye':
                    for i in range(left_value):
                        row = []
                        for j in range(left_value):
                            row.append(0)
                        matrix.append(row)
                    for i in range(left_value):
                        matrix[i][i] = 1

                else:
                    print("Unknown operator \"" + _op.__str__() + "\" at line " + node.operator.line_no.__str__())
                    return None

                return matrix

            elif type(node.operator) is AST.SelfOperator:
                if _op == '\'':
                    return transpose(left_value)
                else:
                    print("Unknown operator \"" + _op.__str__() + "\" at line " + node.operator.line_no.__str__())
                    return None
            elif type(node.operator) is AST.MatrixOperator:
                matrix = left_value
                if _op == '.+':
                    if type(matrix[0]) is list:
                        for i in range(len(matrix)):
                            for j in range(len(matrix[i])):
                                matrix[i][j] += right_value[i][j]
                    else:
                        for i in range(len(matrix)):
                            matrix[i] += right_value[i]
                    return matrix
                elif _op == '.-':
                    if type(matrix[0]) is list:
                        for i in range(len(matrix)):
                            for j in range(len(matrix[i])):
                                matrix[i][j] -= right_value[i][j]
                    else:
                        for i in range(len(matrix)):
                            matrix[i] -= right_value[i]
                    return matrix
                elif _op == '.*':
                    if type(matrix[0]) is list:
                        for i in range(len(matrix)):
                            for j in range(len(matrix[i])):
                                matrix[i][j] *= right_value[i][j]
                    else:
                        for i in range(len(matrix)):
                            matrix[i] *= right_value[i]
                    return matrix
                elif _op == './':
                    if type(matrix[0]) is list:
                        for i in range(len(matrix)):
                            for j in range(len(matrix[i])):
                                matrix[i][j] /= right_value[i][j]
                    else:
                        for i in range(len(matrix)):
                            matrix[i] /= right_value[i]
                    return matrix
                else:
                    print("Unknown operator \"" + _op.__str__() + "\" at line " + node.operator.line_no.__str__())
                    return None


        except ArithmeticError as e:
            print("\nERROR with operation in line " + node.operator.line_no.__str__() + ": " + e.__str__())

    @when(AST.AssignOperation)
    def visit(self, node):
        return node.operator

    @when(AST.Operand)
    def visit(self, node):
        return self.visit(node.value)

    @when(AST.Operator)
    def visit(self, node):
        return node.operator

    @when(AST.MatrixOperator)
    def visit(self, node):
        return node.operator

    @when(AST.SelfOperator)
    def visit(self, node):
        return node.operator

    @when(AST.Function)
    def visit(self, node):
        return node.operator

    @when(AST.ReservedOperation)
    def visit(self, node):
        _op = node.operator

        left_value = None
        right_value = None

        if node.left_operand is not None:
            left_value = self.visit(node.left_operand)
        if node.right_operand is not None:
            right_value = self.visit(node.right_operand)

        if _op == "print":
            print(left_value.__str__())
        elif _op == "return":
            raise ReturnValueException(left_value)
        elif _op == "break":
            raise BreakException
        elif _op == "continue":
            raise ContinueException
        else:
            print("Unknown operator \"" + _op.__str__() + "\"")

    @when(AST.Relation)
    def visit(self, node):
        return node.operator

    @when(AST.Condition)
    def visit(self, node):
        rel = self.visit(node.operator)
        left = self.visit(node.left_operand)
        right = self.visit(node.right_operand)

        if rel == '<':
            return left < right
        elif rel == '>':
            return left > right
        elif rel == '<=':
            return left <= right
        elif rel == '>=':
            return left >= right
        elif rel == '==':
            return left == right
        elif rel == '!=':
            return left != right
        else:
            print("ERROR(" + node.line_no + ")- unknown relation " + rel.__str__())

    @when(AST.Conditional)
    def visit(self, node):
        if self.visit(node.condition):
            self.visit(node.true_instruction)
        elif node.false_instruction is not None:
            self.visit(node.false_instruction)

    @when(AST.LoopConditional)
    def visit(self, node):
        self.memory.push()
        try:
            if node.loop_type == "WHILE":
                while self.visit(node.condition):
                    try:
                        self.visit(node.loop_instruction)
                    except ContinueException:
                        pass
            elif node.loop_type == "FOR":
                iter_range = self.visit(node.iteration_range)
                iter_finish = iter_range[1]
                self.memory.insert(node.iteration_variable.identifier, iter_range[0])

                while self.visit(node.iteration_variable) < iter_finish:
                    try:
                        self.visit(node.loop_instruction)
                    except ContinueException:
                        pass

                    i_var = self.visit(node.iteration_variable)
                    self.memory.set(node.iteration_variable.identifier, i_var+1)

        except BreakException:
            pass

        self.memory.pop()

    @when(AST.Range)
    def visit(self, node):
        left = self.visit(node.left_operand)
        right = self.visit(node.right_operand)

        return left, right

    @when(AST.Structure)
    def visit(self, node):
        if type(node.structure) is str:
            return node.structure
        else:
            return self.visit(node.structure)

    @when(AST.Matrix)
    def visit(self, node):
        matrix = self.visit(node.rows)

        if node.one_dimensional:
            return matrix[0]
        else:
            return matrix

    @when(AST.Rows)
    def visit(self, node):
        rows = [self.visit(node.series)]
        if node.rows is not None:
            return rows + self.visit(node.rows)
        else:
            return rows

    @when(AST.Series)
    def visit(self, node):
        series = [self.visit(node.operand)]
        if node.series is not None:
            return series + self.visit(node.series)
        else:
            return series

    @when(AST.IntegerSeries)
    def visit(self, node):
        series = [self.visit(node.operand)]
        if node.series is not None:
            return series + self.visit(node.series)
        else:
            return series

    @when(AST.Number)
    def visit(self, node):
        if node.number is not None:
            _type = type(node.number)
            if _type == int:
                return int(node.number)
            elif _type == float:
                return float(node.number)
            else:
                print("Couldn't recognize type: " + _type.__str__(), node)
                return None

    @when(AST.Address)
    def visit(self, node):
        value = self.visit(node.identifier)
        address = self.visit(node.integer_series)

        if len(address) == 1:
            return value[address[0]]
        elif len(address) == 2:
            return value[address[0]][address[1]]
        else:
            print("ERROR - address is too long")

    @when(AST.Error)
    def visit(self, node):
        pass


def transpose(matrix):
    new_matrix = []

    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)

    return new_matrix


