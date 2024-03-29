# 矩阵计算
# 描述
#
# Let's define a Series Whose recurrence formula is as follows :
#
# C(n)= 3C(i-1) + 4C(i-2) + 5C(i-3) + 6C(i-4)
#
# C(0)= 2
#
# C(1)= 0
#
# C(2)= 1
#
# C(3)= 7
#
# Now based on this Series a Matrix Mi,j of size nn is to be formed.
# The top left cell is(1,1) and the bottom right corner is (n,n).
# Each cell (i,j) of the Matrix contains either 1 or 0. If C( (i*j)^3 ) is odd, Mi,j is 1, otherwise, it's 0.
# Count the total number of ones in the Matrix.
#
#
# 输入
#
# First Line Of the input will contain an integer 'T'- the number of test cases.
# Each of the next 'T' lines consists of an integer 'n'.-denoting the size of the matrix.
#
# Constraints :
#
# 1 ≤ T ≤ 1000
#
# 1 ≤ n ≤ 1000
#
#
# 输出
#
# For each test case, output a single Integer -the taste value fo the dish of size-n*n.
#
#
# 输入样例 1
#
# 1
# 2
# 输出样例 1
#
# 0


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        count = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):

                temp = (i * j) % 7
                temp = (temp * temp * temp) % 7

                if temp == 2 or temp == 3 or temp == 4 or temp == 6 or temp == 0:
                    count += 1

        print(count)
