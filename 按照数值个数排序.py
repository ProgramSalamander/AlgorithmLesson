# 按照数值个数排序
# 描述
#
# 对给定数组中的元素按照元素出现的次数排序，出现次数多的排在前面，如果出现次数相同，则按照数值大小排序。
# 例如，给定数组为{2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}，则排序后结果为{3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}。
#
#
# 输入
#
# 输入的第一行为用例个数；后面每一个用例使用两行表示，第一行为数组长度，第二行为数组内容，数组元素间使用空格隔开。
#
#
# 输出
#
# 每一个用例的排序结果在一行中输出，元素之间使用空格隔开。
#
#
# 输入样例 1
#
# 1
# 4
# 2 3 2 5
# 输出样例 1
#
# 2 2 3 5


import operator


def sort_by_count(array):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_arr = []
    for i, count in sorted_dict:
        for _ in range(count):
            sorted_arr.append(i)
    return sorted_arr


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        arr_length = int(input())
        arr = [int(_) for _ in input().split(' ')]
        sorted_arr = sort_by_count(arr)
        print(' '.join([str(_) for _ in sorted_arr]))
