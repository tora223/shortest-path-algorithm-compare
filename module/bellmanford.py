def bellman_ford(G: list[tuple[int, int, int]], src: int) -> tuple[list[int], list[int]]:
    """__description__

    Args:
        G (list[tuple[int, int, int]]): (v, u, w)の形式のリスト
        src (int): 始点となるノードのインデックス

    Returns:
        tuple[list[int], list[int]}: (距離のリスト, 経路復元に使うリスト)
    """
    INF = 10**18
    dist = [INF]*len(G)
    dist[src] = 0
    prev = [-1]*len(G)
    
    while True:
        updated = False
        for i in range(len(G)):
            u, v, w = G[i]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break
    
    return dist, prev