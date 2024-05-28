import heapq

def dijkstra(G: list[list[tuple[int, int] | int]], src: int, PQ: bool = True) -> tuple[list[int], list[int]]:
    """__description__

    Args:
        G (list[list[tuple[int, int] | int]]): 隣接リスト表現のグラフ(重み付き) or 隣接行列
        src (int): 始点となるノードのインデックス
        PQ (bool optional): 優先度付きキューを使うかどうか

    Returns:
        tuple[list[int], list[int]}: (距離のリスト, 経路復元に使うリスト)
    """
    INF = 10**18
    visited = [False]*len(G)
    dist = [INF]*len(G)
    dist[src] = 0
    prev = [-1]*len(G)
    
    if PQ:
        pq = [(0, src)]
        heapq.heapify(pq)

        while pq:
            _, u = heapq.heappop(pq)
            if visited[u]:
                continue
            
            visited[u] = True

            for v, weight in G[u]:
                new_dist = weight + dist[u]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))
    
    else:
        while True:
            u = -1
            min_dist = INF
            for i in range(len(G)):
                if not visited[i] and dist[i] < min_dist:
                    u = i
                    min_dist = dist[i]
            
            if u == -1:
                break
            visited[u] = True
            
            for i in range(len(G)):
                if G[u][i] > 0:
                    w = G[u][i]
                    if dist[u] + w < dist[i]:
                        dist[i] = dist[u] + w
                        prev[i] = u
                        
    return dist, prev