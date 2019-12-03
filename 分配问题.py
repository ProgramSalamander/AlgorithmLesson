import sys
from itertools import permutations

# 分配问题
# 描述
# 对给定的n个任务与n个人之间的成本矩阵完成成本最低的任务分配策略。
# 输入
# 第一行为用例个数，之后为每一个用例；用例的第一行为任务个数，即n；
# 用例的第二行为使用逗号隔开的人员完成任务的成本；每一个成本描述包括人员序号、任务序号和成本，使用空格隔开。
# 人员序号和任务序号都是从1到n的整数，序号出现的次序没有固定规则。
# 输出
# 每一个用例输出一行，从序号为1的人员开始，给出其分配的任务序号，使用空格隔开；使用逗号将多个解隔开。
# 结果按照人员分配的任务序号大小排，第一个人员的任务序号大的放在前面，如果相同则看第二个人员的任务，以此类推。
# 输入样例 1
# 1
# 4
# 2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
# 输出样例 1
# 2 1 3 4

if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        n = int(input())
        costs = input().split(',')
        cost_arr = [[0 for _ in range(n)] for _ in range(n)]
        for cost in costs:
            tmp = cost.split(' ')
            worker_no = int(tmp[0]) - 1
            task_no = int(tmp[1]) - 1
            cost_arr[worker_no][task_no] = int(tmp[2])
        # print(cost_arr)
        min_cost = sys.maxsize
        min_permutations = []
        for permutation in permutations(range(n), n):
            cost = 0
            for i in range(n):
                cost += cost_arr[i][permutation[i]]
            if min_cost > cost:
                min_cost = cost
                min_permutations = [permutation]
            elif min_cost == cost:
                min_permutations.append(permutation)
        # print(min_cost)
        # print(min_permutations)
        min_permutations.sort(reverse=True)
        print(",".join(" ".join(str(task_no + 1) for task_no in permutation) for permutation in min_permutations))
        

