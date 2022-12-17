# Write your test here
# Write your test here
from challenge01 import *


def test_1():
    
    graph=Graph()

    a=graph.add_node('a')
    b=graph.add_node('b')
    c=graph.add_node('c')
    d=graph.add_node('d')
    graph.add_edge(a,b)
    graph.add_edge(a,c)
    graph.add_edge(c,d)


    actual=graph.bfs(a)
    expect=['a', 'b', 'c', 'd']
    assert actual == expect


def test_edge():
    graph=Graph()

    a=graph.add_node('a')
    b=graph.add_node('b')

    actual=graph.bfs(a)
    expect='no edges found'
    assert actual == expect

def test_3():
    graph=Graph()

    a=graph.add_node('a')
    b=graph.add_node('b')
    c=graph.add_node('c')
    d=graph.add_node('d')
    e=graph.add_node('e')
    f=graph.add_node('f')
    g=graph.add_node('g')
    h=graph.add_node('h')
    i=graph.add_node('i')
    k=graph.add_node('k')

    graph.add_edge(a,e)
    graph.add_edge(a,c)
    graph.add_edge(b,d)
    graph.add_edge(d,e)
    graph.add_edge(c,f)
    graph.add_edge(e,g)
    graph.add_edge(e,f)
    graph.add_edge(g,h)
    graph.add_edge(f,h)
    graph.add_edge(f,i)
    graph.add_edge(i,k)
    graph.add_edge(h,k)

    actual=graph.bfs(a)
    expect=['a', 'e', 'd', 'b', 'g', 'h', 'f', 'c', 'i', 'k']
    assert actual == expect