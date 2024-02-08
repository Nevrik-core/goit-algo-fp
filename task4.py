import networkx as nx
import matplotlib.pyplot as plt
import uuid

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def heapify(arr, n, i, node_list):
    smallest = i 
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[smallest] > arr[left]:
        smallest = left

    if right < n and arr[smallest] > arr[right]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest, node_list)

def build_heap(arr):
    n = len(arr)
    node_list = [None] * n
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, node_list)
    for i in range(n):
        node_list[i] = Node(arr[i])
        if i != 0:
            parent_index = (i - 1) // 2
            if i % 2 == 1:
                node_list[parent_index].left = node_list[i]
            else:
                node_list[parent_index].right = node_list[i]
    return node_list[0] 

# Допоміжна функція для додавання ребер
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для візуалізації бінарної купи
def visualize_heap(heap_array):
    heap_root = build_heap(heap_array)  
    draw_tree(heap_root) 

heap_array = [0, 4, 1, 5, 2, 10, 3, 17, 35, 6, 22, 7]
visualize_heap(heap_array)
