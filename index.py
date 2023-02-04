#algorithm of Bell-man Ford to find the shortest path in graph

def court_chemin(gragh, depart):
    dist = {sommet : float('inf') for sommet in graph}
    dist[depart]=0
    for i in range(len(graph)-1):
        for sommet in graph :
            for voisin, poid in graph[sommet].items():
                if dist[sommet]+poid < dist[voisin]:
                    dist[voisin]=dist[sommet]+poid
    return dist