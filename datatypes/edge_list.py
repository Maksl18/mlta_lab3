import heapq
from math import inf
import networkx as nx
from colorama import Fore
from matplotlib import pyplot as plt
from networkx import DiGraph

from datatypes.node import Node


class EdgeList:
    def __init__(self, list_type):
        self.edge_list = []
        self.node_list = []
        allowed_types = ["directed", "undirected"]
        if not list_type in allowed_types:
            raise TypeError("Invalid matrix type")
        self.list_type = list_type

    def add_node(self, node):
        self.node_list.append(node)

    def get_node(self, index):
        return self.node_list[index].data

    def check_edge(self, src, dest):
        for index, edge in enumerate(self.edge_list):
            if edge == [src, dest]:
                return index
        return -1

    def get_node_id(self, name):
        try:
            return self.node_list.index(Node(name))
        except ValueError:
            return -1

    def add_edge(self, src, dest, weight=0):
        if not (0 <= src < len(self.node_list)) or not (0 <= dest < len(self.node_list)):
            raise IndexError("Index is out of bounds")
        self.edge_list.append((src, dest, weight))
        if self.list_type == "undirected":
            self.edge_list.append((dest, src, weight))

    def del_edge(self, src, dest):
        index = self.check_edge(src, dest)
        if index != -1:
            self.edge_list.pop(index)

    def print(self):
        for edge in self.edge_list:
            print(f"{self.node_list[edge[0]].data} -> {self.node_list[edge[1]].data}, вага {edge[2]}")

    def deykstra(self, src):
        adj = self.to_adj_list()
        shortest = {}
        min_heap = [[0, src]]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap, [w1 + w2, n2])

        for i in range(len(self.node_list)):
            if i not in shortest:
                shortest[i] = -1
        return shortest

    def print_deykstra(self, src):
        deykstra = self.deykstra(src)
        for key, value in deykstra.items():
            print(f"від {self.get_node(src)} до {self.get_node(key)} – найменший шлях {value}")

    def floyd(self):
        v = len(self.node_list)
        distances = [[0 if i == j else inf for j in range(v)] for i in range(v)]

        for edge in self.edge_list:
            src, dest, weight = edge
            distances[src][dest] = weight

        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

        return distances

    def print_floyd(self):
        print(end="\t")
        for node in self.node_list:
            print(node.data, end="\t")
        print()
        distances = self.floyd()
        for i, row in enumerate(distances):
            print(f"{Fore.WHITE}{self.node_list[i].data}", end="\t")
            for element in row:
                if element is inf:
                    print(f"{Fore.RED}X", end="\t")
                else:
                    print(f"{Fore.WHITE}{element}", end="\t")
            print()

    def to_adj_list(self):
        adj = {number: [] for number in range(len(self.node_list))}
        for src, dest, weight in self.edge_list:
            adj[src].append((dest, weight))
        return adj
