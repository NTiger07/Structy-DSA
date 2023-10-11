graph1 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}
def connectedComponentsCount(graph):
    visited1 = set()
    count = 0
    for node in graph1:
        if explore(graph1, node, visited1) == True: count += 1

    return count
    

def explore(graph, current, visited):
    if current in visited: return False

    visited.add(current)
    
    for neighbour in graph[current]:
        explore(graph, neighbour, visited)

    return True


print(connectedComponentsCount(graph1))