# Function to perform BFS search for a target node
def bfs_search(graph, start, target):
    # STEP 1: Create an empty visited list
    visited = []

    # STEP 2: Create an empty queue
    queue = []

    # STEP 3: Add the start node to the queue
    queue.append(start)

    # STEP 4: Mark the start node as visited
    visited.append(start)

    # Continue until the queue becomes empty
    while queue:
        # Remove the first node from the queue
        current = queue.pop(0)

        # Print the current node
        print(current, end=" ")

        # Check if the target node is found
        if current == target:
            print("\nTarget found")
            return

        # Get all neighbors of the current node
        for neighbor in graph.get(current, []):
            # If neighbor is not visited
            if neighbor not in visited:
                # Mark neighbor as visited
                visited.append(neighbor)

                # Add neighbor to the queue
                queue.append(neighbor)

    # Queue is empty and target was not found
    print("\nTarget not found")


# Create an empty graph
graph = {}

# Take the number of edges from the user
n = int(input("Enter the number of edges: "))

# Take each edge as input
for i in range(n):
    u, v = input(f"Enter edge {i+1}: ").split()

    # Add v as a neighbor of u
    graph.setdefault(u, []).append(v)


# Take start and target nodes from the user
start = input("Enter the start node: ")
target = input("Enter the target node: ")

# Perform BFS search
bfs_search(graph, start, target)