import re
import sys

help="""
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
USAGE: lua seen.lua [OPTIONS]
OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --seperator feild seperator                       = ,
 """

def coerce(s):
    def fun(s1):
        if s=="true":
            return True
        elif s=="false":
            return False
        return s1

    if re.match(r"^[0-9]+$",s):
        return int(s)
    else:
        return None or fun(s)

def cli(t):
    for slot,v in t.items():
        v = str(v)
        arg = sys.argv
        for n, x in enumerate(arg):
            if (x is ("-"+slot[0:1])) or (x is ("--"+slot)):
                v = "true" if v=="false" else ("false" if v=="true" else arg[n+1])
        t[slot] = coerce(v)
    if t["help"] is True:
        sys.exit(print("\n"+help+"\n"))
    return t

def fun_the():
    the = {}
    extract = re.findall(r"[-][-]([\S]+)[^\n]+= ([\S]+)", help)
    for k, v in extract:
        the[k] = coerce(v)
    return the

the = fun_the()