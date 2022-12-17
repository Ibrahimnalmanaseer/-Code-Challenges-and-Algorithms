# Hash Table Challenge-01 Document

## Problem Domain

create a method which accepts a root of graph, to return all the graph's vertexes value inside an array.





**Input** : root = `["A"]`

**Output** : `["A", "C", "E", "B", "F", "G", "D", "I", "H", 'K']`

## Test Cases

- input : root = `['A']`,graph= ```{'A':[['B',0],['C',0]],
'B':[['A',0],['C',0]],
'C':[['A',0],['B',0]],
'D':[['C',0]]
}```,
 return : `["A", "B", "C", "D"]`

### Edge Cases

- input : root = `['A']`, graph=`{'A':[] }`, return = `'Graph have no edges'`




## Visualize

![hash](./linked%20list%20(13).jpg)


## Algorithm


- create a method which accepts `root` of graph.
- the root value will be appended to the `visited` list.
- then the method will loop through root's edges and repeat the process recursively.




## Big O



**Time** :  O(n + v) where n is the number of nodes and v is the number of edges.

**Space**: O(n)



## Code

```
class Graph:

    def __init__(self):

        self.adj_list={}
        
        self.visited=[]




    def add_node(self,node):

        node_1=Node(node)
        self.adj_list[node_1]=[]

        return node_1

    
    def add_edge(self,node1,node2):

        if not node1 in self.adj_list.keys() or not node2 in self.adj_list.keys():

            print( 'node not founded')

        vertex_1=Edge(node2)

        self.adj_list[node1].append(vertex_1)

        vertex_2=Edge(node1)

        self.adj_list[node2].append(vertex_2)


    def bfs(self,root):


        if root.val in self.visited:

            return 

        self.visited.append(root.val)
        if self.adj_list[root]:
            for node in self.adj_list[root]:
                self.bfs(node.vertex)
                
        else:
            print('no edges found')

        return self.visited

        

    


```
