# # Write your test here
from challenge01 import Node,LinkedList,delete_node





def test_delete_1():
    '''
    test delete method 
    '''
    
    linkedList1 = LinkedList()
    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)
    delete_node(node3)
    actual=linkedList1.display()
    expect= ['A', 'B', 'D']
    assert actual == expect


def test_delete_head():
    '''
    test delete method 
    '''
    
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(2)
    linkedList1.append(node2)

    node3 = Node(3)
    linkedList1.append(node3)

    node4 = Node(4)
    linkedList1.append(node4)
    delete_node(node1)
    actual=linkedList1.display()
    expect= [2 , 3, 4]
    assert actual == expect





def test_delete_2():
    '''
    test delete method 
    '''
    
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(1)
    linkedList1.append(node2)
    node3 = Node(1)
    linkedList1.append(node3)
    delete_node(node1)
    actual=linkedList1.display()
    expect= [1,1]
    assert actual == expect
