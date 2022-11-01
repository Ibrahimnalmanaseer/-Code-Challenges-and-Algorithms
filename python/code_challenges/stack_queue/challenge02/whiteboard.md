# Stack and Queue Challenge-02 Document

## Problem Domain

create a validation function which accepts String, the function will check each Parentheses inside the given string are valid;(checking the open and the closed Parentheses and if they are in the correct order) .

**Input** : s="()[]{}"

**Output** : True

## Test Cases

- input : Input: s = "[({}]" ,False  
- input : s = "[(hello)()]" , True
- input : s = "[{(())}]", True
- input :s = "]", False
- input :s = "", False
- input :s = "hello", False


## Visualize

![stack](./Stack%20(8).jpg)


## Algorithm


- create a function accepts a string.
- loop through the given string chars, if the char is an open parentheses,it will be appended to a stack.
- if the char is not an open parentheses,the char will be combined to the top element of stack,to check if they form a correct pairs.
- the function will return true if the all chars forming a correct pairs ,otherwise will return False.

## Big O


The time complexity and space will depends on the amount of string elements amount, as the function will loop through the given string.


**Time** :  O(n)

**Space**: O(n)



## Code

```
def validate_Parentheses(s):

        open_char=['(', '{', '[' ] 
        close_char=[')','}',']']
        char_pairs=['()', '{}', '[]' ]

        char_open_stack=[]
       
   
        for i in s:

            if i in open_char:

                char_open_stack.append(i)
             

            elif len(char_open_stack):
                
                if char_open_stack[-1]+i in char_pairs:
                    char_open_stack.pop() 

                elif  i in close_char:
                    return False  
                           

            else :
                return False 
                                           
        if len(char_open_stack):
            return False

        else:
            return True

```


