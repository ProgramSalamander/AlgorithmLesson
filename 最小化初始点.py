# 最小化初始点
# 描述
#
# Given a grid with each cell consisting of positive, negative or no points i.e, zero points. We can move across a cell only if we have positive points ( > 0 ). Whenever we pass through a cell, points in that cell are added to our overall points. We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :
# 1.From a cell (i, j) we can move to (i+1, j) or (i, j+1).
#
# 2.We cannot move from (i, j) if your overall points at (i, j) is <= 0.
#
# 3.We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.
#
#
# 输入
#
# The first line contains an integer 'T' denoting the total number of test cases.In each test cases, the first line contains two integer 'R' and 'C' denoting the number of rows and column of array.
# The second line contains the value of the array i.e the grid, in a single line separated by spaces in row major order.
#
# Constraints:
#
# 1 ≤ T ≤ 30
#
# 1 ≤ R,C ≤ 10
#
# -30 ≤ A[R][C] ≤ 30
#
# Input: points[m][n] = { {-2, -3, 3},
# {-5, -10, 1},
# {10, 30, -5}
# };
#
#
# 输出
#
# Print the minimum initial points to reach the bottom right most cell in a separate line.
#
# 7
#
# Explanation:
# 7 is the minimum value to reach destination with
# positive throughout the path. Below is the path.
#
# (0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)
#
# We start from (0, 0) with 7, we reach(0, 1)
# with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)with and finally we have 1 point (we needed
# greater than 0 points at the end).
#
#
# 输入样例 1
#
# 1
# 3 3
# -2 -3 3 -5 -10 1 10 30 -5
# 输出样例 1
#
# 7

if __name__ == '__main__':
    cases_num = int(input())
    for _ in range(cases_num):
        line1 = input().split(' ')
        rows = int(line1[0])
        cols = int(line1[1])
        line2 = input().split(' ')
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = int(line2[i * rows + j])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        if grid[rows - 1][cols - 1] > 0:
            dp[rows - 1][cols - 1] = 1
        else:
            dp[rows - 1][cols - 1] = abs(grid[rows - 1][cols - 1]) + 1

        for i in range(rows - 2, -1, -1):
            dp[i][cols - 1] = max(dp[i + 1][cols - 1] - grid[i][cols - 1], 1)
        for i in range(cols - 2, -1, -1):
            dp[rows - 1][i] = max(dp[rows - 1][i + 1] - grid[rows - 1][i], 1)

        for i in range(rows - 1, 0, -1):
            for j in range(cols - 1, 0, -1):
                dp[i - 1][j - 1] = max(min(dp[i][j - 1], dp[i - 1][j]) - grid[i - 1][j - 1], 1)
        min_points = dp[0][0]
        print(min_points)
