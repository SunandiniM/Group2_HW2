import math
import random
# import sys
# sys.path.append('../code')
from ..code import Num
from ..code import LuaCode
from ..code import Sym
from ..code import utilities
from ..code import Row
from ..code import Cols
from ..code import Data

eg = {}
fails = 0
the = LuaCode.the

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
    global fails
    for _, k in list_eg():
        if k != "ALL":
            print("\n------------------------------------")
            if not runs(k):
                fails = fails + 1
    return True

def test_the_eg():
    utilities.oo(the)
    assert True

def test_bignum_eg():
    num = Num.Num()
    the["nums"] = 32
    for i in range(1,1001):
        num.add(i)
    utilities.oo(num.nums())
    assert len(num._has) == 32

def test_num_eg():
    the["nums"] = 512
    num = Num.Num()
    for i in range(1,101):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    assert 50<=mid and mid<=52 and 30.5<div and div<32

def test_sym_eg():
    sym=Sym.Sym()
    pairs=['a','a','a','a','b','b','c']
    for x in pairs:
        sym.add(x)
    mode=sym.mid()
    entropy=sym.div()
    entropy=(1000*entropy)//1/1000
    utilities.oo({"mid":mode,"div":entropy})
    assert mode=='a' and 1.37<= entropy and entropy <= 1.38

def test_csv_eg():
    n=0
    def func(row,n=0):
        n=n+1
        if n>10:
            return
        else:
            return utilities.oo(row)
    print(utilities.csv("../data/sampleData.csv",func))
    assert True

def test_data_eg():
    d = Data.Data("../data/sampleData.csv")
    for _,col in d.cols.y:
        utilities.oo(col)
    assert True

def test_stats_eg():
    data = Data.Data("../data/sampleData.csv")
    div = lambda col: col.div()
    mid = lambda col: col.mid()
    print("xmid", utilities.o(data.stats(2,data.cols.x, "mid")))
    print("xdiv", utilities.o(data.stats(3,data.cols.x, "div")))
    print("ymid", utilities.o(data.stats(2,data.cols.y, "mid")))
    print("ydiv", utilities.o(data.stats(3,data.cols.y, "div")))
    assert True

the = LuaCode.cli(the)
runs(the["eg"])