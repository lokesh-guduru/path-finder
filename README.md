# Path finder
This project was completed for an Algorithms class at USF. The purpose of the project is to find a path from the starting position to the bullseye on a board of colored balls. The balls are represented as a 2D list, where each element is a tuple containing the color of the ball and the direction of the ball's arrow.

## Requirements
This project requires Python 3 to be installed on your system

## Usage
To run the program, navigate to the directory where the pathfinder.py file is located and execute the following command in the terminal:

python pathfinder.py input_file.txt

Replace input_file.txt with the name of the input file you want to use.

The program will output the solution path to a file named input_file-sol.txt in the same directory.

You can verify your solution using verifyGraph.py

I'm uploading some input and output files.

## Functionality
The program uses a Depth First Search algorithm to find a path from the starting position to the bullseye on the board. The algorithm starts at the top-left corner of the board and explores all possible paths until it reaches the bullseye. If no path is found, the program will return "No solution".

The program takes the following steps:

1. Reads the input file and constructs a 2D list representing the board.
2. Calls the 'findPath()' function to find the solution path.
3. 'findPath()' function uses DFS algorithm to find the solution path.
4. Writes the solution path to an output file.

## Limitations
The program has a recursion limit of 100000. This may cause the program to crash if the input file is very large. If you encounter this issue, try increasing the recursion limit.
