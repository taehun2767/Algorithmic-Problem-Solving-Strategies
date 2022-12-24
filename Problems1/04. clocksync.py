import sys
sys.setrecursionlimit(10**7)
INF = 9999
testCase = int(input())
clocklist =[]

for i in range(testCase):
    temp = list(map(int , input().split()))
    clocklist.append(temp)

switch = [ [0, 1, 2], [3, 7 ,9 ,11], [4, 10, 14, 15], [0, 4, 5, 6, 7], [6, 7, 8, 10, 12],
          [0, 2, 14, 15], [3, 14, 15], [4, 5, 7, 14, 15], [1, 2, 3, 4, 5], [3, 4, 5, 9, 13] ]

def areAligned(case_num):
    for i in range(len(clocklist[case_num])):
        if clocklist[case_num][i] != 12:
            return False
    else : return True
    
def push(case_num,switch_num):
    num = len(switch[switch_num])
    clock = clocklist[case_num]
    s = switch[switch_num]
    for j in range(num):
        clock[s[j]] += 3
        if clock[s[j]] == 15:
            clock[s[j]] = 3

def solve(case_num, switch_num):
    if switch_num == 10 and areAligned(case_num):
        return 0
    elif switch_num == 10 and not areAligned(case_num):
        return INF
    ret = INF
    for cnt in range(4):
        ret = min(ret, cnt + solve(case_num, switch_num + 1))
        push(case_num, switch_num)
    return ret



for i in range(testCase):
    ans = solve(i, 0)
    print(ans)

    