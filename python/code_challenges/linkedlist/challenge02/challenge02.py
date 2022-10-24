# Write here the code challenge solution
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








def middle_node(head):
    '''
    params: node or list of node
    return: a list of the middle node inside the linked list
    '''   
        
    new_arr=[]
    linked_list=[head]
    while linked_list[-1].next:
        linked_list.append(linked_list[-1].next)
    mid_node=linked_list[len(linked_list) // 2]
    while mid_node:
            new_arr.append(mid_node.value)
            mid_node=mid_node.next

    return new_arr









