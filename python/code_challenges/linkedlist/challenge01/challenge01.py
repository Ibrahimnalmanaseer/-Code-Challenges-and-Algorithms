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


if __name__ == "__main__":
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


    linkedList1.display()