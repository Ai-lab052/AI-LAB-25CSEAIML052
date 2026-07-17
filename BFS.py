def bfs(graph, start):
    # Create an empty list called visited
    visited = []

    # Create an empty list called queue
    queue = []

    # Put start node into queue
    queue.append(start)

    # Mark the start node as visited
    visited.append(start)

    # While the queue is not empty
    while queue:
        # Pop from the queue
        current_node = queue.pop(0)

        # Print the current node
        print(current_node, end=" ")

        # For each node connected to current node
        for neighbor in graph[current_node]:

            # If neighbor is not visited
            if neighbor not in visited:

                # Add neighbor to visited
                visited.append(neighbor)

                # Add neighbor to the back of the queue
                queue.append(neighbor)


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Start BFS from node A
bfs(graph, 'A')