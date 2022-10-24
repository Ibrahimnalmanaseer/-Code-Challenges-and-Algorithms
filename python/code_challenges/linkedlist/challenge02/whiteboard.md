# link list Challenge Document

## Problem Domain

Create a middle function which accept a node, to return the middle node that inside the linked list as a list.

**Input** : node

**Output** : the middle node's list

## Test Cases

- input = [1,2,3] , return [2,3]
- input = [1,2,3,4] , return [3,4]
- input = [1,2,3,4,5,6] , return [4,5,6]



## Visualize

![linked list](./linked%20list%20(4).jpg)


## Algorithm

- create a function which accepts a node . 
- create list which append all the linked list elements .
- find the middle node by dividing length of linked list by 2 .
- return the rest of linked list nodes starting from the middle node .


## Big O


the time complexity and space will depends on the linked list length , as the function will loop through the list elements.


**Time** :  O(n)

**Space**: O(n)



## Code
```
def middle_node(head):
 
        
    new_arr=[]
    linked_list=[head]
    while linked_list[-1].next:
        linked_list.append(linked_list[-1].next)
    mid_node=linked_list[len(linked_list) // 2]
    while mid_node:
            new_arr.append(mid_node.value)
            mid_node=mid_node.next

    return new_arr
```


## Step Through

![linked list](./linked%20list%20(5).jpg)