

import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self, vertices):
        self.parent_map = {v: v for v in vertices}
        self.rank_map = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent_map[vertex] != vertex:
            self.parent_map[vertex] = self.find(self.parent_map[vertex])
        return self.parent_map[vertex]

    def union(self, root1, root2):
        if self.rank_map[root1] > self.rank_map[root2]:
            self.parent_map[root2] = root1
        elif self.rank_map[root1] < self.rank_map[root2]:
            self.parent_map[root1] = root2
        else:
            self.parent_map[root1] = root2
            self.rank_map[root2] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))
    edges.sort(key=lambda e: e[2])

    vertices = set(v for e in edges for v in e[:2])
    union_find = UnionFind(vertices)

    min_spanning_tree = set()
    for edge in edges:
        u, v, weight = edge
        root1 = union_find.find(u)
        root2 = union_find.find(v)

        if root1 != root2:
            min_spanning_tree.add((u, v, weight))
            union_find.union(root1, root2)

    return min_spanning_tree

def visualize_graph_with_edges(graph, edges, title):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="skyblue", font_weight="bold", width=2, arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()

# Updated Sample Graphs
graph_1 = {
    'A': {'B': 2, 'C': 4, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'A': 3, 'B': 4, 'C': 2}
}

graph_2 = {
    'X': {'Y': 2, 'Z': 1, 'W': 3},
    'Y': {'X': 2, 'Z': 3, 'W': 1},
    'Z': {'X': 1, 'Y': 3, 'W': 2},
    'W': {'X': 3, 'Y': 1, 'Z': 2}
}

graph_3 = {
    'P': {'Q': 2, 'R': 3, 'S': 1},
    'Q': {'P': 2, 'R': 1, 'S': 4},
    'R': {'P': 3, 'Q': 1, 'S': 2},
    'S': {'P': 1, 'Q': 4, 'R': 2}
}

graph_4 = {
    'L': {'M': 2, 'N': 3, 'O': 1},
    'M': {'L': 2, 'N': 1, 'O': 4},
    'N': {'L': 3, 'M': 1, 'O': 2},
    'O': {'L': 1, 'M': 4, 'N': 2}
}

# Run Kruskal's algorithm on Updated Sample Graphs, print the resulting minimum spanning tree, and plot the graphs
min_spanning_tree_1 = kruskal(graph_1)
print("Minimum Spanning Tree - Sample Case 1:")
print(min_spanning_tree_1)
visualize_graph_with_edges(graph_1, [(u, v) for u, v, _ in min_spanning_tree_1], "Minimum Spanning Tree - Sample Case 1")

min_spanning_tree_2 = kruskal(graph_2)
print("\nMinimum Spanning Tree - Sample Case 2:")
print(min_spanning_tree_2)
visualize_graph_with_edges(graph_2, [(u, v) for u, v, _ in min_spanning_tree_2], "Minimum Spanning Tree - Sample Case 2")

min_spanning_tree_3 = kruskal(graph_3)
print("\nMinimum Spanning Tree - Sample Case 3:")
print(min_spanning_tree_3)
visualize_graph_with_edges(graph_3, [(u, v) for u, v, _ in min_spanning_tree_3], "Minimum Spanning Tree - Sample Case 3")

min_spanning_tree_4 = kruskal(graph_4)
print("\nMinimum Spanning Tree - Sample Case 4:")
print(min_spanning_tree_4)
visualize_graph_with_edges(graph_4, [(u, v) for u, v, _ in min_spanning_tree_4], "Minimum Spanning Tree - Sample Case 4")
