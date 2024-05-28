from collections import deque
from collections import defaultdict


def spfa(G: list[list[tuple[int, int]]], src: int) -> tuple[list[int], list[int]]:
    """__description__

    Args:
        G (list[list[tuple[int, int]]]): 隣接リスト表現のグラフ
        src (int): 始点となるノードのインデックス

    Returns:
        list[int]: 距離のリスト
        list[int]: 経路復元に使うリスト
    """
    INF = 10**18
    dist = [INF]*len(G)
    dist[src] = 0
    prev = [-1]*len(G)
    q = deque([src])
    d = defaultdict(bool)
    d[src] = 1
    while q:
        u = q.popleft()
        d[u] = False
        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if not d[v]:
                    q.append(v)
                    d[v] = True
                    
    return dist, prev