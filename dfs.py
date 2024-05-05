class Graph:
    def __init__(self):
        self.graph={}


    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    
    def df(self,v,visited):
        visited.add(v)
        print(v,end=' ')

        
        
        for n in  self.graph[v]:
             if n not in visited:
                 self.df(n,visited)

    def dfs(self,start):
         visited=set()
         self.df(start,visited)
    

graph=Graph()

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(0,3)
graph.add_edge(3,7)
graph.add_edge(2,6)
graph.add_edge(1,5)
graph.add_edge(1,4)




a=int(input("enter the vertex you want to start :"))

graph.dfs(a)
 






