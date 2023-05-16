"""
弗洛伊德算法，用于计算一个加权图中任意两点间的最短路径。可用于有向图。
从第一个顶点开始，依次将每个顶点作为媒介 k，然后对于每一对顶点 i 和 j ，查看其是否存在一条经过 k 的，距离比已知路径更短的路径，如果存在则更新它。
"""


def floyd_warshall(graph_matrix):
    """ graph_matrix: 图矩阵。若两点未连接，则对应位置的值为inf """
    num_nodes = len(graph_matrix)

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                graph_matrix[i][j] = min(graph_matrix[i][j], graph_matrix[i][k] + graph_matrix[k][j])
    return graph_matrix


if __name__ == '__main__':
    g = [[0, 2, 6, 4],
         [float('inf'), 0, 3, float('inf')],
         [7, float('inf'), 0, 1],
         [5, float('inf'), 12, 0]]
    print(floyd_warshall(g))