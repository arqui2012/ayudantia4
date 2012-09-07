# -*- coding: UTF-8 -*-
import re

def polish(input):
    
    ouput = []
    stack = []

    for t in tokenize(input):
        if t == "+":
            output.append(t)
        elif t == "*":
            pass
        elif t == "(":
            pass
        elif t == ")":
            pass
        else:
            output.append(t)

    return "".join(output)

def tokenize(input):
    return [c for c in input if re.match("[A-Z+\*()]", c)]