import time
from module.DataLoader import DataLoader
from module.bfs import bfs
from module.dijkstra import dijkstra
from module.bellmanford import bellman_ford
from module.spfa import spfa
from module.floydwarshall import floyd_warshall


def main():
    file = "data/0.edges"
    data = DataLoader(file)

    info = time.get_clock_info('perf_counter')
    print(f"Resolution: {info.resolution} seconds")
    
    print(f"Nodes: {data.nodes}, Edges: {data.edges}")
    

    # 単一始点最短経路
    print("単一始点最短経路")
    
    # bfs
    G = data.get_graph_list()
    start = time.perf_counter()
    bfs(G, 0)
    end = time.perf_counter()
    time_sec = end-start
    print(f"幅優先探索: {time_sec:0.7f} sec")
    
    # dijkstra (二分ヒープ)
    G = data.get_graph_with_weight()
    start = time.perf_counter()
    dijkstra(G, 0)
    end = time.perf_counter()
    time_sec = end-start
    print(f"ダイクストラ (二分ヒープ): {time_sec:0.7f} sec")
    
    # dijkstra (隣接行列)
    G = data.get_graph_matrix()
    start = time.perf_counter()
    dijkstra(G, 0, PQ=False)
    end = time.perf_counter()
    time_sec = end-start
    print(f"ダイクストラ (隣接行列): {time_sec:0.7f} sec")
    
    # bellman-ford
    G = data.get_graph_bellman_ford()
    start = time.perf_counter()
    bellman_ford(G, 0)
    end = time.perf_counter()
    time_sec = end-start
    print(f"ベルマンフォード: {time_sec:0.7f} sec")
    
    # spfa
    G = data.get_graph_with_weight()
    start = time.perf_counter()
    spfa(G, 0)
    end = time.perf_counter()
    time_sec = end-start
    print(f"spfa: {time_sec:0.7f} sec")
    
    # 全点対最短経路
    print("全点対最短経路")
    
    # ワーシャルフロイド法
    G = data.get_graph_matrix()
    start = time.perf_counter()
    floyd_warshall(G)
    end = time.perf_counter()
    time_sec = end-start
    print(f"ワーシャルフロイド法: {time_sec:0.7f} sec")
    
    # 全点ダイクストラ(二分ヒープ)
    G = data.get_graph_with_weight()
    start = time.perf_counter()
    for i in range(data.nodes):
        dijkstra(G, i)
    end = time.perf_counter()
    time_sec = end-start
    print(f"ダイクストラ(二分ヒープ): {time_sec:0.7f} sec")
    
    # 全点ダイクストラ(隣接行列)
    G = data.get_graph_matrix()
    start = time.perf_counter()
    for i in range(data.nodes):
        dijkstra(G, i, PQ=False)
    end = time.perf_counter()
    time_sec = end-start
    print(f"ダイクストラ(隣接行列): {time_sec:0.7f} sec")
    
    # 全点ベルマンフォード
    G = data.get_graph_bellman_ford()
    start = time.perf_counter()
    for i in range(data.nodes):
        bellman_ford(G, i)
    end = time.perf_counter()
    time_sec = end-start
    print(f"ベルマンフォード: {time_sec:0.7f} sec")
    
    # 全点spfa
    G = data.get_graph_with_weight()
    start = time.perf_counter()
    for i in range(data.nodes):
        spfa(G, i)
    end = time.perf_counter()
    time_sec = end-start
    print(f"spfa: {time_sec:0.7f} sec")
    

if __name__ == "__main__":
    main()