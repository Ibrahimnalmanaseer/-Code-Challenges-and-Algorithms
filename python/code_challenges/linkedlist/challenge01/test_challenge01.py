# Write your test here
from challenge01 import Node,LinkedList

def test_append_1():

    
    linkedList1 = LinkedList()
    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)

    actual=linkedList1.display()
    expect= ['A', 'B', 'C', 'D']
    assert actual == expect


def test_delete_1():

    
    linkedList1 = LinkedList()
    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)
    linkedList1.delete_node('C')
    actual=linkedList1.display()
    expect= ['A', 'B', 'D']
    assert actual == expect


def test_delete_head():

    
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(2)
    linkedList1.append(node2)

    node3 = Node(3)
    linkedList1.append(node3)

    node4 = Node(4)
    linkedList1.append(node4)
    linkedList1.delete_node(1)
    actual=linkedList1.display()
    expect= [2 , 3, 4]
    assert actual == expect


def test_delete_last():

    
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(2)
    linkedList1.append(node2)

    node3 = Node(3)
    linkedList1.append(node3)

    node4 = Node(4)
    linkedList1.append(node4)
    linkedList1.delete_node(4)
    actual=linkedList1.display()
    expect= [1, 2 , 3]
    assert actual == expect


def test_delete_2():

    
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)


    linkedList1.delete_node(1)
    actual=linkedList1.display()
    expect= []
    assert actual == expect
