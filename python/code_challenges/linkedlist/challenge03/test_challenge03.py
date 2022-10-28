# Write your test here
from challenge03 import Node,LinkedList,remove_nth



def test_remove_end_1():

    '''
    
    test remove nth function
   
    '''

    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(3)
    linkedList1.append(node3)
    remove_nth(node1,2)
    actual=linkedList1.display()
    expect=[1,3]

    assert actual==expect

def test_remove_end_2():
    '''
    test remove nth function
    '''
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    remove_nth(node1,1)
    actual=linkedList1.display()
    expect=[1]

    assert actual==expect



def test_remove_end_3():

    '''
     test remove nth function
    '''

    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node2 = Node(3)
    linkedList1.append(node2)
    node2 = Node(4)
    linkedList1.append(node2)
    node2 = Node(5)
    linkedList1.append(node2)
    remove_nth(node1,4)

    actual=linkedList1.display()
    expect=[1,3,4,5]

    assert actual==expect


