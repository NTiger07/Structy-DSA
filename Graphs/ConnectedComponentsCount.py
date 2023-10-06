graph1 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
} # 2


def connectedComponentsCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph1, node, visited) == True: # To explore down a node as far as possible
            count += 1
            
    return count
        
def explore(graph, currentNode, visited):
    if currentNode in visited: return False
    visited.add(currentNode)
    
    
    for neighbourNode in graph[currentNode]: #Explore all neighbours of Current Node
        explore(graph1, neighbourNode, visited)
        
    return True
    
    
    
    
    
    
    
    
print(connectedComponentsCount(graph1))