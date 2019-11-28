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
