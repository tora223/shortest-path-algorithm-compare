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
    
    import time

    info = time.get_clock_info('perf_counter')
    print(f"Resolution: {info.resolution} seconds")
    
    print(f"Nodes: {data.nodes}, Edges: {data.edges}")

    # 単一始点最短経路
    print("単一始点最短経路")
    # bfs
    start = time.perf_counter()
    G = data.get_graph_list()
    bfs(G, 0)
    end = time.perf_counter()
    print(f"幅優先探索: {end-start} sec")
    
    # dijkstra (二分ヒープ)
    start = time.perf_counter()
    G = data.get_graph_with_weight()
    dijkstra(G, 0)
    end = time.perf_counter()
    print(f"ダイクストラ (二分ヒープ): {end-start} sec")
    
    # dijkstra (隣接行列)
    start = time.perf_counter()
    G = data.get_graph_matrix()
    dijkstra(G, 0, PQ=False)
    end = time.perf_counter()
    print(f"ダイクストラ (隣接行列): {end-start} sec")
    
    # bellman-ford
    start = time.perf_counter()
    G = data.get_graph_bellman_ford()
    bellman_ford(G, 0)
    end = time.perf_counter()
    print(f"ベルマンフォード: {end-start} sec")
    
    # spfa
    start = time.perf_counter()
    G = data.get_graph_with_weight()
    spfa(G, 0)
    end = time.perf_counter()
    print(f"spfa: {end-start} sec")
    
    # 全対最短経路
    print("全対最短経路")
    
    # ワーシャルフロイド法
    start = time.perf_counter()
    G = data.get_graph_matrix()
    floyd_warshall(G)
    end = time.perf_counter()
    print(f"ワーシャルフロイド法: {end-start} sec")
    
    # 全点ダイクストラ(二分ヒープ)
    start = time.perf_counter()
    G = data.get_graph_with_weight()
    for i in range(data.nodes):
        dijkstra(G, i)
    end = time.perf_counter()
    print(f"全点ダイクストラ(二分ヒープ): {end-start} sec")
    
    # 全点ダイクストラ(隣接行列)
    start = time.perf_counter()
    G = data.get_graph_matrix()
    for i in range(data.nodes):
        dijkstra(G, i, PQ=False)
    end = time.perf_counter()
    print(f"全点ダイクストラ(隣接行列): {end-start} sec")
    
    # 全点spfa
    start = time.perf_counter()
    G = data.get_graph_with_weight()
    for i in range(data.nodes):
        spfa(G, i)
    end = time.perf_counter()
    print(f"全点spfa: {end-start} sec")
    
    # 全点ベルマンフォード
    start = time.perf_counter()
    G = data.get_graph_bellman_ford()
    for i in range(data.nodes):
        bellman_ford(G, i)
    end = time.perf_counter()
    print(f"全点ベルマンフォード: {end-start} sec")
    

if __name__ == "__main__":
    main()