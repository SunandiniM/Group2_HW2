from .Row import Row
from .Cols import Cols
from .Sym import Sym
from .Num import Num
from .utilities import *

class Data:
    #maintains rows and cols 
    def __init__(self, src):
      #initializing data object
      self.cols = None #column set to None
      self.rows = [] #Rows set a empty list
      self.src = src #Source set as parameter passed
      if type(src) == str:
        def func(row):
          self.add(row)
        csv(src,func)
      else:
        for row in src:
          self.add(row)
   
    def add(self,xs: Row):
      #add row to the data
      if not self.cols:
        self.cols = Cols(xs)
      else:
        row = xs if type(xs)==Row else Row(xs)
        self.rows.append(row)
        for todo in [self.cols.x, self.cols.y]:
          for col in todo:
            col.add(row["cells"][col.c])

    def stats(self,places=2,showCols=None,fun=None):
      #return stats of the data
      showCols = showCols or self.cols.y
      # fun = fun or self.cols.mid
      t={}
      for i in showCols:
        if not fun:
          fun = i.mid
        v = fun(i)
        v = (type(v)==int and rnd(v,places)) or v
        t[i.name]=v
      return t