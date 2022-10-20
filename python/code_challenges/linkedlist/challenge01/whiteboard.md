# link list Challenge Document

## Problem Domain

Create a delete function inside a linked list class which accept a node value, to be deleted from a  pre given linked list.

**Input** : linked list ,node value 

**Output** : updated linked list ;that does not contain the given node

## Test Cases

- linkedlist = [1,2,3] , node = 2  , return [1,3]
- linkedlist = [1] , node = 1 , return []
- linkedlist = [1,5,9] , node = 1 , return [5,9]
- linkedlist = [1,5,9] , node = 9 , return [1,5]


## Visualize

![linked list](./linked%20list%20(2).jpg)


## Algorithm

- create a class accept node value
- create  linked list class that can create a linked list ,- - using appending method that accepts a node.
- create a method inside a class that accepts a node value, which needed to be deleted from the linked list.

- create a method to display the final updated linked list.


## Big O


In append or delete methods , will loop through the list elements, the time complexity and space will depends on length of the linked list .


**Time** :  O(n)

**Space**: O(n)



## Code
```

class Node:
    def __init__(self,node) -> None:
        self.value=node
        self.next=None


class LinkedList:

    def __init__(self) -> None:


        self.head=None
    def append(self,node):
           if self.head==None:

                self.head=node

           else:
                current_node=self.head
                while current_node.next is not None:

                    current_node=current_node.next

                current_node.next=node


    def delete_node(self,node):
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
        output=[]



        current = self.head
        while current is not None:
            output.append(current.value)

            current = current.next

        return output


```


## Step Through

Delete (node = 5)

![stepthrough](./linked%20list%20(3).jpg)