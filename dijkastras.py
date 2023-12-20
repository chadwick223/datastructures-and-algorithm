import networkx as nx
import matplotlib.pyplot as plt

class DirectedGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Use DiGraph for directed edges

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def initialize_distances_and_previous(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    return distances, previous_nodes

def get_unvisited_nodes(graph):
    return set(graph.nodes)

def relax_edges(graph, current_node, distances, previous_nodes):
    for neighbor, edge_data in graph[current_node].items():
        distance_to_neighbor = distances[current_node] + edge_data['weight']
        if distance_to_neighbor < distances[neighbor]:
            distances[neighbor] = distance_to_neighbor
            previous_nodes[neighbor] = current_node

def dijkstra_shortest_paths(graph, start):
    distances, previous_nodes = initialize_distances_and_previous(graph, start)
    unvisited_nodes = get_unvisited_nodes(graph)

    while True:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)
        relax_edges(graph, current_node, distances, previous_nodes)

        if not unvisited_nodes:
            break

    return distances, previous_nodes

def visualize_directed_graph(graph):
    pos = nx.spring_layout(graph.graph)  # positions for all nodes
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Directed Graph Visualization")
    plt.show()

def run_test_case(graph, start_node):
    visualize_directed_graph(graph)
    shortest_distances, previous_nodes = dijkstra_shortest_paths(graph.graph, start_node)
    print(f"Shortest Distances from {start_node}: {shortest_distances}")
    print(f"Previous Nodes: {previous_nodes}")
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
run_test_case(graph1, "A")

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
run_test_case(graph2, "A")

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
run_test_case(graph3, "A")
