# 广度优先遍历图
# 描述
#
# 按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。
#
#
# 输入
#
# 输入第一行为测试用例个数，后面每一个用例用多行表示，用例第一行是节点个数n和开始顶点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
#
#
# 输出
#
# 输出遍历顺序，用空格隔开
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
# a b c d


class Graph:
    def __init__(self, adj):
        self.adj = adj

    def bfs(self, start):
        stack = [start]
        visited = set()
        traversal_order = [start]
        while stack:
            cur = stack[-1]
            visited.add(cur)
            no_child = True
            for i in range(n):
                if self.adj[cur][i] == 1 and (i not in visited):
                    stack.append(i)
                    visited.add(i)
                    traversal_order.append(i)
                    no_child = False
            if no_child:
                stack.pop()
        return traversal_order

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
        traversal_order = g.bfs(ids.index(start))
        print(' '.join([ids[i] for i in traversal_order]))