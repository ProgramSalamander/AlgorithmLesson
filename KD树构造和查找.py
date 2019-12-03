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


def mean(array):
    return sum(array) / len(array)


def variance(array):
    m = mean(array)
    return sum(map(lambda x: (x - m) ** 2, array)) / len(array)


class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance(self, another_point):
        return math.sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)


class KDTreeNode:

    def __init__(self, data, depth=0, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
        self.depth = depth


class KDTree:

    def __init__(self):
        self.nearest = []
        self.KdTree = None
        self.n = 0
        self.axis = 0

    def create(self, data, depth=0):
        if len(data) > 0:
            var_x = variance([x[0] for x in data])
            var_y = variance([x[1] for x in data])
            # 按照方差大小决定哪个维度进行分割。0：x轴，1：y轴。
            self.axis = 0 if var_x > var_y else 1
            # 中位数
            mid = len(data) // 2
            # 按照维度进行排序
            data_copy = sorted(data, key=lambda x: x[self.axis])
            # KD结点为中位数的结点，树深度为depth
            node = KDTreeNode(data_copy[mid], depth)
            if depth == 0:
                self.KdTree = node
            # 前mid行为左子结点，此时行数m改变，深度depth+1，axis会换个维度
            node.lchild = self.create(data_copy[:mid], depth + 1)
            node.rchild = self.create(data_copy[mid + 1:], depth + 1)
            return node
        else:
            return None

    def search(self, target, k_nearest=1):
        self.nearest = []

        def recursive(node):
            if node is not None:
                distance = math.sqrt((node.data[0] - target[0]) ** 2 + (node.data[1] - target[1]) ** 2)
                if len(self.nearest) < k_nearest:
                    self.nearest.append((node, distance))
                    self.nearest.sort(key=lambda x: x[1])
                else:
                    if self.nearest[-1][1] > distance:
                        self.nearest[-1] = (node, distance)
                        self.nearest.sort(key=lambda x: x[1])
                recursive(node.lchild)
                recursive(node.rchild)

        recursive(self.KdTree)
        return self.nearest


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        points = []
        data_type = -1
        for s in input().split(','):
            x, y = s.split(' ')
            if data_type == -1:
                data_type = 1 if '.' in x else 0
            points.append([float(x), float(y)])
        target_x, target_y = input().split(' ')
        target_point = [float(target_x), float(target_y)]
        k = int(input())
        kd_tree = KDTree()
        kd_tree.create(points)
        res = kd_tree.search(target_point, k)
        datas = [_[0].data for _ in res]
        if data_type == 1:
            print(','.join([str(data[0]) + ' ' + str(data[1]) for data in datas]))
        else:
            print(','.join([str(int(data[0])) + ' ' + str(int(data[1])) for data in datas]))
