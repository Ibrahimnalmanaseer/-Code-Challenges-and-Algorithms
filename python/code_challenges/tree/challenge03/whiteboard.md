# Tree Challenge-01 Document

## Problem Domain

convert a given list to a height-balanced BST tree; each root's two subtrees have the same depth.




**Input** : nums = [-10,-3,0,5,9]

**Output** : [0,-3,9,-10,null,5]

## Test Cases

- input : nums=[1,2,4,5,6], Output:[4,2,5,1,null,null,6]
- input : nums=[1,2], Output:[2,1,null]


### Edge Cases

- input : nums=[], Output:['null']





## Visualize

![tree](./tree%20(11).jpg)


## Algorithm


- create a method which accepts a list.
- the method will check the middle element in list , to be considered as the first root in tree.
- then the method will take the middle element of left sub list as a left root as same as the right sub list.
- the method will be called recursively.




## Big O



**Time** :  O(n log n)

**Space**: O(n)



## Code

```
def convert_to_bts(self,nums):



        idx=len(nums)//2

        if  not nums:

            return None
        
        left= nums[:idx]
        right=nums[idx+1:]
        root=Node(nums[idx],self.convert_to_bts(left),self.convert_to_bts(right))   

        return root

        

```
