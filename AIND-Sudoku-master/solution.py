assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
        box(str): a string for the key of the box to be changed
        value(str): a string for the value of the box to be changed
    Returns:
        the values dictionary with the updated value
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find boxes that may be twins
    doubles = [box for box in values.keys() if len(values[box]) == 2]
    for box in doubles:
        val = values[box]
        for unit in units[box]:
            for el in unit:
                # Check if double has a twin here
                if values[el] == val and el != box:
                    for el in unit:
                        # Don't remove digits from the twins
                        if values[el] != val:
                            rep = values[el].replace(val[0],'').replace(val[1],'')
                            # Remove the naked twins as possibilities for their peers
                            assign_value(values, el, rep)
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

#Create variables for segments of sudoku puzzle
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal1 = [[a[0]+a[1] for a in zip(rows,cols)]]
diagonal2 = [[a[0]+a[1] for a in zip(rows,cols[::-1])]]
unitlist = row_units + column_units + square_units + diagonal1 + diagonal2
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    res = {}
    for i, b in enumerate(boxes):
        res[b] = grid[i] if grid[i] != '.' else '123456789'
    return res

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved = []
    for key, value in values.items():
        if len(value)==1:
            solved.append(key)
    for key in solved:
        for peer in peers[key]:
            val = values[peer].replace(values[key],'')
            assign_value(values, peer, val)
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for num in '123456789':
            boxes_w_num = [box for box in unit if num in values[box]]
            if len(boxes_w_num) == 1:
                assign_value(values, boxes_w_num[0], num)
    return values

def reduce_puzzle(values):
    """Loop through the puzzle, reducing the unsolved squares by eliminating values, picking the only choice, and removing naked twins until the puzzle does not change.

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        Resulting Sudoku in dictionary form after reducing the unsolved boxes
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Reduce using eliminate
        values = eliminate(values)
        # Reduce using only_choice
        values = only_choice(values)
        # Reduce using naked_twins
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """Using depth-first search and propagation, create a search tree and solve the sudoku.
    Args: values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns: Resulting Sudoku in dictionary form if puzzle is solved, else returns False
    """
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values == False:
        return False
    elif all(len(values[s]) == 1 for s in boxes):
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value, return that answer
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    sol = search(values)
    if sol:
        return sol
    return False

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
