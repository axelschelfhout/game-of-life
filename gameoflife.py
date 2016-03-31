from numpy import genfromtxt

data = genfromtxt('game-of-life-input1.csv', delimiter=',')

def gameoflife(data):
    dead = 0
    alive = 1

    data_length = len(data)
    data_counter = 0

    for row in data:

        if data_counter < data_length:

            row_length = len(row)
            row_counter = 0
            printer = ''

            for content in row:

                if row_counter < row_length:
                    alive_neighbours = 0

                    # Up

                    # Up Right

                    # Right

                    # Down Right

                    # Down

                    # Down Left

                    # Left

                    # Up Left

                    out = '*'
                    if int(content) == dead:
                        out = '.'

                    printer += str(out)
                    row_counter += 1
            print(printer)
        data_counter += 1

    return

i = 0
while i < 10:
    gameoflife(data)
    i += 1
