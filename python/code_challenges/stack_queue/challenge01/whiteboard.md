# Stack and Queue Challenge-01 Document

## Problem Domain

Create a myQueue class which Implement FIFO Queue using 2 stacks, which support the methods add ``` push, peek, pop, and empty``` methods as well.

**Input** : myQueue.push(1)

**Output** : queue = [1]

## Test Cases

- input : myQueue.push(1) , queue=[1]
- input : myQueue.push(2) , queue=[1,2]
- input : myQueue.pop(), return 1 & queue=[2]
- input : myQueue.peek(), return 1
- input : myQueue.empty(), False



## Visualize

![stack&queue](stack%26queue.jpg)


## Algorithm

- create a class with empty queue list. 
- create ```push``` method accepts element,and append it to the queue list.
- create  ```pop``` method, which remove the first element in queue by create a new stack which append queue's elements reversely,pop the top element,then return queue elements with the same order to the queue list. 
- create ```peek``` method,which return the first value of queue.
- create ```empty``` method,which check if the length of queue = 0 ,will return True otherwise return False.


## Big O


The time complexity and space will depends on the amount of queue elements, as the pop method will loop through the queue.


**Time** :  O(n)

**Space**: O(n)



## Code

```
class MyQueue:



    def __init__(self) -> None:
       self.queue = []

    def push(self,element):
   
        self.queue.append(element)


    def pop(self):

         stack_1=self.queue
        stack_2=[]
        for i in range(len(stack_1)):
            
            stack_2.append(stack_1.pop())
        removed_item=stack_2.pop()
        self.queue=[]
        for i in range(len(stack_2)-1,-1,-1):
            self.queue.append(stack_2[i])
        return removed_item

    def peek(self):
    
        return self.queue[0]

    def empty(self):

        if len(self.queue)>0:
            return False
        else:
            return True

```


