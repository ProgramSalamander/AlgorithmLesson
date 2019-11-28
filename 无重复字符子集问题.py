# 无重复字符子集问题
# 描述
#
# Mike is a lawyer with the gift of photographic memory. He is so good with it that he can tell you all the numbers on a sheet of paper by having a look at it without any mistake. Mike is also brilliant with subsets so he thought of giving a challange based on his skill and knowledge to Rachael. Mike knows how many subset are possible in an array of N integers. The subsets may or may not have the different sum. The challenge is to find the maximum sum produced by any subset under the condition:
#
# The elements present in the subset should not have any digit in common.
#
# Note: Subset {12, 36, 45} does not have any digit in common and Subset {12, 22, 35} have digits in common.Rachael find it difficult to win the challenge and is asking your help. Can youhelp her out in winning this challenge?
#
#
# 输入
#
# First Line of the input consist of an integer T denoting the number of test cases. Then T test cases follow. Each test case consist of a numbe N denoting the length of the array. Second line of each test case consist of N space separated integers denoting the array elements.
#
# Constraints:
#
# 1 <= T <= 100
#
# 1 <= N <= 100
#
# 1 <= array elements <= 100000
#
#
# 输出
#
# Corresponding to each test case, print output in the new line.
#
#
# 输入样例 1
#
# 1
# 3
# 12 22 35
# 输出样例 1
#
# 57

dp = [0] * 1024


# Function to create mask for every number
def get_binary(u):
    ans = 0
    while u:
        rem = u % 10
        ans |= (1 << rem)
        u //= 10
    return ans


# Recursion for Filling DP array
def recur(u, array, n):
    # Base Condition
    if u == 0:
        return 0

    if dp[u] != -1:
        return dp[u]

    temp = 0
    for i in range(n):
        mask = get_binary(array[i])

        # Recurrence Relation
        if (mask | u) == u:
            dp[u] = max(max(0, dp[u ^ mask]) + array[i], dp[u])

    return dp[u]


# Function to find Maximum Subset Sum
def solve(array, n):
    i = 0

    # Initialize DP array
    while i < (1 << 10):
        dp[i] = -1
        i += 1

    ans = 0

    i = 0
    # Iterate over all possible masks of 10 bit number
    while i < (1 << 10):
        ans = max(ans, recur(i, array, n))

        i += 1

    return ans


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        length = int(input())
        line = input().split(' ')
        arr = [int(i) for i in line]
        print(solve(arr, length))
