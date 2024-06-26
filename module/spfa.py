from collections import deque
from collections import defaultdict


def spfa(G: list[list[tuple[int, int]]], src: int) -> tuple[list[int], list[int]]:
    """SPFAによる単一始点最短経路探索

    Args:
        G (list[list[tuple[int, int]]]): 隣接リスト表現のグラフ
        src (int): 始点となるノードのインデックス

    Returns:
        tuple[list[int], list[int]]: (距離のリスト, 経路復元に使うリスト)
    """
    INF = 10**18
    dist = [INF]*len(G)
    dist[src] = 0
    prev = [-1]*len(G)
    q = deque([src])
    in_queue = [False]*len(G)
    in_queue[src] = True
    while q:
        u = q.popleft()
        in_queue[u] = False
        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if not in_queue[v]:
                    q.append(v)
                    in_queue[v] = True
                    
    return dist, prev