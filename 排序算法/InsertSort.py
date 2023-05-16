"""
插入排序
将一个新数据插入到已经排好序的有序数组中，从而一个新的、数据增1的有序数组。
时间复杂度：O(n) ~ O(n2)
"""


def insert_sort(array):
    """ 插入排序。生成升序的有序序列 """
    for i in range(1, len(array)):
        j = i - 1
        # 将array[i]插入已排序的序列array[:j]
        while j >= 0 and array[j] > array[i]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = array[i]
    return array


if __name__ == '__main__':
    print(insert_sort([4, 2, 6, 5, 1, 8, 9]))
