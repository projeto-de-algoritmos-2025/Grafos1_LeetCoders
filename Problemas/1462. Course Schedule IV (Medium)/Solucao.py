from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        grafo = defaultdict(list)
        for a, b in prerequisites:
            grafo[a].append(b)
        
        alcancavel = [set() for _ in range(numCourses)]
        for u in range(numCourses):
            fila = deque([u])
            visitados = set([u])
            while fila:
                atual = fila.popleft()
                for vizinho in grafo[atual]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)
            alcancavel[u] = visitados
        
        resposta = []
        for u, v in queries:
            resposta.append(v in alcancavel[u])
            
        return resposta