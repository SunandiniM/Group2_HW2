import .Row from Row
from .Sym import Sym

class Data:
    def __init__(self, src):
      self.cols = None
      self.rows = []
      if type(src) == str:
        src = csv(src)
      for row in src:
        self.add(row)
   
    def add(self, xs):
      if not self.cols:
        self.cols = Cols(xs)
      else:
        row = push(self.rows, Row(row))
          for todo in [self.cols.x, self.cols.y]:
            for col in todo:
              col.add(row.cells[col.at])
        