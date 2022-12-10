class Node():
 
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 

def getPreIndex():
    return constructTreeUtil.preIndex
 

 
def incrementPreIndex():
    constructTreeUtil.preIndex += 1
 

 
 
def constructTreeUtil(pre, low, high):
 
        # Base Case
    if(low > high):
        return None
 
    # The first node in preorder traversal is root. So take
    # the node at preIndex from pre[] and make it root,
    # and increment preIndex
    root = Node(pre[getPreIndex()])
    incrementPreIndex()
 
    # If the current subarray has onlye one element,
    # no need to recur
    if low == high:
        return root
 
    r_root = -1
 
    # Search for the first element greater than root
    for i in range(low, high+1):
        if (pre[i] > root.data):
            r_root = i
            break
 
    # If no elements are greater than the current root,
    # all elements are left children
    # so assign root appropriately
    if r_root == -1:
        r_root = getPreIndex() + (high - low)
 
    # Use the index of element found in preorder to divide
    # preorder array in two parts. Left subtree and right
    # subtree
    root.left = constructTreeUtil(pre, getPreIndex(), r_root-1)
 
    root.right = constructTreeUtil(pre, r_root, high)
 
    return root
 
# The main function to construct BST from given preorder
# traversal. This function mailny uses constructTreeUtil()
 
 
def constructTree(pre):
    size = len(pre)
    constructTreeUtil.preIndex = 0
    return constructTreeUtil(pre, 0, size-1)
 
 

 
 
# Driver code


   
  

