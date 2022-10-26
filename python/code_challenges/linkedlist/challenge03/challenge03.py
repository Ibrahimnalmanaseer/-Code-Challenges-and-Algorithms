# Write here the code challenge solution
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


    def delete_node(self,node):

        '''
        params: node value
        :return : delete node from a list 

        '''

        current=self.head

        if current.value==node:
                self.head=current.next

        else:

                while current is not None:
                    if current.value == node:
                        break
                    previous_node = current
                    current = current.next
                
                previous_node.next = current.next


    def display(self):
        '''
        :return: a list of linked list elements
        '''
        output=[]
        
            
        
        current = self.head
        while current is not None:
            output.append(current.value)
                
            current = current.next

        return output



def remove_nth(head,n):
    '''
    params: Node , n^th node
    delete n^th node from the linked list ,and return a list of node values .
    
    '''
    new_arr=[head]
    output_list=[]
    while new_arr[-1].next:
        new_arr.append(new_arr[-1].next)
    
    current = head
    if current.next:

        while current!= new_arr[-+n]:

            current=current.next

        current.next = new_arr[-+n].next
    del(new_arr[-+n])

    for i in new_arr:
        output_list.append(i.value)
    return output_list
        




