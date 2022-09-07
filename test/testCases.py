import math
import random
import sys
sys.path.append('../code')
from Num import *
from LuaCode import *
from Sym import *
from utilities import *

eg = {}
fails = 0

def runs(k):
    if eg:
        return
    random.seed(the["seed"])
    random.random()
    old = [None]*len(the)
    for k,v in enumerate(the):
        old[k] = v
    if eval(the["dump"]):
        status, out = True, eg[k]
    else:
        status = False
        try:
            eg[k]
        except:
            out = "Error"
    for k,v in enumerate(old):
        the[k] = v
    msg = ("PASS" if (out is True) else "FAIL") if status else "CRASH"
    print("!!!!!!", msg, k, status)
    return out

def test_bad():
    print("eg.dont.have.this.field")

def list_eg():
    t = []
    for k, _ in eg:
        t.append(k)
    t.sort()
    return t

def LS_eg():
    print("\nExamples lua csv -e ...")
    for _, k in list_eg():
        print("\t%s" % k)
    return True

def ALL_eg():
    for _, k in list_eg():
        if k != "ALL":
            print("\n------------------------------------")
            if not runs(k):
                fails = fails + 1
    return True

def test_the_eg():
    oo(the)
    assert True

def test_bignum_eg():
    num = Num()
    the["nums"] = 32
    for i in range(1,100):
        num.add(i)
    oo(num.nums())
    assert len(num._has) == 32

def test_num_eg():
    num = Num()
    for i in range(1,100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    assert 50<=mid and mid<=52 and 30.5<div and div<32


the = cli(the)
runs(the["eg"])
