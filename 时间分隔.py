if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        trains_num = int(input())
        arrival_times = [int(_) for _ in input().split(' ')]
        departure_times = [int(_) for _ in input().split(' ')]
        times = []
        for i in range(trains_num):
            times.append(arrival_times[i])
            times.append(departure_times[i])
        sorted_times = sorted(times)
        count = 0
        max_count = count
        for i in sorted_times:
            try:
                arrival_times.index(i)
            except ValueError:
                pass
            else:
                count += 1
                max_count = max(max_count, count)
                arrival_times.remove(i)
            try:
                departure_times.index(i)
            except ValueError:
                pass
            else:
                count -= 1
                departure_times.remove(i)
        print(max_count)
