from .LuaCode import *
from .utilities import *
import math
import random

class Num:
    def __init__(self, c=0, s=""):
        self.n=0
        self.c=c
        self.name= s
        self._has={}
        self.lo=math.inf
        self.hi=-math.inf
        self.isSorted=True
        if not s.find("-$"):
            self.w=1
        else:
            self.w=-1

    def nums(self):
        print("printing self._has",self._has)
        if not self.isSorted:
            self._has = sorted(self._has)
            print("printing self._has",self._has)
            self.isSorted=True
        return self._has
    
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

    def div(self):
        a=self.nums()
        return (per(a,0.9)-per(a,0.1))/2.58

    def mid(self):
        return per(self.nums(),0.5)