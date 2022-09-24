from fileinput import filename
from os import environ
from .LuaCode import *
import re
import math

def csv(fname, fun=None):
    if(fname==None or len(fname.strip())==0):
        raise Exception("File not found")
    else:
        sep = "([^"+the["seperator"]+"]+)"
        with open(fname, 'r') as s:
            t = []
            for s1 in s.readlines():
                t.append(coerce(s1))
                if fun:
                    fun(t)

def o(t):
    if type(t) is not dict:
        return str(t)

    def show(k,v):
        if not str(k).find("^_"):
            v=o(v)
            return len(t)==0 and ":{} {}".format(k,v) or str(v)

    u=[]
    for k,v in t.items():
        u.append(show(k,v))
    if len(t)==0:
        u.sort()
    return "{"+' '.join([str(item) for item in u])+"}"

def oo(t):
    print(o(t))
    return t

def copy(t):
    if type(t) is not dict:
        return t
    u={}
    for k,v in t:
        u[k]=copy(v)
    return u

def push(t,x):
    t.append(x)
    return x

def per(t,p = 0.5):
    if t:
        p=math.floor((p*len(t))+0.5)
        return t[max(0,min(len(t),p)-1)]
    else:
        return 0

# def rogues():
#     print(environ.items)
#     for k,v in environ.items:
#         if not b4[k]:
#             print("?",k,type(v))

def rnd(x, places=0):
    mult = 10^(places or 2)
    return math.floor(x * mult + 0.5)/mult
