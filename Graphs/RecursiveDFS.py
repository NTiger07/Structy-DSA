graph = {
    "a":['b', 'c'],
    "b":['d'],
    "c":['e'],
    "d":['f'],
    "e":[],
    "f":[],
}

def depthFirstPrint(graph, source):
    print(source) 
    for neighbourNode in graph[source]:
        depthFirstPrint(graph, neighbourNode)


depthFirstPrint(graph, "a") # abdfce / acebdf 