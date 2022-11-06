# Write your test here
from challenge01 import Node,Tree

tree=Tree()

def test_binary_tree_1():

    root=tree.binary_tree([2,1,4],[1,2,4])
    tree.tree_list=[root.value]
    actual=tree.display_tree(root)
    expect=[2, 1, 4, 'null', 'null', 'null', 'null']
    assert actual == expect

def test_binary_tree_2():

    root=tree.binary_tree([-1],[-1])
    tree.tree_list=[root.value]
    actual=tree.display_tree(root)
    expect=[-1,'null','null']
    assert actual == expect

def test_binary_tree_3():

    

    root=tree.binary_tree([],[])
    try:
        tree.tree_list=[root.value]
    except AttributeError:
        tree.tree_list=[root]
    finally:
    
        actual=tree.display_tree(root)
        expect=['null']
    assert actual == expect


def test_binary_tree_4():

    root=tree.binary_tree([2,1],[1,2])
    tree.tree_list=[root.value]
    actual=tree.display_tree(root)
    expect=[2, 1, 'null', 'null', 'null']
    assert actual == expect