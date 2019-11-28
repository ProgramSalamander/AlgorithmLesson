# KD树构造和查找
# 描述
# 对给定的点集合构造KD树，要求如下：将方差最大的维度作为当前的分割维度，将数据集在分割维度上排序后的中位数作为分割点。
# 程序要检索给定点对应的最近的K个点的坐标。
# 输入
# 输入第一行为测试用例个数，后面为测试用例
# 每一个用例包含三行，第一行为点集合（点之间用逗号隔开，两个坐标用空格隔开），第二行为检索的点，第三行为K值。
# 输出
# 输出每一个用例的最近K个点，按照距离从小到大的顺序打印。
# 输入样例 1
# 1
# 3 5,6 2,5 8,9 3,8 6,1 1,2 9
# 8.2 4.6
# 2
# 输出样例 1
# 8 6,9 3


import math


class Point:

    def __init__(self, s):
        ss = s.split(' ')
        self.x = float(ss[0])
        self.y = float(ss[1])


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        xs = []
        ys = []
        for point in input().split(','):
            xs.append(int(point[0]))
            ys.append(int(point[1]))
        target = input()
        k = int(input())
        length = len(xs)
        sumX = 0
        sumY = 0
        for x, y in xs, ys:
            sumX += x
            sumY += y
        meanX = sumX / length
        meanY = sumY / length
        tempX = 0
        tempY = 0
        for x, y in xs, ys:
            tempX += pow(x - meanX, 2)
            tempY += pow(y - meanY, 2)
        varX = tempX / length
        varY = tempY / length
        xs_sorted = xs
        xs_sorted.sort()
        ys_sorted = ys
        ys_sorted.sort()

        mid = xs_sorted[int(length / 2)] if varX > varY else ys_sorted[int(length / 2)]
