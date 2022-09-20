from .Row import Row
from .Cols import Cols
from .Sym import Sym
from .Num import Num
from .utilities import *

class Data:
  
    def __init__(self, src):
      self.cols = None
      self.rows = []
      self.src = src
      if type(src) == str:
        def func(row):
          self.add(row)
        src = csv(src,func)
      else:
        for row in src:
          self.add(row)
   
    def add(self,xs):
      if not self.cols:
        self.cols = Cols(xs)
      else:
        row1 = push(self.rows,(xs if xs["cells"] else Row(xs)))
        for todo in [self.cols.x, self.cols.y]:
          for col in todo:
            col.add(row1["cells"][col.at])

    def stats(self,places,showCols,fun="mid"):
        showCols = showCols or self.cols.y
        fun = fun or "mid"
        t={}
        for i in showCols:
            if(type(i)==Num):
                if(fun=="mid"):
                    v=i.mid()
                elif(fun=="div"):
                    v=i.div()
                v = (type(v)==int and rnd(v,places)) or v
            t[i.name]=v
        return t 