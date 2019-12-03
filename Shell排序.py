# 实现Shell排序
# 描述
#
# 实现Shell排序，对给定的无序数组，按照给定的间隔变化（间隔大小即同组数字index的差），打印排序结果，注意不一定是最终排序结果！
#
#
# 输入
#
# 输入第一行表示测试用例个数，后面为测试用例，每一个用例有两行，第一行为给定数组，第二行为指定间隔，每一个间隔用空格隔开。
#
#
# 输出
#
# 输出的每一行为一个用例对应的指定排序结果。
#
#
# 输入样例 1
#
# 1
# 49 38 65 97 76 13 27 49 55 4
# 5 3
# 输出样例 1
#
# 13 4 49 38 27 49 55 65 97 76

def shell_sort(array, intervals):
    _array = array
    for interval in intervals:
        for i in range(interval):
            for j in range(i, len(_array), interval):
                for k in range(i, j, interval):
                    if _array[j] < _array[k]:
                        tmp = _array[j]
                        for m in range(j, k, -interval):
                            _array[m] = _array[m - interval]
                        _array[k] = tmp
    return _array


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        array = [int(_) for _ in input().split(' ')]
        intervals = [int(_) for _ in input().split(' ')]
        sorted_array = shell_sort(array, intervals)
        print(' '.join([str(_) for _ in sorted_array]))