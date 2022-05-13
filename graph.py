from functools import reduce
import random
from itertools import permutations


class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.verteces = []
        for a,b in self.graph.keys():
            if a not in self.verteces:
                self.verteces.append(a)
            if b not in self.verteces:
                self.verteces.append(b)
        pass
    def __getitem__(self, item):
        if item in self.graph.keys():
            return self.graph[item]
        elif (item[1],item[0]) in self.graph.keys():
            return self.graph[(item[1],item[0])]

    def __contains__(self, item):
        if item in self.graph.keys():
            return True
        elif (item[1],item[0]) in self.graph.keys():
            return True
        else:
            return False

    def keys(self):
        return self.graph.keys()

    def shortest_path_table(self,start):
        node=start
        unvisited = self.verteces.copy()
        visited = []
        if node not in unvisited:
            raise ValueError(f'node "{node}" does not exists')
        else:
            map_table = {i:(0 if i==node else float('inf'),None) for i in unvisited}
            while unvisited:
                visited.append(node)

                unvisited.remove(node)
                neighbours = list(filter(lambda a: True if (node,a) in self.keys() \
                                        or (a,node) in self.keys() else False,unvisited))
                for n in neighbours:
                    new_distance = map_table[node][0]+self[(node,n)]
                    distance = map_table[n][0]
                    if new_distance<distance:
                        map_table[n] = (new_distance,node)
                if unvisited:
                    srt_pth_n = unvisited[0]
                    for VTX in unvisited:
                        if map_table[VTX][0]<map_table[srt_pth_n][0]:
                            srt_pth_n=VTX
                    node = srt_pth_n


            return map_table

    def show_shortest_path_table(self,node):
        table = self.shortest_path_table(node)
        ft_st = "Node\tshortest distance\tprevious node\n\n"
        print(ft_st)
        for key in table:
            print(f"{key.center(4,' ')}\t{str(table[key][0]).center(17,' ')}\t{table[key][1]}\n")

    def show_shortest_path(self,a,b):
        cur = b
        path=f"-->{b}"
        s_path_table = self.shortest_path_table('a')
        while cur!=a:
            path = "-->"+str(s_path_table[cur][1])+path
            cur = s_path_table[cur][1]
        print("*"+path)


def ramdom_graph_generator(verteces):
    edges = [(a,b) for a,b in permutations(verteces,2)]
    return  Graph({key:random.randint(1,100) for key in edges})
