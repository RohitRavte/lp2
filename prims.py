import heapq

def prim(graph):
    # Initialize an empty MST
    mst = []
    # Set of visited vertices
    visited = set()
    # Start from vertex 0
    start_vertex = list(graph.keys())[0]
    # Priority queue to store edges
    pq = [(0, start_vertex, None)]
    
    while pq:
        weight, current_vertex, previous_vertex = heapq.heappop(pq)
        if current_vertex not in visited:
            visited.add(current_vertex)
            if previous_vertex:
                mst.append((previous_vertex, current_vertex, weight))
            for neighbor, edge_weight in graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor, current_vertex))
    
    return mst


graph =  {

    'A':[('B',4),('C',1)],
    'B': [('A',4),('C',2),('D',5)],
    'C': [('A',1),('B',2),('D',3)],
    'D': [('B',5),('C',3)]

}
   


mst = prim(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
