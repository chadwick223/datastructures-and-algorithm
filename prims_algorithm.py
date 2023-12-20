#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import heapq

def custom_prim(graph, start):
    result_tree = set()
    visited_nodes = {start}
    priority_queue = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(priority_queue, (weight, start, neighbor))

    while visited_nodes != set(graph.keys()):
        weight, current_node, next_node = heapq.heappop(priority_queue)
        if next_node not in visited_nodes:
            result_tree.add((current_node, next_node))
            visited_nodes.add(next_node)
            for neighbor, edge_weight in graph[next_node].items():
                if neighbor not in visited_nodes:
                    heapq.heappush(priority_queue, (edge_weight, next_node, neighbor))

    return result_tree

def plot_graph_with_edges_custom(graph, edges, title):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="black", node_color="lightgreen", font_weight="bold", width=2)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()

graph_custom_1 = {
    'A': {'B': 2, 'C': 4, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'A': 3, 'B': 4, 'C': 2}
}

graph_custom_2 = {
    '1': {'2': 1, '3': 2},
    '2': {'1': 1, '3': 3},
    '3': {'1': 2, '2': 3}
}

graph_custom_3 = {
    'X': {'Y': 2, 'Z': 1, 'W': 3},
    'Y': {'X': 2, 'Z': 3, 'W': 1},
    'Z': {'X': 1, 'Y': 3, 'W': 2},
    'W': {'X': 3, 'Y': 1, 'Z': 2}
}

graph_custom_4 = {
    'M': {'N': 2, 'O': 3, 'P': 1},
    'N': {'M': 2, 'O': 1, 'P': 4},
    'O': {'M': 3, 'N': 1, 'P': 2},
    'P': {'M': 1, 'N': 4, 'O': 2}
}

graph_custom_5 = {
    'P': {'Q': 2, 'R': 3},
    'Q': {'P': 2, 'R': 1, 'S': 4},
    'R': {'P': 3, 'Q': 1, 'S': 2},
    'S': {'Q': 4, 'R': 2}
}

graph_custom_6 = {
    'X': {'Y': 1, 'Z': 2},
    'Y': {'X': 1, 'Z': 3},
    'Z': {'X': 2, 'Y': 3}
}

print("AS ARROWS ARE NOT HIGHLIGHTED IN THE PLOT, CHECK KERNEL FOR THE TRAVELLING OF THE SHORTEST PATH DISTANCE.")
# Run
start_node_custom_1 = list(graph_custom_1.keys())[0]
min_spanning_tree_custom_1 = custom_prim(graph_custom_1, start_node_custom_1)
print("Minimum Spanning Tree (Custom Prim) - Sample Case 1:")
print(min_spanning_tree_custom_1)
plot_graph_with_edges_custom(graph_custom_1, min_spanning_tree_custom_1, "Minimum Spanning Tree (Custom Prim) - Sample Case 1")

start_node_custom_2 = list(graph_custom_2.keys())[0]
min_spanning_tree_custom_2 = custom_prim(graph_custom_2, start_node_custom_2)
print("\nMinimum Spanning Tree (Custom Prim) - Sample Case 2:")
print(min_spanning_tree_custom_2)
plot_graph_with_edges_custom(graph_custom_2, min_spanning_tree_custom_2, "Minimum Spanning Tree (Custom Prim) - Sample Case 2")

start_node_custom_3 = list(graph_custom_3.keys())[0]
min_spanning_tree_custom_3 = custom_prim(graph_custom_3, start_node_custom_3)
print("\nMinimum Spanning Tree (Custom Prim) - Sample Case 3:")
print(min_spanning_tree_custom_3)
plot_graph_with_edges_custom(graph_custom_3, min_spanning_tree_custom_3, "Minimum Spanning Tree (Custom Prim) - Sample Case 3")

start_node_custom_4 = list(graph_custom_4.keys())[0]
min_spanning_tree_custom_4 = custom_prim(graph_custom_4, start_node_custom_4)
print("\nMinimum Spanning Tree (Custom Prim) - Sample Case 4:")
print(min_spanning_tree_custom_4)
plot_graph_with_edges_custom(graph_custom_4, min_spanning_tree_custom_4, "Minimum Spanning Tree (Custom Prim) - Sample Case 4")


start_node_custom_5 = list(graph_custom_5.keys())[0]
min_spanning_tree_custom_5 = custom_prim(graph_custom_5, start_node_custom_5)
print("\nMinimum Spanning Tree (Custom Prim) - Additional Case 5:")
print(min_spanning_tree_custom_5)
plot_graph_with_edges_custom(graph_custom_5, min_spanning_tree_custom_5, "Minimum Spanning Tree (Custom Prim) - Additional Case 5")

start_node_custom_6 = list(graph_custom_6.keys())[0]
min_spanning_tree_custom_6 = custom_prim(graph_custom_6, start_node_custom_6)
print("\nMinimum Spanning Tree (Custom Prim) - Additional Case 6:")
print(min_spanning_tree_custom_6)
plot_graph_with_edges_custom(graph_custom_6, min_spanning_tree_custom_6, "Minimum Spanning Tree (Custom Prim) - Additional Case 6")
