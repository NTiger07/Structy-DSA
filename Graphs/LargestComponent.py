graph1 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

def largestComponent(graph):
    visited = set()
    count = 0
    max = 0
    
    for node in graph:
        count =  explore(graph1, node, visited)
        if count > max:
            max = count
    return max
    
def explore(graph, currentNode, visited):
    if currentNode in visited: return 0
    visited.add(currentNode)
    count = 1
    
    for neighbourNode in graph[currentNode]:
        count += explore(graph1, neighbourNode, visited)
        
        
    return count


print(largestComponent(graph1))
    