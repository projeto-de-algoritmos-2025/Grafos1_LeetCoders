class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visitados = {}
        fila = deque([node])

        visitados[node] = Node(node.val)

        while fila:
            atual = fila.popleft()

            for vizinho in atual.neighbors:
                if vizinho not in visitados:
                    visitados[vizinho] = Node(vizinho.val)
                    fila.append(vizinho)

                visitados[atual].neighbors.append(visitados[vizinho])

        return visitados[node]
