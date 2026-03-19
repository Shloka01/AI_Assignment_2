import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))

    g = {start: 0}
    parent = {}

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for d in directions:
            neighbor = (current[0]+d[0], current[1]+d[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = g[current] + 1

                if neighbor not in g or new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    f = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f, neighbor))
                    parent[neighbor] = current

    return None
