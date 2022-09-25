from .LuaCode import *
from .utilities import *
import math
import random

class Num:
    #Initialize Num object if given with column number and name else with default values
    def __init__(self, c=0, s=""):
        self.n=0 # items seen
        self.c=c # column position
        self.name= s # column name
        self._has={} # kept data
        self.lo=math.inf # lowest seen
        self.hi=-math.inf # highest seen
        self.isSorted=True # no updates sinces last sort of data
        if not s.find("-$"):
            self.w=1
        else:
            self.w=-1

    def nums(self):
        # Return kept numbers, sorted
        print("printing self._has",self._has)
        if not self.isSorted:
            self._has = sorted(self._has)
            print("printing self._has",self._has)
            self.isSorted=True
        return self._has
    
    # Reservoir sampler. Keep at most `the.nums` numbers 
    # (and if we run out of room, delete something old, at random)., 
    def add(self,v,pos=None):
        if v!= "?":
            self.n= self.n+1
            self.lo=min(v,self.lo)
            self.hi=max(v,self.hi)
            if len(self._has) < the["nums"]:
                pos=1+len(self._has)
            elif random.random() < the["nums"]/self.n:
                pos=random.randint(1,len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = float(v)
    # Diversity (standard deviation for Nums, entropy for Syms)
    def div(self):
        a=self.nums()
        return (per(a,0.9)-per(a,0.1))/2.58
    # Central tendancy (median for Nums, mode for Syms)
    def mid(self):
        return per(self.nums(),0.5)