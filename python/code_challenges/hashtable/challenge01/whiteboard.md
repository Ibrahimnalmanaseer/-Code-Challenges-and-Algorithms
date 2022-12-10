# Hash Table Challenge-01 Document

## Problem Domain

by given a BTS and number, return true if the sum of two element of BTS equal the given number and false otherwise.




**Input** : root = [5,3,6,2,4,null,7], k = 9 

**Output** : `True`

## Test Cases

- input : root = [7,2,9,1,5,null,14], k = 3; Output: True
- input : root = [7,5,9,2,4,8,10], k = 30; Output:False


### Edge Cases

- input : root = [28], k = 28; Output:False




## Visualize

![hash](./linked%20list%20(12).jpg)


## Algorithm


- create a function which accept `BTS` and Number as `K`.
- the function will traverse tree using `recursive`.
- the elements will be appended to the hashtable; *each appended element's index == element value.*
- while appending to the hashtable the function will check if the `current element == K - element.value` inside the hashtable ,otherwise append it. 
- once the element found in hashtable the result will be `True`,otherwise `False`.




## Big O



**Time** :  O(n)

**Space**: O(n)



## Code

```
def find_target(root,k):

    if not root:
        return False

    binary_list = [root]

    hash_set = set()

    for root in binary_list:
        
        
        if k - root.val in hash_set: 
            return True
    
        hash_set.add(root.val)

        if root.left:
                binary_list.append(root.left)
        if root.right:
                binary_list.append(root.right)

    return False


```
