# Write here the code challenge solution

class MyQueue:

    '''
    Create a queue list
    
    '''

    def __init__(self) -> None:
       self.queue = []

    def push(self,element):
        '''
        params : element
        
        add the given element to the queue list 
        '''



        self.queue.append(element)


    def pop(self):

        '''
        delete the first element of the queue's list 
        return : the removed value 
        '''

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
        '''
        return: the first value of queue's list 
        '''

        return self.queue[0]

    def empty(self):

        '''
        Check if the queue wether have an element or not 
        return : False if the queue list out of elements ,True if the queue have no elements 
        '''

        if len(self.queue)>0:
            return False
        else:
            return True



