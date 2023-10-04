graph = {
    "a":['c', 'b'],
    "b":['d'],
    "c":['e'],
    "d":['f'],
    "e":[],
    "f":[],
}

def breadthFirstPrint(graph, source):
    queue = [source]
    while len(queue) > 0:
        currentNode = queue.pop(0) #remove the first element of the queue
        print(currentNode)
        for neighbourNode in graph[currentNode]:
            queue.append(neighbourNode)


breadthFirstPrint(graph, "a") # acbedf 