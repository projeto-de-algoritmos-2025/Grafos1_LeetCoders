from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        grafo = defaultdict(list)
        for a, b in connections:                #Grafo não direcionado
            grafo[a].append(b)
            grafo[b].append(a)
        
        nivel = [-1]*n  
        menor_nivel = [-1]*n     
        conex_critica = []
        
        def DFS(no_atual, no_pai, profundidade):
            nivel[no_atual] = profundidade
            menor_nivel[no_atual] = profundidade
            
            for vizinho in grafo[no_atual]:
                if vizinho == no_pai:
                    continue
                
                if nivel[vizinho] == -1:            #Vizinho não visitado
                    DFS(vizinho, no_atual, profundidade + 1)
                    menor_nivel[no_atual] = min(menor_nivel[no_atual], menor_nivel[vizinho])
                    
                    if menor_nivel[vizinho] > nivel[no_atual]:
                        conex_critica.append([no_atual, vizinho])

                else:
                    menor_nivel[no_atual] = min(menor_nivel[no_atual], nivel[vizinho])
        
        DFS(0, -1, 0) 

        return conex_critica

solucao = Solution()
print(solucao.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))  # Saída: [[1, 3]]