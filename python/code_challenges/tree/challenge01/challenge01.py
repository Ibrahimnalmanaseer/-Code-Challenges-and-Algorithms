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
        
        









rrr=Tree()
rrr.binary_tree([3,9,20,15,7],[9,3,15,20,7]).value


def display_tree(root):
    new_arr=[]
    right_root=root
    new_arr.append(root.value)
    while root.left and root.right:
        

        if root.left.value:

            new_arr.append(root.left.value)

        if root.right.value: 
            new_arr.append(root.right.value)
        root=root.left

    if not root.right: 
        new_arr.append('null')

    if not root.left:
        new_arr.append('null')
                
    
    while right_root.right:
        

        if right_root.left.value:

            new_arr.append(right_root.left.value)

        if right_root.right.value: 
            new_arr.append(right_root.right.value)
        right_root=right_root.right
       


        


    print(new_arr)      

display_tree(rrr.binary_tree([3,9,20,15,7],[9,3,15,20,7]))