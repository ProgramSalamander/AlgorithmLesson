# 拓扑排序解的个数
# 描述
#
# 给定有向无环图中所有边，计算图的拓扑排序解的个数。
#
#
# 输入
#
# 输入第一行为用例个数，后面每一行表示一个图中的所有边，边的起点和终点用空格隔开，边之间使用逗号隔开。
#
#
# 输出
#
# 输出拓扑排序解的个数。
#
#
# 输入样例 1
#
# 1
# a c,b c,c d,d e,d f,e g,f g
# 输出样例 1
#
# 4


import copy


class GraphNode:
    def __init__(self, id):
        self.id = id
        self.outgoings = []
        self.incomings = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def topology_count(self):
        counts = []
        nodes = copy.deepcopy(self.nodes)
        while nodes:
            tmp_count = 0
            remove_nodes = []
            for node in nodes.values():
                if not node.incomings:
                    tmp_count += 1
                    remove_nodes.append(node)
            counts.append(tmp_count)
            for remove_node in remove_nodes:
                for node in nodes.values():
                    if remove_node in node.incomings:
                        node.incomings.remove(remove_node)
                nodes.pop(remove_node.id)
        total_count = 1
        for count in counts:
            total_count *= count
        return total_count

if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        g = Graph()
        for edge in input().split(','):
            from_id, to_id = edge.split(' ')
            from_node = g.nodes[from_id] if from_id in g.nodes else GraphNode(from_id)
            to_node = g.nodes[to_id] if to_id in g.nodes else GraphNode(to_id)
            from_node.outgoings.append(to_node)
            to_node.incomings.append(from_node)
            g.nodes[from_id] = from_node
            g.nodes[to_id] = to_node
        print(g.topology_count())
