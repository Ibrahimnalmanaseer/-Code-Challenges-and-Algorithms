# Write your test here
from challenge02 import Node,LinkedList,middle_node



def test_middle_node_1():

    '''
    test middle node
    '''

    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(3)
    linkedList1.append(node3)

    actual=middle_node(node1)
    expect=[2,3]

    assert actual==expect

def test_middle_node_2():

    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(3)
    linkedList1.append(node3)
    node4 = Node(4)
    linkedList1.append(node4)
    node5 = Node(5)
    linkedList1.append(node5)
    node6 = Node(6)
    linkedList1.append(node6)
    actual=middle_node(node1)
    expect=[4,5,6]

    assert actual==expect



def test_middle_node_3():

    '''
    test middle node
    '''

    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)


    actual=middle_node(node1)
    expect=[2]

    assert actual==expect