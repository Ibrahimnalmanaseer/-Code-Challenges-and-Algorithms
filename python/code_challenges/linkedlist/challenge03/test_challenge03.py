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

    actual=remove_nth(node1,2)
    expect=[1,3]

    assert actual==expect

def test_remove_end_2():
    '''
    test remove nth function
    '''
    linkedList1 = LinkedList()
    node1 = Node(1)
    
    actual=remove_nth(node1,1)
    expect=[]

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


    actual=remove_nth(node1,1)
    expect=[1,2,3,4]

    assert actual==expect


def test_remove_end_4():

    '''
    test remove nth function
    '''

    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)



    actual=remove_nth(node1,2)
    expect=[2]

    assert actual==expect