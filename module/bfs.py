from collections import deque


def bfs(G: list[list[int]], src: int) -> tuple[list[int], list[int]]:
    """幅優先探索による単一始点最短経路探索

    Args:
        G (list[list[int]]): 隣接リスト表現のグラフ
        src (int): 始点となるノードのインデックス

    Returns:
        tuple[list[int], list[int]]: (距離のリスト, 経路復元に使うリスト)
    """
    q = deque([src])
    dist = [-1] * len(G)
    dist[src] = 0
    prev = [-1] * len(G)
    
    while q:
        v = q.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                prev[u] = v
                q.append(u)
                
    return dist, prev