C = int(input())

nm = []

areFriends = []

for i in range(C):
    n, m = list(map(int , input().split()))
    
    nm.append(n)
    
    
    relationship = list(map(int, input().split()))
    
    Friends = [[False] * n for _ in range(n)]

    for j in range(0, len(relationship), 2):
        f1 = relationship[j]
        f2 = relationship[j+1]
        Friends[f1][f2] = True
        Friends[f2][f1] = True
    
    areFriends.append(Friends)
taken = []
for m in range(len(nm)):
    temp = [False] * nm[m]
    taken.append(temp)


def countPairing(taken, k):
    firstFree = -1

    for i in range(len(taken)):
        if not taken[i]:
            firstFree = i
            break
    if firstFree == -1:
        return 1
    ret = 0

    for pairWith in range(firstFree + 1, len(taken)):
        if not taken[pairWith] and areFriends[k][firstFree][pairWith]:

            taken[firstFree] = taken[pairWith] = True
            ret += countPairing(taken, k)
            taken[firstFree] = taken[pairWith] = False

    return ret

answer = []
for k in range(len(nm)):

    temp = countPairing(taken[k], k)
    answer.append(temp)
    
for ele in answer:
    print(ele)