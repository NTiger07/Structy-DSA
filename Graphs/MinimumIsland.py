grid1 = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

def minimumIsland(grid):
    visited = set()
    min = 100
    
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            count = explore(grid1, row, column, visited)
            if count > 0 and count < min:
                min = count
                
    return min


def explore(grid, row, column, visited):
    
    # Base cases...
    rowInbounds = 0 <= row and row < len(grid) # When exploring to make sure we don't go out of bounds
    columnInbounds = 0 <= column and column < len(grid[0])
    if rowInbounds == False or columnInbounds == False: return 0
    if grid[row][column] == "W": return 0 # Return false if node is water
    position = (row, column)
    if position in visited: return 0
    visited.add(position)
    
    # Now DFS... 
    count = 1
    
    count += explore(grid1, row - 1, column, visited) # Up
    count += explore(grid1, row + 1, column, visited) # Down
    count += explore(grid1, row, column - 1, visited) # Left
    count += explore(grid1, row, column + 1, visited) # Right
    
    return count
    
    
    
        
        





print(minimumIsland(grid1))