import sys
import scanner
import parser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
from TypeChecker import get_type
from Interpreter import Interpreter


if __name__ == '__main__':

    filename = sys.argv[1] if len(sys.argv) > 1 else "example.m"

    try:
        file = open(filename, "r")
    except IOError:
        print("Cannot open file".format(filename))
        sys.exit(0)

    parser = parser.parser
    text = file.read()

    ast = parser.parse(text, lexer=scanner.lexer)

    if parser.errorok:
        print("Checking types...")
        typeChecker = TypeChecker()
        typeChecker.visit(ast)
        if typeChecker.isValid:
            print("... successful.\nInterpreting:\n")
            interpreter = Interpreter()
            val = interpreter.visit(ast)
            print("\nFinished execution with return value \'" + val.__str__() + "\'")
        else:
            print("... unsuccessful. Types are invalid.")
    else:
        print("Correct syntax errors before running type checker!")
