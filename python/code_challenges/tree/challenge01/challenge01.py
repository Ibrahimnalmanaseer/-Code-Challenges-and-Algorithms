# # Write here the code challenge solution
# class Node:
#     '''
#     params: value
#     return: a node value,with left and right values.
    
#     '''
#     def __init__(self,value) -> None:
#         self.value=value
#         self.right=None
#         self.left=None


    

# class Tree:


#     def __init__(self) -> None:
         
#          self.tree_list=[]


#     def binary_tree(self, pre_order, in_order):
#         '''
#         params: pre_order list , in_order list
        
#         return : root of tree 
    
#         '''

#         if in_order:

#                 root_idx = in_order.index(pre_order.pop(0))
#                 root = Node(in_order[root_idx])
#                 root.left = self.binary_tree(pre_order, in_order[:root_idx])
#                 root.right = self.binary_tree(pre_order, in_order[root_idx+1:])
                
             
                
#                 return root
       
       

#     def display_tree(self,root):

#                 '''
#                 params: root
                    
#                 return : all the roots values as a list 

#                 '''
                
            
#                 if not root:

#                     return ['null']               
                    
                
                
#                 if root :

#                     if root.left:

                        
#                         self.tree_list.append(root.left.value)
#                         try:
#                             self.tree_list.append(root.right.value)
#                         except AttributeError:
#                             self.tree_list.append('null')
                    

#                     else:

#                         if not root.left:
#                             self.tree_list.append('null')
                    
#                         if not root.right:
#                             self.tree_list.append('null')

#                     self.display_tree(root.left)  
#                     self.display_tree(root.right)   
                
               

#                 return self.tree_list 



# # rrr=Tree()


# # root=rrr.binary_tree([2,1],[1,2])

# # try:
    
# #     rrr.tree_list=[root.value]

# # except AttributeError:
# #     rrr.tree_list=[root]

# # finally:

# #     print(rrr.display_tree(root))


def check_if_merror(root_1,roo_2):

    current=root_1

    
    if current.left != roo_2.right:
        return False

    if current.right!= roo_2.left:
         return False

    

    if current.left == roo_2.right:

        current=current.left






