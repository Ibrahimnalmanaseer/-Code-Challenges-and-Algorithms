# Write here the code challenge solution
from os import remove


class Node:

    def __init__(self,node) -> None:
        self.value=node
        self.next=None



class LinkedList:
    '''
    Create a link list ,Append nodes ,Delete nodes 

    '''
    def __init__(self) -> None:
        
        
        self.head=None
    def append(self,node):

        '''
        params: node 
        :return: append node into a link list

        '''
        if self.head==None:

                self.head=node

        else: 
                current_node=self.head
                while current_node.next is not None:

                    current_node=current_node.next

                current_node.next=node



    def display(self):
        '''
        :return: a list of linked list elements
        '''
        
        
        new_arr=[]    
        
        current = self.head
        while current is not None:
            
              new_arr.append(current.value)  
              current = current.next
              
        return new_arr




def delete_node(node):

        '''
        params: node value
        :return : delete node from a list 

        '''

        nextNode = node.next
        node.value = nextNode.value
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)

                
                



linkedList1 = LinkedList()
node1 = Node(1)
linkedList1.append(node1)
node2 = Node(2)
linkedList1.append(node2)
node3 = Node(3)
linkedList1.append(node3)
delete_node(node2)   
print(linkedList1.display())