
import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)

# Modified Sample Graphs
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
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="black", node_color="lightcoral", font_weight="bold", width=2)
    plt.title(title)
    plt.show()

# Run DFS on Modified Sample Graphs and Plot
print("Sample Case 1:")
dfs(graph_1, 'C')
plot_graph(graph_1, "Sample Case 1 - DFS")

print("\nSample Case 2:")
dfs(graph_2, 'W')
plot_graph(graph_2, "Sample Case 2 - DFS")

print("\nSample Case 3:")
dfs(graph_3, 'O')
plot_graph(graph_3, "Sample Case 3 - DFS")

print("\nSample Case 4:")
dfs(graph_4, 'L')
plot_graph(graph_4, "Sample Case 4 - DFS")
