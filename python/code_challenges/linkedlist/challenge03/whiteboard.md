# link list Challenge Document

## Problem Domain

Create a remove n^th function which accept a node and nth node, to return remove the nth node and return a list of node values inside a linked list .

**Input** : Node , $n^{th}$

**Output** : a list of nodes values without the $n^{th}$ node. 

## Test Cases

- input : head= [1,2,3] n=2, return [1,3]
- input : head= [1] n=1, return []
- input : head= [1,2,3,5,6] n=1, return [1,2,3,5]



## Visualize

![linked list](./linked%20list%20(6).jpg)


## Algorithm

- create a function which accepts a node,and $n^{th}$ value. 
- create list which append all the linked list elements .
- loop through a  node list to find the $n^{th}$ node to remove it.
- return the updated list of nodes .


## Big O


the time complexity and space will depends on the linked list length , as the function will loop through the list elements.


**Time** :  O(n)

**Space**: O(n)



## Code
```
def remove_nth(head,n):

    new_arr=[head]
    
    while new_arr[-1].next:
        new_arr.append(new_arr[-1].next)
    
    current = head


    if head==new_arr[-+n]:

        head=head.next
        
    else:
        if current.next:

            while current.next!= new_arr[-+n]:

                current=current.next

            current.next = new_arr[-+n].next
        
        
    return head
```


## Step Through

![linked list](./linked%20list%20(7).jpg)