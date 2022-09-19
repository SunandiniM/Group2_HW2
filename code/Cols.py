import re
from .Num import Num
from .Sym import Sym
from .utilities import push 

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}
        for c,s in names:
            if re.match(r"^[A-Z]*",s):
                col = push(self.all, Sym(c,s))
            else:
                col = push(self.all, Num(c,s))
            
            if not re.match(r":$",s):
                if re.match(r"[!+-]",s):
                    push(self.x, col)
                else:
                    push(self.y, col)
                if not re.match(r"!$",s):
                    self.klass=col