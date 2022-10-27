# link list Challenge Document

## Problem Domain

Create a delete function inside a linked list class which accept a node value, to be deleted from a  pre given linked list.

**Input** : linked list ,node value 

**Output** : updated linked list ;that does not contain the given node

## Test Cases

- linkedlist = [1,2,3] , node = 2  , return [1,3]
- linkedlist = [1,5,9] , node = 1 , return [5,9]
- linkedlist = [1,5,9] , node = 9 , return [1,5]


## Visualize

![linked list](./linked%20list%20(2).jpg)


## Algorithm



- create a function inside a class that accepts a node value, which needed to be deleted from the linked list.

- create a method to display the final updated linked list.


## Big O


1 node needs to be updated, and the time complexity is constant.


**Time** :  O(1)

**Space**: O(1)



## Code
```

def delete_node(node):

   

        nextNode = node.next
        node.value = nextNode.value
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)


```


## Step Through

Delete (node = 5)

![stepthrough](./linked%20list%20(3).jpg)