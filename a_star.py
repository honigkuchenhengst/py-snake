#Quelle für Basis: https://www.youtube.com/watch?app=desktop&v=qWbqHKzVLIw

import heapq

class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic
        self.parent = None

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(graph, start, goal):
    open_set = []
    closed_set = set()

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            # Path found, reconstruct and return it
            path = []
            while current_node:
                path.insert(0, current_node.position)
                current_node = current_node.parent
            return path

        closed_set.add(current_node.position)

        for neighbor in graph[current_node.position]:
            if neighbor not in closed_set:
                cost = current_node.cost + graph[current_node.position][neighbor]
                heuristic_val = heuristic(neighbor, goal)
                new_node = Node(neighbor, cost, heuristic_val)
                new_node.parent = current_node

                existing_node = next((node for node in open_set if node.position == neighbor), None)
                if existing_node and existing_node.cost <= cost:
                    continue

                heapq.heappush(open_set, new_node)

    return None  # No path found

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def create_grid(width, depth, blocked_nodes):
    graph = {}
    for i in range(width):
        for j in range(depth):
            if (i, j) not in blocked_nodes:
                neighbors = {}
                if i > 0 and (i - 1, j) not in blocked_nodes:
                    neighbors[(i - 1, j)] = 1
                if j > 0 and (i, j - 1) not in blocked_nodes:
                    neighbors[(i, j - 1)] = 1
                if i < width - 1 and (i + 1, j) not in blocked_nodes:
                    neighbors[(i + 1, j)] = 1
                if j < depth - 1 and (i, j + 1) not in blocked_nodes:
                    neighbors[(i, j + 1)] = 1
                graph[(i, j)] = neighbors
    return graph

# Create the graph with a 5x5 grid and specified blocked nodes
width = 5
depth = 5
blocked_nodes = {(0, 4), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (4, 0)}
graph = create_grid(width, depth, blocked_nodes)

# Example usage with the created graph
start_node = (0, 0)
goal_node = (4, 3)

path = astar_search(graph, start_node, goal_node)

if path:
    print("Path found:", path)
else:
    print("No path found")