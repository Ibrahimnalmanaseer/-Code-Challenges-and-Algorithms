# Write here the code challenge solution
class Node:
    '''
    params: value
    return: a node value,with left and right values.
    
    '''
    def __init__(self,value) -> None:
        self.value=value
        self.right=None
        self.left=None

    

class Tree:

    new_arr1=[]
    def binary_tree(self, pre_order, in_order):
        '''
        params: pre_order list , in_order list
        
        return : root of tree 
    
        '''

        if in_order:

                root_idx = in_order.index(pre_order.pop(0))
                root = Node(in_order[root_idx])
                root.left = self.binary_tree(pre_order, in_order[:root_idx])
                root.right = self.binary_tree(pre_order, in_order[root_idx+1:])
                
             
                
                return root
       
       
   














def display_tree(root):


    
    
    if root :

        if root.left:
            
            new_arr.append(root.left.value)
            new_arr.append(root.right.value)
          

        else:

            if not root.left:
                new_arr.append('null')
        
            if not root.right:
                new_arr.append('null')

        display_tree(root.left)  
        display_tree(root.right)
   

    
       


        


    return new_arr  

rrr=Tree()
root=rrr.binary_tree([2,1,4],[1,2,4])

new_arr=[root.value]
print(display_tree(root))