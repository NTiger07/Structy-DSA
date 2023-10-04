graph = {
    "f":['g', 'i'],
    "g":['h'],
    "h":[],
    "i":['g', 'k'],
    "j":['i'],
    "k":[],
}

def hasPathDFS(graph, source, destination):
    if source == destination: return True
    
    for neighbourNode in graph[source]:
        if hasPathDFS(graph, neighbourNode, destination) == True:
            return True
        
    return False # Return false if the for loop is completed without returning True
        
    
    
print(hasPathDFS(graph, "f", "k"))
    