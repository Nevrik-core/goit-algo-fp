import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree, pos, colors):
    plt.figure(figsize=(8, 5))
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток
    nx.draw(tree, pos, node_color=colors, with_labels=True, node_size=2500, labels=labels)
    plt.show()



# Функція для рекурсивного обходу в глибину
def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)
    
    for neighbor in graph.adj[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)

    return path

# Функція для рекурсивного обходу в ширину
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            for neighbor in graph.adj[vertex]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return path

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.left.left.left = Node(15)
root.left.left.right = Node(25)
root.right = Node(1)
root.right.left = Node(3)

# Створюємо граф дерева
tree = nx.DiGraph()
pos = {root.id: (0, 0)}
add_edges(tree, root, pos)

# Функція для зміни кольору вузлів під час обходу
def color_nodes(path, start_color, end_color):
    colors = {}

    n = len(path)

    for i, node_id in enumerate(path):
        r = int(start_color[0] + i * (end_color[0] - start_color[0]) / (n - 1))
        g = int(start_color[1] + i * (end_color[1] - start_color[1]) / (n - 1))
        b = int(start_color[2] + i * (end_color[2] - start_color[2]) / (n - 1))
        color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        colors[node_id] = color
    return colors



# Початкові і кінцеві кольори для DFS і BFS
dfs_start_color = (255, 200, 200)  # світло-червоний
dfs_end_color = (255, 0, 0)  # темно-червоний
bfs_start_color = (200, 200, 255)  # світло-синій
bfs_end_color = (0, 0, 255)  # темно-синій


# Обхід дерева в глибину (DFS)
dfs_path = dfs(tree, root.id)
dfs_colors = color_nodes(dfs_path, dfs_start_color, dfs_end_color)


# Обхід дерева в ширину (BFS)
bfs_path = bfs(tree, root.id)
bfs_colors = color_nodes(bfs_path, bfs_start_color, bfs_end_color)

# Функція для візуалізації обходів
def visualize_traversal(tree, pos, dfs_colors, bfs_colors):
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    axs[0].set_title('DFS Обхід в глибину')
    nx.draw(tree, pos, node_color=[dfs_colors[node] for node in tree.nodes], node_size=2000, with_labels=True, labels=nx.get_node_attributes(tree, 'label'), ax=axs[0])

    axs[1].set_title('BFS Обхід в ширину')
    nx.draw(tree, pos, node_color=[bfs_colors[node] for node in tree.nodes], node_size=2000, with_labels=True, labels=nx.get_node_attributes(tree, 'label'), ax=axs[1])

    plt.show()


visualize_traversal(tree, pos, dfs_colors, bfs_colors)
