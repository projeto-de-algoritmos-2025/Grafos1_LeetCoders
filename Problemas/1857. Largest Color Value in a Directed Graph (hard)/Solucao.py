from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        grafo = [[] for _ in range(n)]
        for no, vizinho in edges:
            grafo[no].append(vizinho)
        count = [[0] * 26 for _ in range(n)]
        visitado = [0] * n  
        max_count = 0
        tem_ciclo = False
        def dfs(no: int) -> bool:
            nonlocal max_count, tem_ciclo

            if visitado[no] == 1:
                tem_ciclo = True
                return False 
            if visitado[no] == 2:
                return True 

            visitado[no] = 1
            for vizinho in grafo[no]:
                if not dfs(vizinho):
                    return False
                for c in range(26):
                    count[no][c] = max(count[no][c], count[vizinho][c])

            color_index = ord(colors[no]) - ord('a')
            count[no][color_index] += 1
            max_count = max(max_count, count[no][color_index])
            visitado[no] = 2
            return True

        for i in range(n):
            if visitado[i] == 0:
                if not dfs(i):
                    return -1

        return max_count