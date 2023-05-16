"""
堆排序
堆：即完全二叉树。包括大顶堆与小顶堆。
    最大堆：每个节点的值都大于或者等于它的左右子节点的值。若映射为数组，即：arr[i] >= arr[2i + 1] && arr[i] >= arr[2i + 2]
    最小堆：每个节点的值都小于或者等于它的左右子节点的值。若映射为数组，即：arr[i] <= arr[2i + 1] && arr[i] <= arr[2i + 2]
堆排序：基于堆的性质（堆顶节点一定是最大/最小）进行排序
"""


def max_heapify(array, i, size):
    """ 对于数组中的某一个index的节点，使得以该index节点为根节点的子树保持最大堆性质 """
    # 节点索引为i的左孩子索引：2*i+1；右孩子索引：2*i+2
    left_index, right_index = 2 * i + 1, 2 * i + 2
    # 左节点未溢出时，比较左节点与原节点的值，标记较大的一个为largest
    if left_index < size and array[left_index] > array[i]:
        largest = left_index
    else:
        largest = i
    # 若右节点未溢出，比较右节点与largest节点的值，标记较大的一个为largest
    if right_index < size and array[right_index] > array[largest]:
        largest = right_index
    # 若largest是原节点，则该节点与其两个子节点已满足最大堆性质，不需调整。
    # 否则，调整原节点与largest节点的位置，并以largest节点为根节点继续递归，保证这一颗子树都符合最大堆性质。
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        # 以largest为根节点的子树，由于刚刚经历修改（移动了一个较小的值过来），可能又违背最大堆性质，所以需要继续递归调用
        max_heapify(array, largest, size)


def min_heapify(array, i, size):
    """ 对于数组中的某一个index的节点，使得以该index节点为根节点的子树保持最小堆性质 """
    left_index, right_index = 2 * i + 1, 2 * i + 2
    if left_index < size and array[left_index] < array[i]:
        smallest = left_index
    else:
        smallest = i
    if right_index < size and array[right_index] < array[smallest]:
        smallest = right_index
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest, size)


# 建堆，自顶向下方法，把一个大小为n的数组A，转换为最大/小堆
def build_max_heap(array):
    mid = len(array) // 2 - 1
    # 最终的堆中，array[mid+1, ..., size]都是树的叶节点，所以只需要对其他节点调用max_heapify，保证最大堆的性质就可
    # 从右往左，从下往上修改树
    for i in range(mid, -1, -1):
        max_heapify(array, i, len(array))
    return array


def build_min_heap(array):
    mid = len(array) // 2 - 1
    # 从右往左，从下往上修改树
    for i in range(mid, -1, -1):
        min_heapify(array, i, len(array))
    return array


def heap_sort(array):
    """
    堆排序
    1. 建最大堆；
    2. 将堆顶节点与最后一个节点交换
    3. 将除最后一个节点（原本的堆顶节点）之外的所有节点，重新构造一个最大堆
    4. 重复步骤2、3
    """
    # 建堆
    build_max_heap(array)
    # 最大元素总在根节点，即array[0]。根节点与最后一个节点array[-1]交换
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        # 每次交换后，需要保证根节点维持最大堆性质。同时将树的规模缩小（即去掉交换后的最后一个节点）
        max_heapify(array, 0, i)
    return array


if __name__ == '__main__':
    arr = [5, 3, 2, 8, 9, 10, 7, 6, 2]
    print(heap_sort(arr))