import sys
sys.path.append('../code')
from .LuaCode import *
import math
# import LuaCode
import random

class Num:
    def __init__(self, c=0, s=""):
        self.n=0
        self.c=c
        self.name= s
        self._has=[]
        self.lo=-math.inf
        self.hi=math.inf
        self.isSorted=True
        if "-$" not in s:
            self.w=1
        else:
            self.w=-1

    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted=True
        return self._has
    
    def add(self,v):
        if v!= "?":  #check
            self.n= self.n+1
            self.lo=min(v,self.lo)
            self.hi=max(v,self.hi)
            if len(self._has) - 1 < the["nums"]:
                pos=len(self._has)
            elif random.random() < the["nums"]/self.n:
                pos=random.random(len(self._has-1))
            if pos:
                self.isSorted = False
                self._has[pos] = int(v)

    def per(self,t,p):
        p=math.floor(((p or 0.5)*(len(t)))+0.5)
        return t[max(0,min(len(t),p))]

    def div(self):
        a=self.nums()
        return (self.per(a,0.9)-self.per(a,0.1))/2.58

    def mid(self):
        return self.per(self.nums(),0.5)