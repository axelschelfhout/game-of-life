from numpy import genfromtxt
import time
import sys

# Take in arguments from command line.
error = 0
iterations = 100
delay = 0
if len(sys.argv) > 1 < 4:
    try:
        iterations = int(sys.argv[1])
    except ValueError:
        error = 1
        print("The first argument should be used to give the amount of iterations you want to run. Defaults to 100")
        print("This should be an int")

    if len(sys.argv) == 3:
        try:
            delay = float(sys.argv[2])
        except ValueError:
            error = 1
            print("The second argument is the amount of delay (in seconds) you want for the iterations. Defaults to 0")
            print("This should be an int or float")

    if error == 1:
        exit()
# END Take in arguments from command line.

data = genfromtxt('game-of-life-input1.csv', delimiter=',')
#data = genfromtxt('example.csv', delimiter=',')

dead = 0
alive = 1


def game_of_life(data):

    amount_of_rows = len(data)
    row_counter = 0

    # Create new matrix to put the new cell states in
    # This is created with the amount of rows and columns
    new_data = [[0 for cols in range(amount_of_rows)] for rows in range(len(data[0]))]

    for row in data:
        row = list(map(int, row))  # Parse row to int

        if row_counter < amount_of_rows:

            row_length = len(row)
            cell_counter = 0

            for cell in row:

                if cell_counter < row_length:
                    alive_neighbours = 0

                    # Up
                    if row_counter == 0:
                        pass
                    elif data[row_counter-1][cell_counter] == alive:
                        alive_neighbours += 1

                    # Up Right
                    if row_counter == 0 or cell_counter == row_length - 1:
                        pass
                    elif data[row_counter - 1][cell_counter + 1] == alive:
                        alive_neighbours += 1

                    # Right
                    if cell_counter == row_length - 1:
                        pass
                    elif row[cell_counter + 1] == alive:
                        alive_neighbours += 1
                        
                    # Down Right
                    if row_counter == amount_of_rows - 1 or cell_counter == row_length - 1:
                        pass
                    elif data[row_counter + 1][cell_counter + 1] == alive:
                        alive_neighbours += 1

                    # Down
                    if row_counter == amount_of_rows - 1:
                        pass
                    elif data[row_counter + 1][cell_counter] == alive:
                        alive_neighbours += 1

                    # Down Left
                    if row_counter == amount_of_rows - 1 or cell_counter == 0:
                        pass
                    elif data[row_counter + 1][cell_counter - 1] == alive:
                        alive_neighbours += 1

                    # Left
                    if cell_counter == 0:
                        pass
                    elif row[cell_counter - 1] == alive:
                        alive_neighbours += 1

                    # Up Left
                    if row_counter == 0 or cell_counter == 0:
                        pass
                    elif data[row_counter - 1][cell_counter - 1] == alive:
                        alive_neighbours += 1

                    # Check if the cell should be alive or dead
                    if cell == alive and alive_neighbours == 2 or alive_neighbours == 3:
                        cell = alive
                    elif cell == dead and alive_neighbours == 3:
                        cell = alive
                    else:
                        cell = dead

                    new_data[row_counter][cell_counter] = cell

                    cell_counter += 1
        row_counter += 1
    return new_data


def print_game_of_life_on_data(input_data):
    printer = ''
    for row in input_data:
        for cell in row:
            out = '*'
            if cell == dead:
                out = '.'
            printer += str(out)
        printer += '\n'
    return printer


i = 0
while i < iterations:
    print(print_game_of_life_on_data(data))
    data = game_of_life(data)
    if delay > 0:
        time.sleep(delay)
    i += 1
