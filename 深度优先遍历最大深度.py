# 深度优先遍历
# 描述
#
# 按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。
#
#
# 输入
#
# 输入第一行是用例个数，后面每个用例使用多行表示，用例的第一行是图中节点的个数n和起始点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
#
#
# 输出
#
# 输出深度优先遍历中遇到的最大深度。
#
#
# 输入样例 1
#
# 1
# 4 a
# a b c d
# a 0 1 1 0
# b 1 0 1 0
# c 1 1 0 1
# d 0 0 1 0
# 输出样例 1
#
# 4


class Graph:
    def __init__(self, adj):
        self.adj = adj

    def dfs(self, start):
        stack = [start]
        visited = set()
        max_depth = 0
        while stack:
            cur = stack[-1]
            visited.add(cur)
            no_child = True
            for i in range(n):
                if self.adj[cur][i] == 1 and (i not in visited):
                    stack.append(i)
                    max_depth = max(max_depth, len(stack))
                    no_child = False
                    break
            if no_child:
                stack.pop()
        return max_depth


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        n, start = input().split(' ')
        n = int(n)
        adj = [[0 for _ in range(n)] for _ in range(n)]
        ids = input().split(' ')
        for i in range(n):
            line = input().split(' ')
            for j in range(1, n + 1):
                adj[i][j - 1] = int(line[j])
        # print(adj)
        g = Graph(adj)
        max_depth = g.dfs(ids.index(start))
        print(max_depth)
