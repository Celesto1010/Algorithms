"""
赫夫曼编码与赫夫曼树
赫夫曼树即最优二叉树。该树的带权路径长度在所有二叉树中最小
假定C是一个n个字符的集合，其中每个字符 c∈C 都是一个对象，其属性c.freq给出了字符的出现频率，即权值。
算法自底向上地构造出对应的最优编码的二叉树T。它从|C|个叶节点开始，执行|C|-1个“合并”操作，创建出最终的二叉树。
https://blog.csdn.net/BGoodHabit/article/details/106068573
"""


class Node(object):
    """
    节点类。
    key：节点的特征值（如freq）
    code：节点编码，0或1. 节点的最终编码由根节点到该节点路径上所有节点的编码组合而成。
    """
    def __init__(self, key, code=0, parent=None, lchild=None, rchild=None):
        self.key = key
        self.code = code
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        # tree保存节点。其中原始节点按照顺序在tree的前面，组合而成的新节点按照顺序依次在后面排列
        self.tree = list()
        self.root = root

    def find_node(self, flag):
        """ 找到当前key最小的两个节点 """
        min_key_nodes = list()
        # 遍历所有节点。跳过已经合并、组成子树的节点，用合并后新产生的节点取代
        for i in range(len(self.tree)):
            if i in flag:
                continue
            if len(min_key_nodes) < 2:
                min_key_nodes.append(i)
            else:
                # 若新遍历的节点的key小于min_key_nodes，则用该新节点取代min_key_nodes中key较大的那一个
                if self.tree[i].key < max(self.tree[min_key_nodes[0]].key, self.tree[min_key_nodes[1]].key):
                    index = 0 if self.tree[min_key_nodes[0]].key > self.tree[min_key_nodes[1]].key else 1
                    min_key_nodes[index] = i
        # 调整，使得lchild.key < rchild.key
        if self.tree[min_key_nodes[0]].key > self.tree[min_key_nodes[1]].key:
            min_key_nodes[0], min_key_nodes[1] = min_key_nodes[1], min_key_nodes[0]
        return min_key_nodes

    def build(self, nodes):
        """ 建立huffman tree """
        # 以flag记录已经被合并的节点（的index）
        flag = list()
        # 初始化所有节点
        for node_key in nodes:
            self.tree.append(Node(key=node_key))
        # 创建树。n个值需要n-1次合并操作
        for _ in range(len(nodes) - 1):
            min_key_nodes = self.find_node(flag)
            flag.append(min_key_nodes[0])
            flag.append(min_key_nodes[1])
            l_node, r_node = self.tree[min_key_nodes[0]], self.tree[min_key_nodes[1]]
            # 构建合并后的新节点
            new_key = l_node.key + r_node.key
            new_node = Node(key=new_key, lchild=l_node, rchild=r_node)
            # 将新节点加入. 记录
            self.tree.append(new_node)
            l_node.parent = r_node.parent = new_node
            # 定义右子树的code为1
            r_node.code = 1
        # 完成创建后，记录root节点
        self.root = new_node

    # 中序遍历
    def inorder_tree_walk(self, tree):
        if tree is not None:
            self.inorder_tree_walk(tree.lchild)
            print(tree.key, end=" ")
            self.inorder_tree_walk(tree.rchild)

    @staticmethod
    def get_huffman_code(cur_node):
        """ 获取某个节点的code. 由树的叶子节点从下往上走到根节点 """
        path = list()
        while cur_node.parent is not None:
            path.insert(0, cur_node.code)
            cur_node = cur_node.parent
        return path


if __name__ == '__main__':
    huff_tree = Tree()
    C = [5, 9, 12, 13, 16, 45]
    huff_tree.build(C)
    huff_tree.inorder_tree_walk(huff_tree.root)
    print()
    for i in range(len(C)):
        node_path = huff_tree.get_huffman_code(huff_tree.tree[i])
        print('key=' + str(huff_tree.tree[i].key))
        print(node_path)
