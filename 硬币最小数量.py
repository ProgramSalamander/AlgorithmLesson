# 硬币最小数量
# 描述
#
# Given the list of coins of distinct denominations and total amount of money.
# Output the minimum number of coins required to make up that amount.
# Output -1 if that money cannot be made up using given coins.
# You may assume that there are infinite numbers of coins of each type.
#
#
# 输入
#
# The first line contains 'T' denoting the number of test cases.
# Then follows description of test cases.
# Each cases begins with the two space separated integers 'n' and 'amount' denoting the total number of distinct coins and total amount of money respectively.
# The second line contains N space-separated integers A1, A2, ..., AN denoting the values of coins.
#
# Constraints:1<=T<=30，1<=n<=100，1<=Ai<=1000，1<=amount<=100000
#
#
# 输出
#
# Print the minimum number of coins required to make up that amount or return -1 if it is impossible to make that amount using given coins.
#
#
# 输入样例 1
#
# 2
# 3 11
# 1 2 5
# 2 7
# 2 6
# 输出样例 1
#
# 3
# -1


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        coins_num, amount = [int(i) for i in input().split(' ')]
        # print(coins_num)
        # print(amount)
        coin_values = [int(i) for i in input().split(' ')]
        # print(coin_values)
        coin_values.sort(reverse=True)
        count = 0
        cur_coin = 0
        while amount > 0 and cur_coin < len(coin_values):
            max = coin_values[cur_coin]
            if amount >= max:
                amount -= max
                count += 1
            else:
                cur_coin += 1
        if amount > 0:
            print(-1)
        else:
            print(count)
