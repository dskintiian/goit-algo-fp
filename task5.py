import uuid
import webcolors
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from random import sample
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs_iterative(start):
    colors_queue = deque(['#FFFFFF', '#CCFFEE', '#99FFCC', '#66FFAA', '#33FF99', '#00FF77', '#00CC66', '#009955', '#006633'])
    visited = set()
    start.color = colors_queue.pop()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            left, right = vertex.left, vertex.right
            shift_color = colors_queue.pop()
            if left:
                left.color = shift_color
                queue.extend([left])
            if right:
                right.color = shift_color
                queue.extend([right])


def dfs_iterative(start_vertex):
    colors_queue = deque(['#FFFFFF', '#CCFFEE', '#99FFCC', '#66FFAA', '#33FF99', '#00FF77', '#00CC66', '#009955', '#006633'])
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        vertex.color = colors_queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            left, right = vertex.left, vertex.right
            if left:
                stack.extend([left])
            if right:
                stack.extend([right])


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.left.left = Node(78)
root.left.right = Node(10)
root.left.right.right = Node(27)
root.right = Node(1)
root.right.left = Node(3)

dfs_iterative(root)
# bfs_iterative(root)
draw_tree(root)
