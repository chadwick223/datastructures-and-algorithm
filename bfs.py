import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for next_node in graph[current_node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)

# Sample Graphs
graph_1 = {
    'X': ['Y', 'Z', 'W'],
    'Y': ['X', 'A'],
    'Z': ['X', 'B', 'C'],
    'W': ['X', 'D', 'E'],
    'A': ['Y', 'F'],
    'B': ['Z', 'G'],
    'C': ['Z', 'H'],
    'D': ['W'],
    'E': ['W'],
    'F': ['A'],
    'G': ['B'],
    'H': ['C']
}

graph_2 = {
    'P': ['Q', 'R', 'S'],
    'Q': ['P', 'T'],
    'R': ['P', 'U', 'V'],
    'S': ['P', 'W'],
    'T': ['Q'],
    'U': ['R'],
    'V': ['R'],
    'W': ['S', 'X'],
    'X': ['W']
}

graph_3 = {
    'M': ['N', 'O'],
    'N': ['O'],
    'O': []
}

graph_4 = {
    'I': ['J', 'K', 'L'],
    'J': ['I', 'M'],
    'K': ['I', 'N', 'O'],
    'L': ['I', 'P'],
    'M': ['J'],
    'N': ['K'],
    'O': ['K'],
    'P': ['L']
}

def plot_graph(graph, title):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="black", node_color="skyblue", font_weight="bold", width=2)
    plt.title(title)
    plt.show()

# Run BFS on Modified Sample Graphs and Plot
print("Sample Case 1:")
bfs(graph_1, 'X')
plot_graph(graph_1, "Sample Case 1 - BFS")

print("\nSample Case 2:")
bfs(graph_2, 'P')
plot_graph(graph_2, "Sample Case 2 - BFS")

print("\nSample Case 3:")
bfs(graph_3, 'M')
plot_graph(graph_3, "Sample Case 3 - BFS")

print("\nSample Case 4:")
bfs(graph_4, 'I')
plot_graph(graph_4, "Sample Case 4 - BFS")
