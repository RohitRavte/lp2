
import heapq





def dk(graph,start):
    distances={node:float('inf')for node in graph}
    distances[start]=0

    heap=[(0,start)]

    while heap:
        curr_dist,curr_node=heapq.heappop(heap)
        if curr_dist> distances[curr_node]:
            continue
        
        for n,wt in graph[curr_node].items():
           distance=wt+curr_dist
           if distance<distances[n]:
               distances[n]=distance
               heapq.heappush(heap,(distance,n))
    return distances
            
               







graph = {
   0:{1:4 ,7:8},
   1:{0:4,2:8,7:22},
   2:{1:8,3:7,8:2,5:4},
   3:{2:7,4:9},
   4:{3:4,5:10},
   5:{4:10,6:2,2:4},
   6:{5:2,8:6,7:1},
   7:{0:8,6:1,8:7,1:11},
   8:{7:7,6:6}
}
start_node = int(input("enter the start node :"))

distances = dk(graph,start_node)

print(f"Shortest path from {start_node}: ")
for node,dist in distances.items():
    print(f"{node}=> {dist}")