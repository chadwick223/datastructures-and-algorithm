import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class DirectedGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Use DiGraph for directed edges
        self.node_indices = {}

    def add_node(self, value):
        node_index = len(self.node_indices)
        self.node_indices[value] = node_index
        self.graph.add_node(node_index)

    def add_edge(self, from_node, to_node, weight):
        from_index = self.node_indices[from_node]
        to_index = self.node_indices[to_node]
        self.graph.add_edge(from_index, to_index, weight=weight)

    def floyd_warshall(self):
        n = len(self.graph)
        distance_matrix = np.full((n, n), np.inf)

        for i in range(n):
            distance_matrix[i, i] = 0

        for edge in self.graph.edges(data=True):
            from_node, to_node, weight = edge
            distance_matrix[from_node][to_node] = weight['weight']

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance_matrix[i, k] + distance_matrix[k, j] < distance_matrix[i, j]:
                        distance_matrix[i, j] = distance_matrix[i, k] + distance_matrix[k, j]

        return distance_matrix.tolist()

def visualize_directed_graph(graph):
    pos = nx.spring_layout(graph.graph)  # positions for all nodes
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Directed Graph Visualization")
    plt.show()

def run_test_case(graph):
    visualize_directed_graph(graph)
    shortest_paths = graph.floyd_warshall()
    print("Shortest Paths:")
    for row in shortest_paths:
        print(row)
    print()

# Test Case 1
graph1 = DirectedGraph()
graph1.add_node("A")
graph1.add_node("B")
graph1.add_node("C")
graph1.add_edge("A", "B", 1)
graph1.add_edge("B", "C", 3)
graph1.add_edge("A", "C", 2)
print("Test Case 1:")
run_test_case(graph1)

# Test Case 2
graph2 = DirectedGraph()
graph2.add_node("A")
graph2.add_node("B")
graph2.add_node("C")
graph2.add_node("D")
graph2.add_edge("A", "B", 2)
graph2.add_edge("B", "C", 4)
graph2.add_edge("C", "D", 3)
graph2.add_edge("A", "C", 1)
graph2.add_edge("B", "D", 5)
print("Test Case 2:")
run_test_case(graph2)

# Test Case 3
graph3 = DirectedGraph()
graph3.add_node("A")
graph3.add_node("B")
graph3.add_node("C")
graph3.add_node("D")
graph3.add_edge("A", "B", 2)
graph3.add_edge("B", "C", 1)
graph3.add_edge("C", "D", 4)
graph3.add_edge("A", "C", 3)
graph3.add_edge("B", "D", 3)
print("Test Case 3:")
run_test_case(graph3)
