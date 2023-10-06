edges1 = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"],
]


def shotestPath(edges, start, destination):
    graph = buildGraph(edges1)
    visited = set(start)
    queue = [[start, 0]]
    
    while len(queue) > 0:
        [node, distance] = queue.pop(0)    
        
        if node == destination:
            return distance
        
        for neighbourNode in graph[node]:
            if neighbourNode not in visited:
                visited.add(neighbourNode)
                queue.append([neighbourNode, distance + 1]) # Distance is plus 1 since it is a neighbour 
        
    return -1
    
def buildGraph(edges):
    graph = {}
    
    for edge in edges:
        [a, b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
            
        graph[a].append(b)
        graph[b].append(a)
        
    return graph



print(shotestPath(edges1, "w", "y"))