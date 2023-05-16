"""
Prim算法，用于生成最小生成树。
最小生成树：一个联通加权无向图的一颗权值最小的生成树
Prim算法：
    1. 以某一点开始，寻找当前该点可以访问的所有边；
    2. 在可访问的所有边中，确定一条满足另一个端点还没有被访问过的前提下权值最小的边。称该边为最小边。将这条边的另一个点加入集合，并记录该边。
    3. 对于当前集合的所有点，重复步骤2，直到没有新的点可以加入集合。
    4. 此时由所有边构成的树即为最小生成树。
"""


from heapq import *
from collections import defaultdict
import random


def prim(edges):
    """
    prim算法
    :param edges: 图的所有边。每一条边形如(weight, node_a, node_b)
    :return: 最小生成树
    """
    adjacent_dict = defaultdict(list)
    for weight, v1, v2 in edges:
        adjacent_dict[v1].append((weight, v1, v2))
        adjacent_dict[v2].append((weight, v2, v1))
    '''
    经过上述操作，将图转化为以下邻接表形式：
    {'A': [(7, 'A', 'B'), (5, 'A', 'D')], 
     'C': [(8, 'C', 'B'), (5, 'C', 'E')], 
     'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')], 
     'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')], 
     'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')], 
     'G': [(9, 'G', 'E'), (11, 'G', 'F')], 
     'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')]})
    '''
    start = random.choice(list(adjacent_dict.keys()))

    # 存储最小生成树的结果
    minu_tree = []
    # 记录已访问过的点
    visited = [start]
    # 点相连的所有边，将这些边转为最小堆，便于快速找到权重最小的边
    adjacent_vertexs_edges = adjacent_dict[start]
    heapify(adjacent_vertexs_edges)

    while adjacent_vertexs_edges:
        # 找到权重最小的边，并从堆中删除
        weight, v1, v2 = heappop(adjacent_vertexs_edges)
        # 若另一个端点未被访问过：
        if v2 not in visited:
            # 将另一个端点记录为已访问
            visited.append(v2)
            # 在最小树中记录此路径
            minu_tree.append((weight, v1, v2))
            # 再检测另一个端点的所有路径。若路径不在堆中，则压入堆，参与下一次的最小边的搜寻
            for edge in adjacent_dict[v2]:
                # 若这些路径的另一端点未被访问过，则将这条路径放入堆中
                heappush(adjacent_vertexs_edges, edge)
    return minu_tree


if __name__ == '__main__':
    e = [(7, 'A', 'B'),
         (5, 'A', 'D'),
         (8, 'B', 'C'),
         (9, 'B', 'D'),
         (7, 'B', 'E'),
         (5, 'C', 'E'),
         (15, 'D', 'E'),
         (6, 'D', 'F'),
         (8, 'E', 'F'),
         (9, 'E', 'G'),
         (11, 'F', 'G'),
         ]
    print(prim(e))
