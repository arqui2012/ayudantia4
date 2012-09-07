# -*- coding: UTF-8 -*-
import re

def polish(input):
    
    output = []
    stack = []

    for t in tokenize(input):
        if t == "+":
            while len(stack) > 0 and stack[-1] != "+":
                output.append(stack.pop())
            stack.append(t)
        elif t == "*":
            stack.append(t)
        elif t == "(":
            pass
        elif t == ")":
            pass
        else:
            output.append(t)
    while len(stack) > 0:
        output.append(stack.pop())

    return "".join(output)

def tokenize(input):
    return [c for c in input if re.match("[A-Z+\*()]", c)]