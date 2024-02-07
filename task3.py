import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Graph:
    def __init__(self, vertices):
        self.graph = nx.Graph()

    def add_edge(self, u, v, w):
        self.graph.add_edge(u, v, weight=w)

    def dijkstra(self, src):
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[src] = 0
        queue = [(0, src)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, data in self.graph[current_vertex].items():
                distance = data['weight']
                if distances[neighbor] > current_distance + distance:
                    distances[neighbor] = current_distance + distance
                    heapq.heappush(queue, (distances[neighbor], neighbor))

        return distances

g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

distances = g.dijkstra(0)  

print("Найкоротші відстані від вершини 0 до інших вершин:")
for vertex, distance in distances.items():
    print(f"Вершина {vertex} має найкоротшу відстань {distance}")


pos = nx.spring_layout(g.graph)
nx.draw(g.graph, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700, font_size=14)
edge_labels = nx.get_edge_attributes(g.graph, 'weight')
nx.draw_networkx_edge_labels(g.graph, pos, edge_labels=edge_labels, font_color='red')

plt.show()