grid1 = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

def islandCount(grid):
    visited = set()
    count = 0
    
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if explore(grid1, row, column, visited) == True:
                count += 1
                
    return count
            
            
def explore(grid, row, column, visited):
    
    # Base cases...
    rowInbounds = 0 <= row and row < len(grid) # When exploring to make sure we don't go out of bounds
    columnInbounds = 0 <= column and column < len(grid[0])
    if rowInbounds == False or columnInbounds == False: return False
    
    if grid[row][column] == "W": return False # Return false if node is water
    position = (row, column)
    if position in visited: return False
    visited.add(position)
    
    # Now DFS... 
    explore(grid1, row - 1, column, visited) # Up
    explore(grid1, row + 1, column, visited) # Down
    explore(grid1, row, column - 1, visited) # Left
    explore(grid1, row, column + 1, visited) # Right
    
    return True
    



print(islandCount(grid1))