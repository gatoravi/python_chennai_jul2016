#! /usr/bin/env python

import sys

def hello():
    print("Hello World!")
    print("inside")

def sum(n1, n2):
    sum1 = n1 + n2
    return sum1

def greatest(g1, g2, g3):
    if g1 > g2:
        if g1 > g3:
            print(str(g1) + " is greatest")
            return g1
    elif g2 > g3:
            print(str(g2) + " is greatest")
            return g2
    else:
        print(g3, " is greatest")
        return g3

def toupperr(x):
    for fruit in x:
        print(fruit.upper())

def main():
    list1 = ["apple", "banana", "orange", "mango"]
    toupperr(list1)

hello() #function call
greatest_val = greatest(10, 20, 30)
