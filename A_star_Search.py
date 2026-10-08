import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f_cost, current_node)
    open_list = [(heuristic[start], start)]

    # Cost from start node to each node
    g_cost = {start: 0}

    # To store the path
    parent = {start: None}

    while open_list:
        f_cost, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], g_cost[goal]

        # Explore neighbours
        for neighbour, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                f_cost = new_g + heuristic[neighbour]

                parent[neighbour] = current
                heapq.heappush(open_list, (f_cost, neighbour))

    return None, float('inf')


# Weighted graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'G': 0
}

start = 'A'
goal = 'G'

path, cost = a_star(graph, heuristic, start, goal)

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)