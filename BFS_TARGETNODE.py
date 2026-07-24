def bfs_search(graph, start, target):
    visited = []
    queue = []

    queue.append(start)
    visited.append(start)

    while queue:
        current = queue.pop(0)
        print(current, end=" ")

        if current == target:
            print("\nTarget found")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    print("\nTarget not found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs_search(graph, 'A', 'E')