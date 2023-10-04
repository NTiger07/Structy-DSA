graph = {
    "f":['g', 'i'],
    "g":['h'],
    "h":[],
    "i":['g', 'k'],
    "j":['i'],
    "k":[],
}

def hasPathBFS(graph, source, destination):
    queue = [source]
    
    while len(queue) > 0:
        currentNode = queue.pop(0)
        if source == destination: return True
        for neighbourNode in graph[currentNode]:
            queue.append(neighbourNode)
    return False
        
    
    
print(hasPathBFS(graph, "f", "k"))
    