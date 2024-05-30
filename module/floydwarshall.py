def floyd_warshall(G: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    """ワーシャルフロイド法による全対最短経路探索

    Args:
        G (list[list[int]]): 隣接行列表現のグラフ

    Returns:
        tuple[list[list[int]], list[list[int]]]: (距離のリスト, 経路復元に使うリスト)
    """
    nodes = len(G)
    INF = 10**18
    dist = [[INF]*nodes for _ in range(nodes)]
    prev = [[-1]*nodes for _ in range(nodes)]
    for i in range(nodes):
        for j in range(nodes):
            if i == j:
                dist[i][j] = 0
            elif G[i][j] > 0:
                dist[i][j] = G[i][j]
                prev[i][j] = i
    
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]
                    
    return dist, prev