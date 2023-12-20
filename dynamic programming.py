import networkx as nx
import matplotlib.pyplot as plt

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

    def visualize_directed_graph(self):
        pos = nx.spring_layout(self.graph)  # positions for all nodes
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Directed Graph Visualization")
        plt.show()

    def bellman_ford(self, source):
        vertices = len(self.graph)
        distances = [float('inf')] * vertices
        distances[source] = 0

        for iteration in range(vertices - 1):
            for edge in self.graph.edges(data=True):
                u, v, weight = edge
                # Relax the edge
                if distances[u] + weight['weight'] < distances[v]:
                    distances[v] = distances[u] + weight['weight']

        # Check for negative cycles
        for edge in self.graph.edges(data=True):
            u, v, weight = edge
            if distances[u] + weight['weight'] < distances[v]:
                print("Graph contains a negative cycle")
                return None

        return distances

def run_test_case(graph, source_vertex):
    graph.visualize_directed_graph()
    shortest_distances = graph.bellman_ford(source_vertex)

    if shortest_distances is not None:
        print(f"Shortest distances from vertex {source_vertex}:")
        for i, distance in enumerate(shortest_distances):
            print(f"To vertex {i}: {distance}")

# Test Case 1
graph1 = DirectedGraph()
graph1.add_node("A")
graph1.add_node("B")
graph1.add_node("C")
graph1.add_edge("A", "B", 1)
graph1.add_edge("B", "C", 3)
graph1.add_edge("A", "C", 2)
print("Test Case 1:")
run_test_case(graph1, source_vertex=0)

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
run_test_case(graph2, source_vertex=0)

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
run_test_case(graph3, source_vertex=0)
