# Write here the code challenge solution
class Node:

    def __init__(self,val):
        self.val=val
    def __str__(self):
        return self.val



class Edge:

    def __init__(self,vertex,weight=0):

        self.vertex=vertex
        self.weight=weight


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
            return 'no edges found'

        return self.visited

    def __str__(self) :

        output=''

        for key in self.adj_list.keys():

            output +=f'{key} ---> '

            for data in self.adj_list[key]:

                output +=f'{data.vertex} --- > '

            output+= '\n'

        return output

if __name__=='__main__':
    graph=Graph()

    a=graph.add_node('a')
    b=graph.add_node('b')
    c=graph.add_node('c')
    d=graph.add_node('d')
    e=graph.add_node('e')
    f=graph.add_node('f')
    g=graph.add_node('g')
    h=graph.add_node('h')
    i=graph.add_node('i')
    k=graph.add_node('k')

    graph.add_edge(a,e)
    graph.add_edge(a,c)
    graph.add_edge(b,d)
    graph.add_edge(d,e)
    graph.add_edge(c,f)
    graph.add_edge(e,g)
    graph.add_edge(e,f)
    graph.add_edge(g,h)
    graph.add_edge(f,h)
    graph.add_edge(f,i)
    graph.add_edge(i,k)
    graph.add_edge(h,k)


    print(graph.bfs(a))
