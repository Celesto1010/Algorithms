"""
希尔排序
1. 通过某个增量，将数组分为若干组。对每一组的子数组分别进行插入排序。
2. 对于分组排序而生成的新数组，缩小增量，重复进行步骤1
3. 重复进行步骤2，直到增量为1。此时数组已基本有序，只需要进行微调即可。
"""


def shell_sort(array):
    # 初始增量取length // 2
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp: #">"由小到大排序；"<"由大到小排序
                array[j] = array[j - gap]
                j -= gap
                array[j] = temp
        gap = gap // 2 #再次