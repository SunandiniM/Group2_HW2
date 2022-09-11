from .utilities import copy 
class Row:
    def __init__(self, t):
        self.t = t
    def __new__(cls, t):
        return { "cells":t, "cooked":copy(t), "isEvaled":False }