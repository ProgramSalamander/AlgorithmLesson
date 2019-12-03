# 时间与收益
# 描述
#
# Given a set of n jobs where each job i has a deadline and profit associated to it.
# Each job takes 1 unit of time to complete and only one job can be scheduled at a time.
# We earn the profit if and only if the job is completed by its deadline.
# The task is to find the maximum profit and the number of jobs done.
#
#
# 输入
#
# The first line of input contains an integer T denoting the number of test cases.
# Each test case consist of an integer N denoting the number of jobs and the next line consist of Job id, Deadline and the Profit associated to that Job.
#
# Constraints:1<=T<=100，1<=N<=100，1<=Deadline<=100，1<=Profit<=500
#
#
# 输出
#
# Output the number of jobs done and the maximum profit.
#
#
# 输入样例 1
#
# 2
# 4
# 1 4 20 2 1 10 3 1 40 4 1 30
# 5
# 1 2 100 2 1 19 3 2 27 4 1 25 5 1 15
# 输出样例 1
#
# 2 60
# 2 127

if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        jobs_num = int(input())
        line = [int(_) for _ in input().split(' ')]
        jobs = [(line[i * 3 + 1], line[i * 3 + 2]) for i in range(jobs_num)]
        jobs.sort(reverse=True)
        # print(jobs)
        jobs_count = 0
        profit = 0
        max_time = jobs[0][0]
        for _ in range(jobs_num):
            t = jobs[0][0]
            if t == 0:
                break
            profit += jobs[0][1]
            jobs_count += 1
            jobs.pop(0)
            jobs = list(map(lambda x: (x[0] - 1, x[1]) if x[0] == t else (x[0], x[1]), jobs))
            # print(jobs)
        print('%d %d'%(jobs_count, profit))
