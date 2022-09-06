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
 -S  --seperator feild seperator                       = ,"""

the = {}

def coerce(s):
    if s=="true":
        return True
    elif s=="false":
        return False
    elif re.match(r"^[0-9]+$",s):
        return int(s)
    return s

def cli(t):
    for slot,v in list(t.items()):
        v = str(v)
        arg = sys.argv
        for x in arg:
            n = arg.index(x)
            if x is ("-"+slot[0]) or x is ("--"+slot):
                v = "true" if v=="false" else ("false" if v=="true" else arg[n+1])
        t[slot] = coerce(v)
    if help:
        exit(print("\n"+help+"\n"))
    return t

extract=re.findall(r"[-][-]([\S]+)[^\n]+= ([\S]+)",help)

for k,v in extract:
    the[k]=coerce(v)
