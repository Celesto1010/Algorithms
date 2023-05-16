"""
冒泡排序
1. 比较相邻的元素，若前者比后者大，则交换二者的顺序。每一对执行一次，最终最大的元素出现在末尾。
2. 对于数组中除末尾元素的其他元素，重复执行第一步。使得末尾的子数组均为有序。
3. 持续执行，直到数组有序

时间复杂度：O(n2)
"""


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] >= array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    arr = [5, 3, 2, 8, 9, 10, 7, 6, 2]
    print(bubble_sort(arr))