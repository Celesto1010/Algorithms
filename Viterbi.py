"""
维特比算法。用于寻找最优路径。适用于解决层序的路径规划问题。
适配于解决HMM的三大问题之一：给定观测序列和模型参数，求最优（具有最大概率）的状态序列。
维特比算法的基本思路：若要求整体路径最优，则对于一个时间步上的一个节点，若最优路径经过了该节点，则从起点到该节点的子路径必为最优。
"""
import numpy as np


def viterbi(transition, emission, pi, observation):
    """ 维特比算法。矩阵乘法精简版 """
    # 状态个数
    num_states = np.shape(transition)[0]
    # 观测次数，即步数
    steps = np.shape(observation)[0]
    # 每个时刻每个状态对应的局部最优状态序列的概率数组
    delta = np.zeros((steps, num_states))
    # 每个时刻每个状态对应的局部最优状态序列的前导状态索引数组。第i行的第j列，即代表第i步时，若选取第j个节点，其最优路径的前一步的节点
    path = np.zeros((steps, num_states))

    for t in range(steps):
        if t == 0:
            delta[t] = pi.T * emission[:, observation[t]].T
        else:
            delta_tmp = delta[t - 1] * transition.T * emission[:, observation[t]]
            delta[t] = np.max(delta_tmp, axis=1)
            path[t] = np.argmax(delta_tmp, axis=1)
    print(delta)
    print(path)

    # 返回的最优状态序列
    states = np.zeros((steps,), dtype=int)
    # 从后往前确定最优路径
    for t in range(steps)[::-1]:
        # 最后一步，通过最优的delta值，确定最优路径经过的节点（隐状态）
        if t == steps - 1:
            states[t] = np.argmax(delta[t])
        # 前面的步，则根据path矩阵逆推即可
        else:
            states[t] = path[t + 1, states[t + 1]]
    return states


def viterbi_algorithm(transition, emission, pi, observation):
    """ 维特比算法，详细介绍版 """
    # 状态个数
    num_states = np.shape(transition)[0]
    # 观测次数，即步数
    steps = np.shape(observation)[0]
    
    # 每个时刻每个状态对应的局部最优状态序列的概率数组
    delta = np.zeros((steps, num_states))
    # [[0.18,    0.15,      0.1],        时刻0每个状态对应的局部最优状态序列的概率
    #  [0.03,    0.0756,    0.03],       时刻1每个状态对应的局部最优状态序列的概率
    #  [0.02268, 0.0054,    0.01512]]    时刻2每个状态对应的局部最优状态序列的概率
    
    # 每个时刻每个状态对应的局部最优状态序列的前导状态索引数组
    psi = np.zeros((steps, num_states))
    # [[0, 0, 0],       时刻0的前导状态索引
    #  [1, 0, 1],       时刻1的前导状态索引
    #  [1, 0, 1]]       时刻2的前导状态索引

    for t in range(steps):
        print('\n===================time t=%d' % t)
        # 第一步
        if t == 0:
            # delta[0]：初始隐状态向量 × 隐状态到第一个观测状态的发射向量
            delta[t] = np.multiply(pi.reshape((1, num_states)),
                                   np.array(emission[:, observation[t]]).reshape((1, num_states)))
            print('delta_t0:', delta[t])
            continue
        # 后续步
        # 考虑每一步的每一个节点（隐状态），基于delta[t-1]，确定对于这一步的每一个节点的最优路径
        for i in range(num_states):
            print('\n*****i=%d' % i)
            print('delta[t%d-1]:' % t, delta[t-1], 'A[:,i%d]' % i, transition[:, i])
            print('shape:::::, ', transition[:, i].shape)
            # 对于节点i，对delta[t - 1]向量与转移矩阵向量的乘积。该结果用来确定到该节点的最优路径
            delta_t_i = np.multiply(delta[t - 1], transition[:, i])
            print('delta_t%d_i%d step1:' % (t, i), delta_t_i)
            # 计算该结果与此刻的观测值对应的发射向量的乘积
            delta_t_i = np.multiply(delta_t_i, emission[i, observation[t]])
            print('delta_t%d_i%d result:' % (t, i), delta_t_i)
            # 取结果的最大值，即得到delta[t][i]
            delta[t, i] = max(delta_t_i)
            # 更新此节点对应的最优路径
            psi[t][i] = np.argmax(delta_t_i)
            print('delta:\n', delta)
            print('psi:\n', psi)
    
    states = np.zeros((steps,))
    t_range = -1 * np.array(sorted(-1 * np.arange(steps)))
    for t in t_range:
        if steps -1 == t:
            print('time %d'%t, np.argmax(delta[t]))
            states[t] = np.argmax(delta[t])
        else:
            print('psi shape:', np.shape(psi))
            print('states shape:', np.shape(states))
            states[t] = psi[t + 1, int(states[t + 1])]
    print('best state queue:', states)
    return states


if __name__ == '__main__':
    # A: 状态转移概率分布，状态集合Q的大小N=np.shape(A)[0]
    # 从下给定A可知：Q={盒1, 盒2, 盒3}, N=3
    A = np.array([[0.2, 0.6, 0.2],
                  [0.5, 0.1, 0.4],
                  [0.6, 0.2, 0.2]])

    # B：观测概率分布，即发射矩阵。观测集合V的大小T=np.shape(B)[1]
    # 从下面给定的B可知：V={红，白}，T=2
    B = np.array([[0.6, 0.4],
                  [0.3, 0.7],
                  [0.5, 0.5]])
    # Π是初始状态概率分布，初始状态个数=np.shape(Π)[0]
    pai = np.array([[0.3],
                    [0.5],
                    [0.2]])

    # 观测序列。0表示红色，1表示白，就是(红，白，红)观测序列
    O = np.array([[0],
                  [1],
                  [0]])
    print(viterbi(A, B, pai, O))