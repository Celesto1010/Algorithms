"""
快速排序
1. 取一个分界值，将数组中小于该分界值的数放到左边，大于或等于该分界值的数放到右边。
2. 对于新的左右数组，继续进行取分界值 - 划分左右的操作。始终递归直到所有元素有序。
"""


def quick_sort(array, start, end):
    # 当数组只有零个或一个数据时，递归结束
    if start >= end:
        return
    # 取数组最左边的值作为划分值
    mid_data, left, right = array[start], start, end
    while left < right:
        # 若right指向的值比划分值大，则该值不需要移动。right -= 1
        while array[right] >= mid_data and left < right:
            right -= 1
        # 遇到right指向的值比划分值小，则将该值赋给left位置，并开始检查left的值
        array[left] = array[right]
        # 若left指向的值比划分值小，则该值不需要移动。left += 1
        while array[left] < mid_data and left < right:
            left += 1
        # 遇到left指向的值比划分值大，则将该值赋给right位置，并开始检查right的值
        array[right] = array[left]
    # 当左右子数组的值都分配完毕，最后将划分值赋给left位置。完成本次处理。
    array[left] = mid_data
    # 对划分值左右的子数组递归进行快速排序
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)


if __name__ == '__main__':
    arr = [5, 3, 2, 8, 9, 10, 7, 6, 2]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)