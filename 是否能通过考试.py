# 是否能通过考试
# 描述
# 小张想要通过明天的考试。他知道考题的分值分布，也知道考试中要拿到每一个题目需要耗费的时间。
# 假设考试时长为h，共n个题目，需要拿到p分才能通过考试。
# 现在已知每个考题的得分与耗时，请你判断小张能否通过合理安排时间，而通过考试，并给出通过考试的最短时间。
# 输入
# 输入第一行为测试用例个数.每一个用例有若干行，第一行为任务数量n、考试时常h、通过分数p，下面的n行是每一个题目的耗时和得分。所有数值用空格分开。
# 输出
# 对每一个用例输出一行，如果能够通过考试，则输出“YES”和消耗最短时间，用空格隔开。 否则，输出“NO”。
# 输入样例 1
# 1
# 5 40 21
# 12 10
# 16 10
# 20 10
# 24 10
# 8 3
# 输出样例 1
# YES 36

if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        line1 = input().split(' ')
        question_num = int(line1[0])
        time_limit = int(line1[1])
        score_limit = int(line1[2])
        question_times = []
        question_scores = []
        for i in range(question_num):
            line = input().split(' ')
            question_times.append(int(line[0]))
            question_scores.append(int(line[1]))

        dp = [[0 for _ in range(time_limit + 1)] for _ in range(question_num)]
        for i in range(time_limit + 1):
            if question_times[0] <= i:
                dp[0][i] = question_scores[0]
            else:
                dp[0][i] = 0
        for i in range(1, question_num):
            for j in range(time_limit + 1):
                dp[i][j] = dp[i - 1][j]
                if question_times[i] <= j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - question_times[i]] + question_scores[i])
        find = False
        min_time = 0
        for i in range(question_num):
            for j in range(time_limit):
                if dp[i][j] >= score_limit:
                    find = True
                    min_time = j
                    break
            if find:
                break
        if find:
            print('YES %d'%min_time)
        else:
            print('NO')
