"""
Dijkstra算法，计算有向图中两点的最短距离的路径
计算某节点i到其他每个节点的最短距离路径：
1. 根据图，初始化点i到其他每个节点的距离。即：直接联通
2. 找出图中距离点i最近的点，称为点k。注意：这个点之前没有被作为点k过
3. 对于每一个其他节点j，计算该点经过点k后到达节点j的距离是否比之前更近。若更近，则更新点i到点j的距离与路径
4. 对于2、3，执行n - 1次的遍历。即把每个其他点都当作一次点k
"""


def get_shortest_route(graph):
    n = len(graph)                  # 节点个数
    dp = [float('inf')] * n         # 记录第一个节点到其他每个节点的最短距离
    dpp = [[]] * n                  # 记录第一个节点到其他每个节点的最短距离的路径
    seen = [0] * n                  # 记录各节点是否访问。0代表未访问

    # 初始化：第一个节点到各节点的初始最短距离
    for i in range(n):
        dp[i] = graph[0][i]
        dpp[i] = [i + 1]
    print('到各点的初始化最短距离：', dp, dpp)

    # n-1次遍历
    for i in range(1, n):
        min_ = float('inf')
        # 找到图中距离源点最近的点k。这个点以前没有被当作点k过
        for j in range(1, n):
            if dp[j] < min_ and seen[j] == 0:
                min_ = dp[j]
                k = j
        # 标记点k为已访问
        seen[k] = 1
        # 计算源点经过点k到达某个点j是否比原来更近
        for j in range(1, n):
            # 若更近，且j未访问，则更新路径与最短距离
            if dp[j] > dp[k] + graph[k][j] and seen[j] == 0:
                dp[j] = dp[k] + graph[k][j]
                dpp[j] = [k + 1, j + 1]
    return dp, dpp


if __name__ == "__main__":
    inf = float('inf')
    mgraph = [[0, 5, 2, inf, inf],
              [inf, 0, 2, 6, 1],
              [inf, inf, 0, 7, 6],
              [inf, inf, 7, 0, 2],
              [inf, inf, inf, inf, 0]]
    dp, dpp = get_shortest_route(mgraph)
    for i in range(len(dp)):
        print('到点', i + 1, '的最短距离：', dp[i], '路径：', dpp[i])