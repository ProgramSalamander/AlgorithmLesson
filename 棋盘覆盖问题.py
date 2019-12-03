# 棋盘覆盖问题
# 描述
#
# 棋盘覆盖问题：给定一个大小为2^n2^n个小方格的棋盘，其中有一个位置已经被填充，现在要用一个L型（22个小方格组成的大方格中去掉其中一个小方格）形状去覆盖剩下的小方格。求出覆盖方案，即哪些坐标下的小方格使用同一个L型格子覆盖。注意：坐标从0开始。左上方的第一个格子坐标为(0,0)，第一行第二个坐标为(0,1)，第二行第一个为(1,0)，以此类推。
#
#
# 输入
#
# 输入第一行为测试用例个数，后面每一个用例有两行，第一行为n值和特殊的格子的坐标（用空格隔开），第二行为需要查找其属于同一个L型格子的格子坐标。
#
#
# 输出
#
# 输出每一行为一个用例的解，先按照行值从小到大、再按照列值从小到大的顺序输出每一个用例的两个坐标；用逗号隔开。
#
#
# 输入样例 1
#
# 1
# 1 1 1
# 0 0
# 输出样例 1
#
# 0 1,1 0

import copy


class Chessboard:
    def __init__(self, n=1):
        self.Ls = []
        self.n = n

    def cover(self, special):

        def recursive(n, left_top, special):
            if n == 1:
                points = [left_top,
                          (left_top[0] + 1, left_top[1]),
                          (left_top[0], left_top[1] + 1),
                          (left_top[0] + 1, left_top[1] + 1)]
                points.remove(special)
                self.Ls.append(points)
            else:
                gap = 2 ** (n - 1)
                left_tops = [left_top,
                             (left_top[0] + gap, left_top[1]),
                             (left_top[0], left_top[1] + gap),
                             (left_top[0] + gap, left_top[1] + gap)]

                if special[0] < left_tops[3][0] and special[1] < left_tops[3][1]:
                    specials = [special,
                                (left_tops[3][0], left_tops[3][1] - 1),
                                (left_tops[3][0] - 1, left_tops[3][1]),
                                (left_tops[3][0], left_tops[3][1])]
                elif special[0] >= left_tops[3][0] and special[1] < left_tops[3][1]:
                    specials = [(left_tops[3][0] - 1, left_tops[3][1] - 1),
                                special,
                                (left_tops[3][0] - 1, left_tops[3][1]),
                                (left_tops[3][0], left_tops[3][1])]
                elif special[0] < left_tops[3][0] and special[1] >= left_tops[3][1]:
                    specials = [(left_tops[3][0] - 1, left_tops[3][1] - 1),
                                (left_tops[3][0], left_tops[3][1] - 1),
                                special,
                                (left_tops[3][0], left_tops[3][1])]
                else:
                    specials = [(left_tops[3][0] - 1, left_tops[3][1] - 1),
                                (left_tops[3][0], left_tops[3][1] - 1),
                                (left_tops[3][0] - 1, left_tops[3][1]),
                                special]
                special_L = copy.copy(specials)
                special_L.remove(special)
                self.Ls.append(special_L)
                for i in range(4):
                    recursive(n - 1, left_top=left_tops[i], special=specials[i])

        recursive(self.n, (0, 0), special)


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        line = [int(_) for _ in input().split(' ')]
        n = line[0]
        special = (line[1], line[2])
        target_x, target_y = [int(_) for _ in input().split(' ')]
        target = (target_x, target_y)
        # print(n)
        # print(special)
        # print(target)
        chessboard = Chessboard(n)
        chessboard.cover(special)
        for L in chessboard.Ls:
            if target in L:
                output_L = L
                output_L.remove(target)
                output_L.sort()
                print(','.join([str(_[0]) + ' ' + str(_[1]) for _ in output_L]))
                break
