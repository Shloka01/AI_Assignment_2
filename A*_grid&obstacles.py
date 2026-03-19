import random

def generate_grid(size=70, density=0.2):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if random.random() < density:
                grid[i][j] = 1  # obstacle

    return grid
