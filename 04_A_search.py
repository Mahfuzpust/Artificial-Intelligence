import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def astar_search(initial_state, goal_state, successors_fn, heuristic_fn):
    # Initialize start node
    start_node = Node(initial_state, None, 0, heuristic_fn(initial_state))

    # Initialize priority queue and visited set
    queue = []
    visited = set()

    # Add start node to the queue
    heapq.heappush(queue, start_node)

    while queue:
        # Get node with lowest total cost
        current_node = heapq.heappop(queue)

        # Check if goal state reached
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        # Add current node to visited set
        visited.add(current_node.state)

        # Generate successor nodes
        successors = successors_fn(current_node.state)

        for successor_state, action_cost in successors:
            # Calculate cost from start to successor
            successor_cost = current_node.cost + action_cost

            # Calculate heuristic for successor
            successor_heuristic = heuristic_fn(successor_state)

            # Calculate total cost for successor
            successor_total_cost = successor_cost + successor_heuristic

            # Create successor node
            successor_node = Node(successor_state, current_node, successor_cost, successor_heuristic)

            # Check if successor node is already visited
            if successor_state in visited:
                continue

            # Check if successor node is already in the queue
            for node in queue:
                if node.state == successor_state and node.total_cost <= successor_total_cost:
                    break
            else:
                # Add successor node to the queue
                heapq.heappush(queue, successor_node)

    # No path found
    return []

# Example usage
# Define the initial state, goal state, successors function, and heuristic function
initial_state = 'S'
goal_state = 'G'

successors = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 5)],
    'C': [('G', 4), ('D', 3)],
    'D': [('G', 2)],
    'G': []
}

def successors_fn(state):
    return successors[state]

def heuristic_fn(state):
    # Heuristic function (Manhattan distance)
    heuristic_values = {'S': 5,'A': 3, 'B': 4, 'C': 2, 'D': 6,'G': 0}
    return heuristic_values[state]

# Run A* search algorithm
path = astar_search(initial_state, goal_state, successors_fn, heuristic_fn)

# Print the resulting path
if path:
    print("Path found:", path)
else:
    print("No path found.")
