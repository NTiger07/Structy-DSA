edges1 = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]

def undirectedPath(edges, source, destination):
    graph1 = buildGraph(edges1)
    return hasPath(graph1, source, destination, set())
    
    
def hasPath(graph, source, destination, visited): # Solving recursively
    if source == destination: return True
    if source in visited: return False
    
    visited.add(source) # Keep track of visited nodes
    
    for neighbourNode in graph[source]:
        if hasPath(graph, neighbourNode, destination, visited) == True: return True
        
    return False

def buildGraph(edges): # Convert edges to graph
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

print(undirectedPath(edges1, "j", "m"))