import sys
if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        houses_num, pipes_num = [int(_) for _ in input().split(' ')]
        tanks = []
        taps = []
        froms = []
        tos = []
        diameters = []
        for _ in range(pipes_num):
            from_house, to_house, diameter = [int(_) for _ in input().split(' ')]
            froms.append(from_house)
            tos.append(to_house)
            diameters.append(diameter)
        for i in range(1, houses_num + 1):
            if i in froms and i in tos:
                pass
            elif i in froms:
                tanks.append(i)
            elif i in tos:
                taps.append(i)
        # print(tanks)
        # print(taps)
        print(len(tanks))
        for tank in tanks:
            cur = tank
            min_diameter = sys.maxsize
            while cur in froms:
                idx = froms.index(cur)
                min_diameter = min(diameters[idx], min_diameter)
                cur = tos[froms.index(cur)]
            print('%d %d %d'%(tank, cur, min_diameter))