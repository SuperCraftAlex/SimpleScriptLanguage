import sys, os
import pathlib as path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import interpret as main
import storage

from math import cos



def command(args, optargs, bl):
    i1 = main.parsearg(args[0], bl)
    o = math.cos(i1)
    main.storeb(args[1], o, bl)