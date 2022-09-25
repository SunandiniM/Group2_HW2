import re
from .Num import Num
from .Sym import Sym
from .utilities import push 

class Cols:
    # `Columns` Holds of summaries of columns. 
    # Columns are created once, then may appear in  multiple slots.
    def __init__(self, names):
        #Initialize columns
        #names initialized from the parameter names and the rest are initialized as an emtpy list or None
        self.names = names #all column names
        self.all = [] # all the columns (including the skipped ones)
        self.klass = None # the single dependent klass column (if it exists)
        self.x = [] # independent columns (that are not skipped)
        self.y = [] # depedent columns (that are not skipped)
        for s in names:
            #Numerics start with Uppercase.
            if re.match(r"^[A-Z]*",s):
                col = push(self.all, Sym(names.index(s),s))
            else:
                col = push(self.all, Num(names.index(s),s))
            #separate columns that are skipped from columns that are not skipped
            if not re.match(r":$",s):
                if re.match(r"[!+-]",s):
                    push(self.x, col)
                else:
                    push(self.y, col)
                if not re.match(r"!$",s):
                    self.klass=col