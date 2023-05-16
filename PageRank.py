"""
PageRank算法，用于为一个有向图的各个节点打分。最经典的用途为基于网页的超链接来计算网页的分值，从而给网页进行排名。

若一个图有n个节点，则可定义一个 n×n 的转移矩阵M，Mij代表由节点i转移到节点j的概率。
初始状态下，任意节点的得分是均等的。记节点的得分向量为v。
另外，定义一个概率值α，代表一个节点有一定的概率转移到一个随机节点。

迭代方式：v = (1 - α)Mv + αv
"""
import numpy as np


class PageRank(object):
    def __init__(self, graph):
        self.graph = graph
        self.pr = self.init_pr()
        self.transition = self.create_transition()

    def create_transition(self):
        """ 基于有向图，构建转移矩阵 """
        shape = self.graph.shape
        transition = np.zeros(shape)
        for i in range(shape[0]):
            num_paths = sum(self.graph[i])
            for j in range(shape[1]):
                transition[i][j] = self.graph[i][j] / num_paths
        return transition

    def init_pr(self):
        """ 初始得分向量pr初始化 """
        shape = self.graph.shape
        pr = np.ones((shape[0], 1), dtype=float) / shape[0]
        return pr

    def run(self, alpha, max_iteration, epsilon):
        """ 运行page rank算法，直到收敛（满足epsilon），或达到最大迭代轮次 """
        for _ in range(max_iteration):
            pre_pr = self.pr
            self.pr = (1 - alpha) * self.transition.T @ self.pr + alpha * self.pr
            if np.linalg.norm(self.pr - pre_pr) <= epsilon:
                return self.pr


if __name__ == '__main__':
    g = np.array([[0, 1, 1, 1],
                  [1, 0, 0, 1],
                  [1, 0, 0, 0],
                  [0, 1, 1, 0]])
    sol = PageRank(g)
    print(sol.run(0.2, 100, 1e-8))
    # # print(sol.transition)
    # # print(sol.pr)
    # # print(sol.transition.T @ sol.pr)