import re
import sys


#command line arguments
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
    #convert input in the form of a string to appropriate data type int/bool/str
    def fun(s1):
        #returns boolean for the string
        if s=="true":
            return True
        elif s=="false":
            return False
        return s1
    #return integer of the number in the form of string or calls fun to return appropriately
    if re.match(r"^[0-9]+$",s):
        return int(s)
    else:
        return None or fun(s)

def cli(t):
    #Command Line Interface arguments processed
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
    #create "the" variable and parse through "help" to get the values needed
    the = {}
    extract = re.findall(r"[-][-]([\S]+)[^\n]+= ([\S]+)", help)
    for k, v in extract:
        the[k] = coerce(v)
    return the

the = fun_the()