class Symbol:
    pass


class VariableSymbol(Symbol):
    def __init__(self, name, type):
        self.name = name
        self.type = type


class MatrixSymbol(Symbol):
    def __init__(self, name, matrix_type, rows=None, columns=None):
        self.name = name
        self.type = 'matrix'
        self.matrix_type = matrix_type
        self.row = rows
        self.column = columns


class SymbolTable(object):
    def __init__(self, parent, name):
        self.symbols = {}
        self.name = name
        self.parent = parent

    def put(self, name, symbol):
        self.symbols[name] = symbol

    def get(self, name):
        try:
            ret = self.symbols[name]
            return ret
        except Exception:
            return None

    def delete(self, name):
        self.symbols.pop(name)

    def getMatrixSize(self, name):
        try:
            matrix = self.symbols[name]
            row = matrix.row
            column = matrix.column
            return row, column
        except Exception:
            return None

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        self.name = name

    def popScope(self):
        return self.name
