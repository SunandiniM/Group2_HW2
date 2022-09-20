import re
from .Num import Num
from .Sym import Sym
from .utilities import push 

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for s in names:
            if re.match(r"^[A-Z]*",s):
                col = push(self.all, Sym(names.index(s),s))
            else:
                col = push(self.all, Num(names.index(s),s))
            
            if not re.match(r":$",s):
                if re.match(r"[!+-]",s):
                    push(self.x, col)
                else:
                    push(self.y, col)
                if not re.match(r"!$",s):
                    self.klass=col