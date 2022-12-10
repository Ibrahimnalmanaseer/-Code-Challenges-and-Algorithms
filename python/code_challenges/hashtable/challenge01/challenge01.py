
def find_target(root,k):

    if not root:
        return False

    binary_list = [root]

    hash_set = set()

    for root in binary_list:
        
        
        if k - root.data in hash_set: 
            return True
    
        hash_set.add(root.data)

        if root.left:
                binary_list.append(root.left)
        if root.right:
                binary_list.append(root.right)

    return False



