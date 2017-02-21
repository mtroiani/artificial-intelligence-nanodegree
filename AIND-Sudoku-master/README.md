# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: In sudoku naked twins occur when two boxes in the same unit only have the same two possible values as possibilities. A unit can be a row, column, 3x3 cube, or depending on the game, one of the two major diagonals. Units can only have one instance of each digit from 1 through 9. When two boxes have only the same two possible values we don't know which box will have which value, but we know that no other box can have either of those two values because once we determine one of them we immediately know the other. Therefore, in this case we can remove both of these possible numbers from all other boxes in the same unit. Using constraint propagation we can we can continue reducing the unsolved boxes in the puzzle with the naked twins, elimination, and only choice techniques. This pattern can also be extended to triplets (where three boxes have the same three possibilities) and more.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: To solve the diagonal sudoku problem we added the two major diagonals (from top left to bottom right and from bottom left to top right of the grid) to the group of units. Each unit (row, column, 3x3 square, and major diagonal) can only have one instance of each digit from 1 through 9, so we know that if a digit occurs within a unit no other box in the unit can contain that digit, and since each box needs a digit we know that if there is only one possibility for that box it can be assigned to that box. By adding the two major diagonals to our list of units our agent also enforces these constraints to the diagonals, allowing our sudoku solver to reduce the unsolved boxes in the puzzle for diagonal sudoku in addition to regular sudoku. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
