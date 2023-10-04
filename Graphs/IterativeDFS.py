graph = {
    "a":['b', 'c'],
    "b":['d'],
    "c":['e'],
    "d":['f'],
    "e":[],
    "f":[],
}

def depthFirstPrint(graph, source):
    stack = [source]
    while len(stack) > 0:
        currentNode = stack.pop()
        print(currentNode)
        for neighbourNode in graph[currentNode]:
            stack.append(neighbourNode)


depthFirstPrint(graph, "a") # abdfce / acebdf 