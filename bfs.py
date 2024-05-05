from collections import deque

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

    
    def bfs(self ,start):
        visited=set()
        q=deque([start])
        visited.add(start)


        while q:
            v=q.popleft()
            print(v,end=' ')


            for n in self.graph:
                if n not in visited:
                    q.append(n)
                    visited.add(n)


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 3)




a=int(input("enter from where to start"))

graph.bfs(a)
