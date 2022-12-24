answer =set()

num_testcase = int(input())
board = []
targetWords = []
for i in range(5):
    boardLine = input()
    board.append(boardLine)

N = int(input())

for j in range(N):
    word = input()
    targetWords.append(word)


moveX = [-1, -1, 0, 1 ,1 ,1 , 0, -1]
moveY = [0, -1, -1, -1,0 ,1 ,1 , 1]

def findNext(target, row, column, cur_word, idx):

    string_temp = cur_word

    if cur_word == target:
        answer.add(cur_word)
        return True
    if idx >= len(target):
        return False
    for m in range(len(moveX)):
        r = row +moveY[m]
        c = column + moveX[m]
        if r <= -1 or r >=len(board) or c <= -1 or c >=len(board[0]):
            continue
        elif board[r][c] == target[idx]:

            if idx < (len(target)):

                findNext(target, r, c, cur_word + target[idx], idx + 1)
        else:
            pass


    return False
        

for k in range(len(targetWords)):
    target = targetWords[k]
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == target[0]:
                findNext(target, row, column, target[0], 1)

for i in range(len(targetWords)):
    if targetWords[i] in answer:
        print(targetWords[i], "Yes")
    else:
        print(targetWords[i], "No")