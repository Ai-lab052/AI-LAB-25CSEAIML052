# Function to perform BFS search for a target node
def bfs_search(graph, start, target):

    # STEP 1: Create an empty list to store visited nodes
    visited = []

    # STEP 2: Create an empty queue
    queue = []

    # STEP 3: Add the start node to the queue
    queue.append(start)

    # STEP 4: Mark the start node as visited
    visited.append(start)

    # STEP 4.1: Continue until the queue becomes empty
    while queue:

        # STEP 4.1.1: Remove the first node from the queue
        current = queue.pop(0)

        # STEP 4.1.2: Print the current node
        print(current, end=" ")

        # Check if the current node is the target node
        if current == target:
            print("\nTarget found")
            return

        # STEP 4.2: Get all neighbors of the current node
        # get(current, []) returns an empty list if the node has no neighbors
        for neighbor in graph.get(current, []):

            # STEP 4.2.1: Check if the neighbor has not been visited
            if neighbor not in visited:

                # STEP 4.2.2: Mark the neighbor as visited
                visited.append(neighbor)

                # STEP 4.2.3: Add the neighbor to the back of the queue
                queue.append(neighbor)

    # STEP 5: If queue becomes empty without finding the target
    print("\nTarget not found")


# Create an empty graph
graph = {}

# Add nodes and their neighbors as per our need
graph['A'] = ['B', 'C']    # B and C are neighbors of A
graph['B'] = ['D', 'E']    # D and E are neighbors of B
graph['C'] = ['F']         # F is a neighbor of C

# Start BFS from node A and search for target node E
bfs_search(graph, 'A', 'E')