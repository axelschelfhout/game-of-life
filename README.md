# README #

### GAME OF LIFE ###

![life.png](https://bitbucket.org/repo/gz98nM/images/3328389336-life.png)

The challenge is based on John’s Conway ‘Game of Life’. The Game of Life is a cellular automaton developed by the British mathematician John Conway in 1970. The universe of the game is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell that is horizontally, vertically, or diagonally adjacent interacts with its eight neighbors. At each step in time, the following iterations occur:

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overcrowding.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths occur simultaneously. The rules continue to be applied repeatedly to create further generations.

You have a grid of size N×N, seeded with some live cells. Your task is to determine the state of the grid after 10 iterations.

### INPUT SAMPLE ###

The first argument is a file with the initial state of the grid. Alive cells are shown as asterisks ‘*’, and dead cells are shown as points ‘.’. E.g.

![Screen Shot 2016-03-22 at 9.02.44 PM.png](https://bitbucket.org/repo/gz98nM/images/1200975950-Screen%20Shot%202016-03-22%20at%209.02.44%20PM.png)


### OUTPUT SAMPLE ###

Print to stdout the state of the grid after 10 iterations. E.g.

![Screen Shot 2016-03-22 at 9.04.24 PM.png](https://bitbucket.org/repo/gz98nM/images/4049356696-Screen%20Shot%202016-03-22%20at%209.04.24%20PM.png)


### CONSTRAINTS ###

The size of the grid in real input is 100×100 cells.
The cells outside the grid borders are assumed to be dead.