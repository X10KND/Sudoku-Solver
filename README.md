# Sudoku Solver

## Project Details

This project was created to solve [Sudoku](https://en.wikipedia.org/wiki/Sudoku) problems in a fast, efficient way. The program loads the Sudoku board and checks which values from 1 to 9 can be present in the empty cells. The check is performed in every row, column and 3x3 subgrid. If only one value can be present in the cell, that value is placed and the check is performed over and over again, until all the cells are filled, or the cells can have multiple values. For the later, a trail and error DFS method is used, where a value in a cell is guessed and see if a solution can be reached. This is done until a solution is reached.

## Instructions

Example board:

<table>
<tbody>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>6</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>7</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>9</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>5</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>5</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>2</td>
<td>&nbsp;</td>
<td>1</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>5</td>
<td>6</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>8</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>7</td>
<td>3</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>9</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>1</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>8</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>9</td>
<td>&nbsp;</td>
<td>8</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>7</td>
</tr>
<tr>
<td>5</td>
<td>3</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>4</td>
</tr>
</tbody>
</table>

`input.txt` file contents should be:

006007000  
000900005  
050020100  
000000560  
080073000  
900100000  
800000013  
009080007  
530000004

where the zeros represent blank space. Run the program to solve the board.

## Requirements

`pip install numpy`

## TODO

It is currently not tested how the program will perform with an invalid board. A JS version will be made for browser support. Program can be optimized further.