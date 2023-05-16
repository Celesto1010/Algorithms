"""
计数排序
1. 遍历一次，寻找待排序集合中的最大值与最小值，计算其差值，根据该值申请额外空间；
2. 遍历待排序集合，将每个元素出现的次数记录到元素值对应的额外空间中。
3. 展开额外空间，即为排好序的集合

时间复杂度：O(n + k)
空间复杂度：O(k)

局限性：不适用于非整数；不适用于最大最小值差距过大的数组
"""


def count_sort(array):
    max_val, min_val = max(array), min(array)
    # 记录每个元素出现的次数
    count = dict([(i, 0) for i in range(min_val, max_val + 1)])
    for num in array:
        count[num] += 1
    ret = list()
    for num, num_count in count.items():
        ret.extend([num] * num_count)
    return ret


if __name__ == '__main__':
    print(count_sort([4, 2, 5, 7, 8, 2, 6, 6, 9, 4, 8]))