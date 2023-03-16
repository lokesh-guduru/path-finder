import sys
sys.setrecursionlimit(100000)
def construct2DArrayFromFile(filename):
    # Open the file
    infile = open(filename, "r")
    # Read the first line
    line = infile.readline()
    # Split the line into a list
    line = line.split()
    # Convert the first two elements to integers
    rows = int(line[0])
    cols = int(line[1])
    # Create a 2D list
    array = [[0] * cols for i in range(rows)]
    # Read the rest of the lines
    for i in range(rows):
        line = infile.readline()
        line = line.split()
        for j in range(cols):
            array[i][j] = tuple(line[j].split('-'))
    # Close the file
    infile.close
    # Return the array
    return array

def writeOutfile(path):
    # Open the file
    outfile = sys.argv[1].split('.')[0] + '-sol.txt'
    f = open(outfile, "w")
    # Write the solution
    f.write(path)
    # Close the file
    f.close()

def getDirections(direction):
    #Create a dictionary
    dirToMap = {}
    #Add the directions to the dictionary
    dirToMap['N'] = (-1, 0)
    dirToMap['S'] = (1, 0)
    dirToMap['W'] = (0, -1)
    dirToMap['E'] = (0, 1)
    dirToMap['NW'] = (-1, -1)
    dirToMap['NE'] = (-1, 1)
    dirToMap['SW'] = (1, -1)
    dirToMap['SE'] = (1, 1)
    return dirToMap[direction]

def nextPossiblePositions(graph, i, j):
    # Get the number of rows and columns
    rows = len(graph)
    cols = len(graph[0])
    # Get the parent color and direction
    color = graph[i][j][0]
    dir = graph[i][j][1]
    children = []
    # Get the next position in the parent direction
    di, dj = getDirections(dir)
    cost = 0
    while True:
        # Get the next position
        i += di
        j += dj
        cost += 1
        # Check if the next position is out of bounds
        if i < 0 or i >= rows or j < 0 or j >= cols:
            break
        # Check if the next position is different from the parent color
        if graph[i][j][0] != color:
            children.append((i,j, cost))
    return children

def DFS(graph, i, j, visited, path):
    # Get the number of rows and columns
    rows = len(graph)
    cols = len(graph[0])
    # Check if the current position is valid
    if i<0 or i>=rows or j<0 or j>=cols:
        return
    # Check if the current position is visited
    if visited[i][j]:
        return
    # Mark the current position as visited
    visited[i][j] = True
    # Check if the current position is the goal
    if graph[i][j][0] == 'O':
        print(path)
        writeOutfile(path)
        return
    # Get the parent color and direction
    color = graph[i][j][0]
    dir = graph[i][j][1]
    # Get the next position in the parent direction
    children = nextPossiblePositions(graph, i, j)
    # Loop over the children
    for child in children:
        DFS(graph, child[0], child[1], visited, path + str(child[2]) + dir + ' ')
    return

    

def findPath(graph):
    #DFS Redursive
    #Step 1: Check if the current position is valid
    #Step 2: If the current position is bullseye the generate the path.
    #Step 3: Traverse through the path provided by current position and find all the opposite color balls.
    #Step 4: Add the child to visited and call the DFS again making the child as the parent.
    #Step 4: Do this until the bull eye is found or all the nodes are visited
    #Step 5: If the bull eye is not found then backtrack and remove the last node from the path and visited list
    #Step 6: Repeat the process until the path is empty
    #Step 7: If the path is empty then return no solution
    #Step 8: If the solution is found then return the path
    #Step 9: Write the path to the output file
    #Step 10: Close the file
    #Step 11: Exit the program
    #Step 12: End
    DFS(graph, 0, 0, [[False] * len(graph[0]) for i in range(len(graph))], '')

def main():
    # Get the graph from the file
    graph = construct2DArrayFromFile(sys.argv[1])
    # Find the path
    findPath(graph)

if __name__ == "__main__":
    main()



    