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
