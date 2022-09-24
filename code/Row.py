from .utilities import copy 
class Row:
    def __init__(self, cells):
        self.cells = cells
    def __new__(cls, cells):
        return { "cells":cells, "cooked":copy(cells), "isEvaled":False }