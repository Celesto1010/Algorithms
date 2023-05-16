"""
选择排序
1. 在未排序序列中找到最小元素，交换该元素与序列第一个元素。
2. 再从剩余序列继续寻找最小元素，交换该元素与剩余序列的第一个元素。
3. 重复第二步，直到所有元素均排序完毕。
"""


def selection_sort(array):
    for i in range(len(array) - 1):
        # 记录最小数的索引
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    arr = [4, 2, 5, 7, 8, 2, 6, 6, 9, 4, 8]
    print(selection_sort(arr))