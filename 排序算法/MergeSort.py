"""
合并（归并）排序
1. 分解：将待排序集合分成大小大致相同的两个子序列。
2. 求解子问题：用分别对两个子序列递归地进行排序。
3. 合并：将排好序的有序子序列进行合并，得到符合要求的有序序列。
"""


def merge_sort(array):
    """ 合并排序算法，分治部分 """
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def merge(left, right):
    """ 合并算法，合并部分：将两组已排好序的数组进行合并，合并后的数组仍然为有序 """
    ret = []
    left.append(float('inf'))
    right.append(float('inf'))
    # m、n分别为left、right数组的指针
    m, n = 0, 0
    for _ in range(len(left) + len(right) - 2):
        if left[m] <= right[n]:
            ret.append(left[m])
            m += 1
        else:
            ret.append(right[n])
            n += 1
    return ret


if __name__ == '__main__':
    print(merge_sort([5, 3, 2, 8, 9, 10, 7, 6, 2]))