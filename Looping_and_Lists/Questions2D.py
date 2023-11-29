from typing import Any

"""
2D lists are often useful for storing groups of data. They are also useful representations
for other concepts such as physical space in two or three dimensions. A chess board, for instance
can be represented as a 2d list where the outer list has 8 inner lists and the inner lists have
8 elements each (making 64 elements in total)
"""

# an empty 4*4 grid might be expressed as follows
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

"""
Question 1

Write a function create_empty_grid(dims: int, empty: Any) -> list[list[Any]] which takes two args: 
an integer arg, and an arg of any type which is used to represent an empty space. Your function should 
return a dim*dim 2D-list where each element is set to the value of the empty argument.

"""

def create_empty_grid(dims: int, empty: Any) -> list[list[Any]]:
    return [[0]] # change this return when you have finished your code


"""
Question 2

Create a function print_grid(list[list[Any]]) -> None, which prints out your grid in a grid like format. 
A 4*4 grid filled with 0s should look like this:

0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

You must write the function out in full this time (no help!)

"""

#write your answer to Q2 here

"""
Question 3

write a function num_moves(grid: list[list[Any]], x_cor: int, y_cor: int)-> int which returns the number of
mooves it takes to get from the bottom left hand position of the grid to the x,y coordinate passed as the second
and third arg of the function. Coordinates for any grid are set as follows. Assume that in a single move
you can only travel one position along the x axis or one position_along the y axis.

  1 2 3 4 - x_cors
4 0 0 0 0
3 0 0 0 0
2 0 0 0 0
1 0 0 0 0
|
y_cors

"""

def num_moves(grid: list[list[Any]], x_cor: int, y_cor: int)-> int:
    return 0