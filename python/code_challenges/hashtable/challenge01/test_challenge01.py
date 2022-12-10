# Write your test here
from challenge01 import *
from node import *

def test_1():
    pre = [7,2,9,1,5,14]
    root = constructTree(pre)
    k=11
    actual=find_target(root,k)
    expect=True
    assert actual == expect


def test_2():
    pre = [7,2,9,1,5,14]
    root = constructTree(pre)
    k=20
    actual=find_target(root,k)
    expect=False
    assert actual == expect

def test_edge():
    pre = [28]
    root = constructTree(pre)
    k=28
    actual=find_target(root,k)
    expect=False
    assert actual == expect