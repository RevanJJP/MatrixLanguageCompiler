class Node(object):
    line_no = None

    def __init__(self):
        return self.printTree()

    def set_line(self, line_no):
        self.line_no = line_no

    def accept(self, visitor):
        class_name = self.__class__.__name__
        method_ = getattr(visitor, 'visit_' + class_name, None)
        if method_:
            return method_(self)


class Start(Node):
    def __init__(self, line, instruction_set):
        self.type = 'start'
        self.instruction_set = instruction_set
        self.set_line(line)


class Instruction(Node):
    def __init__(self, line, expr):
        self.type = 'instruction'
        self.expr = expr
        self.set_line(line)


class InstructionSet(Node):
    def __init__(self, line, instruction, instruction_rest):
        self.type = 'instruction_set'
        self.instruction = instruction
        self.instruction_rest = instruction_rest
        self.set_line(line)


class Expression(Node):
    def __init__(self, line, expr):
        self.type = 'expression'
        self.expr = expr
        self.set_line(line)


class Identifier(Node):
    def __init__(self, line, identifier):
        self.type = 'identifier'
        self.identifier = identifier
        self.set_line(line)


class Assignment(Node):
    def __init__(self, line, operator, identifier, operand):
        self.type = "assignment"
        self.operator = operator
        self.identifier = identifier
        self.operand = operand
        self.set_line(line)


class Operation(Node):
    def __init__(self, line, operator, left_operand, right_operand):
        self.type = "operation"
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.set_line(line)


class AssignOperation(Node):
    def __init__(self, line, operator):
        self.type = "assignoperation"
        self.operator = operator
        self.set_line(line)


class Operand(Node):
    def __init__(self, line, value):
        self.type = "operand"
        self.value = value
        self.set_line(line)


class Operator(Node):
    def __init__(self, line, operator):
        self.type = "operator"
        self.operator = operator
        self.set_line(line)


class MatrixOperator(Operator):
    def __init__(self, line, operator):
        super().__init__(line, operator)
        self.type = "matrixoperator"
        self.operator = operator
        self.set_line(line)


class SelfOperator(Operator):
    def __init__(self, line, operator):
        super().__init__(line, operator)
        self.type = "selfoperator"
        self.set_line(line)


class Function(Operator):
    def __init__(self, line, operator):
        super().__init__(line, operator)
        self.type = "function"
        self.set_line(line)


class ReservedOperation(Operation):
    def __init__(self, line, operator, left_operand, right_operand):
        super().__init__(line, operator, left_operand, right_operand)
        self.type = "reservedoperation"
        self.set_line(line)


class Relation(Operator):
    def __init__(self, line, operator):
        super().__init__(line, operator)
        self.type = "relation"
        self.set_line(line)


class Condition(Operation):
    def __init__(self, line, operator, left_operand, right_operand):
        super().__init__(line, operator, left_operand, right_operand)
        self.type = "condition"
        self.set_line(line)


class Conditional(Node):
    def __init__(self, line, condition, true_instruction, false_instruction):
        self.type = "conditional"
        self.condition = condition
        self.true_instruction = true_instruction
        self.false_instruction = false_instruction
        self.set_line(line)


class LoopConditional(Node):
    def __init__(self, line, condition, loop_instruction, iteration_variable, iteration_range, loop_type):
        self.type = "loopconditional"
        self.condition = condition
        self.iteration_variable = iteration_variable
        self.iteration_range = iteration_range
        self.loop_instruction = loop_instruction
        self.loop_type = loop_type
        self.set_line(line)


class Range(Node):
    def __init__(self, line, left_operand, right_operand):
        self.type = "range"
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.set_line(line)


class Structure(Node):
    def __init__(self, line, structure):
        self.type = "structure"
        self.structure = structure
        self.set_line(line)


class Matrix(Node):
    def __init__(self, p, rows, one_dimensional=False):
        self.type = "matrix"
        self.rows = rows
        self.set_line(p)
        self.one_dimensional = one_dimensional


class Rows(Node):
    def __init__(self, line, series, next_rows):
        self.type = "rows"
        self.series = series
        self.rows = next_rows
        self.set_line(line)


class Series(Node):
    def __init__(self, line, operand, next_series):
        self.type = "series"
        self.operand = operand
        self.series = next_series
        self.set_line(line)


class IntegerSeries(Series):
    def __init__(self, line, int_num, next_series):
        super().__init__(line, int_num, next_series)
        self.type = "integer_series"
        self.set_line(line)


class Number(Node):
    def __init__(self, line, number):
        self.type = "number"
        self.number = number
        self.set_line(line)


class Address(Node):
    def __init__(self, line, identifier, integer_series):
        self.type = "address"
        self.identifier = identifier
        self.integer_series = integer_series
        self.set_line(line)


class Error(Node):
    def __init__(self):
        pass
