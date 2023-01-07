import heapq
def dijkstra(graph,node):
    #implement Dijkstra algorithm to return shorest path from a node in a graph
    distances={node:float('inf') for node in graph}
    distances[node]=0
    came_from={node:None for node in graph}
    queue=[(0,node)]
    
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        # relaxation
        for next_node,weight in graph[current_node].items():
            distance_temp=current_distance+weight
            if distance_temp<distances[next_node]:
                distances[next_node]=distance_temp
                came_from[next_node]=current_node
                heapq.heappush(queue,(distance_temp,next_node))
    return distances,came_from

graph={
    'U':{'V':2,'W':5,'X':1},
    'V':{'U':2,'X':2,'W':3},
    'W':{'V':3,'U':5,'X':3,'Y':1,'Z':5},
    'X':{'U':1,'V':2,'W':3,'Y':1},
    'Y':{'X':1,'W':1,'Z':1},
    'Z':{'W':5,'Y':1}
}
print(dijkstra(graph,'X'))
