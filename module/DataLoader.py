import csv
import pandas as pd


class DataLoader:
    def __init__(self, filepath: str):
        self._filepath = filepath
        
        data = []
        max_id = 0
        min_id = 10**18
        with open(self._filepath, "r") as file:
            reader = csv.reader(file, delimiter=" ")
            next(reader)
            for row in reader:
                a = int(row[0])
                b = int(row[1])
                data.append((a, b))
                max_id = max(max_id, a, b)
                min_id = min(min_id, a, b)
                
        self._max_id = max_id    
        self._min_id = min_id
        self._data = data
        self.edges = len(data)
        self.nodes = (max_id - min_id + 1) if not min_id == max_id else 0


    def get_graph_list(self) -> list[list[int]]:
        G = [[] for _ in range(self._max_id + 1)]
        for a, b in self._data:
            G[a].append(b)
        
        return G
    
    
    def get_graph_with_weight(self) -> list[list[tuple[int, int]]]:
        G = [[] for _ in range(self._max_id + 1)]
        for a, b in self._data:
            G[a].append((b, 1))
        
        return G
    
    
    def get_graph_bellman_ford(self) -> list[tuple[int, int, int]]:
        G = []
        for a, b in self._data:
            G.append((a, b, 1))
        
        return G
    
    
    def get_graph_matrix(self) -> list[list[int]]:
        G = [[0]*(self._max_id + 1) for _ in range(self._max_id + 1)]
        for a, b in self._data:
            G[a][b] = 1
        
        return G