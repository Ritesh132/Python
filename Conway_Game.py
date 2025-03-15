import random, time, copy

WIDTH = 60  # Grid width
HEIGHT = 20  # Grid height

# Initialize grid with random cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        column.append('#' if random.randint(0, 1) == 0 else ' ')
    nextCells.append(column)

while True:  # Main simulation loop
    print('\n' * 5)  # Clear screen
    currentCells = copy.deepcopy(nextCells)

    # Print the grid
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

    # Calculate next state
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count living neighbors
            numNeighbors = sum(
                currentCells[nx][ny] == '#'
                for nx, ny in [
                    (leftCoord, aboveCoord), (x, aboveCoord), (rightCoord, aboveCoord),
                    (leftCoord, y), (rightCoord, y),
                    (leftCoord, belowCoord), (x, belowCoord), (rightCoord, belowCoord)
                ]
            )

            # Apply Conway's rules
            if currentCells[x][y] == '#' and numNeighbors in (2, 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

    time.sleep(1)  # Slow down animation
