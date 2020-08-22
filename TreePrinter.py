from __future__ import print_function
from AST import *


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @classmethod
    def printIndented(cls, string, level):
        print("| " * level + string)

    @addToClass(Node)
    def printTree(self, indent):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(Start)
    def printTree(self, indent=0):
        self.instruction_set.printTree(indent)

    @addToClass(Instruction)
    def printTree(self, indent=0):
        self.expr.printTree(indent)

    @addToClass(InstructionSet)
    def printTree(self, indent=0):
        if self.instruction:
            self.instruction.printTree(indent)
        if self.instruction_rest:
            self.instruction_rest.printTree(indent)

    @addToClass(Expression)
    def printTree(self, indent=0):
        self.expr.printTree(indent)

    @addToClass(Identifier)
    def printTree(self, indent=0):
        if type(self.identifier) is Address:
            self.identifier.printTree(indent)
        else:
            TreePrinter.printIndented(self.identifier, indent)

    @addToClass(Assignment)
    def printTree(self, indent=0):
        if type(self.operation) is AssignOperation:
            self.operation.printTree(indent)
        else:
            TreePrinter.printIndented(self.operation, indent)
        self.identifier.printTree(indent+1)
        self.operand.printTree(indent+1)

    @addToClass(Operation)
    def printTree(self, indent=0):
        self.operator.printTree(indent)
        if self.left_operand:
            self.left_operand.printTree(indent + 1)
        if self.right_operand:
            self.right_operand.printTree(indent + 1)

    @addToClass(AssignOperation)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.operation, indent)

    @addToClass(Operand)
    def printTree(self, indent=0):
        self.value.printTree(indent)

    @addToClass(Operator)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.operator, indent)

    @addToClass(SelfOperator)
    def printTree(self, indent=0):
        if self.operator == "'":
            TreePrinter.printIndented("TRANSPOSE", indent)
        else:
            TreePrinter.printIndented(self.operator, indent)

    @addToClass(Function)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.operator, indent)

    @addToClass(ReservedOperation)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.operator.__str__().upper(), indent)
        if self.left_operand:
            self.left_operand.printTree(indent+1)
        if self.right_operand:
            self.right_operand.printTree(indent+1)

    @addToClass(Relation)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.operator.__str__().upper(), indent)

    @addToClass(Condition)
    def printTree(self, indent=0):
        self.operator.printTree(indent)
        if self.left_operand:
            self.left_operand.printTree(indent+1)
        if self.right_operand:
            self.right_operand.printTree(indent+1)

    @addToClass(Conditional)
    def printTree(self, indent=0):
        TreePrinter.printIndented("IF", indent)
        self.condition.printTree(indent+1)
        if self.true_instruction:
            TreePrinter.printIndented("THEN", indent)
            self.true_instruction.printTree(indent+1)
        if self.false_instruction:
            TreePrinter.printIndented("ELSE", indent)
            self.false_instruction.printTree(indent+1)

    @addToClass(LoopConditional)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.loop_type, indent)
        if self.condition:
            self.condition.printTree(indent+1)
        if self.iteration_variable:
            self.iteration_variable.printTree(indent+1)
        if self.iteration_range:
            TreePrinter.printIndented("RANGE", indent+1)
            self.iteration_range.printTree(indent+2)
        if self.loop_instruction:
            self.loop_instruction.printTree(indent+1)

    @addToClass(Range)
    def printTree(self, indent=0):
        if self.left_operand:
            self.left_operand.printTree(indent)
        if self.right_operand:
            self.right_operand.printTree(indent)

    @addToClass(Structure)
    def printTree(self, indent=0):
        if self.structure:
            if type(self.structure) == str:
                TreePrinter.printIndented(self.structure + (" <- STRING"), indent)
            else:
                self.structure.printTree(indent)

    @addToClass(Matrix)
    def printTree(self, indent=0):
        TreePrinter.printIndented("MATRIX", indent)
        if self.rows:
            self.rows.printTree(indent+1)

    @addToClass(Rows)
    def printTree(self, indent=0):
        TreePrinter.printIndented("VECTOR", indent)
        self.series.printTree(indent+1)
        if self.rows:
            self.rows.printTree(indent)

    @addToClass(Series)
    def printTree(self, indent=0):
        self.operand.printTree(indent)
        if self.series:
            self.series.printTree(indent)

    @addToClass(IntegerSeries)
    def printTree(self, indent=0):
        self.operand.printTree(indent)
        if self.series:
            self.series.printTree(indent)

    @addToClass(Number)
    def printTree(self, indent=0):
        TreePrinter.printIndented(self.number.__str__(), indent)

    @addToClass(Address)
    def printTree(self, indent=0):
        TreePrinter.printIndented("REF", indent)
        self.identifier.printTree(indent+1)
        self.integer_series.printTree(indent+1)

