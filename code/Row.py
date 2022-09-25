from .utilities import copy 
class Row:
    def __init__(self, cells):
        self.cells = cells # one record
    def __new__(cls, cells):
        return { "cells":cells, "cooked":copy(cells), "isEvaled":False }
        # cooked => used if we discretize data
        # isEvaled => true if y-values evaluated