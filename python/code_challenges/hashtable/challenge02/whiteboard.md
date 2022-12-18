# Hash Table Challenge-01 Document

## Problem Domain

create a function which accepts a string and return the first repeated word.





**Input** : input = `'ASAC is a department at LTUC. ASAC teaches programming in LTUC.'`

**Output** : `ASAC`

## Test Cases

- input :` 'I am learning programming at ASAC.'`,return= `No Repetition`

### Edge Cases

- input :`'' `,return= `No Repetition`




## Visualize

![hash](./linked%20list%20(14).jpg)


## Algorithm


- Create a function which accepts `string` as input .
- The input will be separated to a list of `words`.
- Traverse the `words` list,each element will be added to the hash table as key ,and count frequency as a value.

- Traverse the `words` list and check if any word has frequency greater than 1.
- Return the first word and break the loop.





## Big O



**Time** :  O(n) 

**Space**: O(n)



## Code

```
def first_repeated(input):



    hashtable={}
    words_arr=input.split(' ')

    for word in words_arr:


        if word in hashtable.keys():

           hashtable[word]+=1 
           break
        
        hashtable[word]=1


    

    for word in words_arr:

       
        if hashtable[word]>1:


            return word
            break


    return 'No Repetition'
    


```
