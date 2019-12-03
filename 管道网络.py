# 管道网络
# 描述
#
# Every house in the colony has at most one pipe going into it and at most one pipe going out of it.
# Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap.
# Find the efficient way for the construction of the network of pipes.
#
#
# 输入
#
# The first line contains an integer T denoting the number of test cases.
# For each test case, the first line contains two integer n & p denoting the number of houses and number of pipes respectively.
# Next, p lines contain 3 integer inputs a, b & d, d denoting the diameter of the pipe from the house a to house b.
# Constraints:
# 1<=T<=50，1<=n<=20，1<=p<=50，1<=a, b<=20，1<=d<=100
#
#
# 输出
#
# For each test case, the output is the number of pairs of tanks and taps installed i.e n followed by n lines that contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.
#
#
# 输入样例 1
#
# 1
# 9 6
# 7 4 98
# 5 9 72
# 4 6 10
# 2 8 22
# 9 7 17
# 3 1 66
# 输出样例 1
#
# 3
# 2 8 22
# 3 1 66
# 5 6 10

import sys
if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        houses_num, pipes_num = [int(_) for _ in input().split(' ')]
        tanks = []
        taps = []
        froms = []
        tos = []
        diameters = []
        for _ in range(pipes_num):
            from_house, to_house, diameter = [int(_) for _ in input().split(' ')]
            froms.append(from_house)
            tos.append(to_house)
            diameters.append(diameter)
        for i in range(1, houses_num + 1):
            if i in froms and i in tos:
                pass
            elif i in froms:
                tanks.append(i)
            elif i in tos:
                taps.append(i)
        # print(tanks)
        # print(taps)
        print(len(tanks))
        for tank in tanks:
            cur = tank
            min_diameter = sys.maxsize
            while cur in froms:
                idx = froms.index(cur)
                min_diameter = min(diameters[idx], min_diameter)
                cur = tos[froms.index(cur)]
            print('%d %d %d'%(tank, cur, min_diameter))