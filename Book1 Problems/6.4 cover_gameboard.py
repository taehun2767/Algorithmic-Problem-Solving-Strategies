C = int(input())
totalBoard = []  # 전체 보드 담은 리스트
for i in range(C):
    H, W = list(map(int, input().split()))
    
    board = []
    
    for j in range(H):
        layer = input()
        boolBoard = [False if layer[:W][_] == "#" else True for _ in range(len(layer[:W])) ]
        board.append(boolBoard)
    totalBoard.append(board)





location = [[[0, 0], [0, 1], [1, 0]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, -1]], [[0, 0], [1, 0], [1, 1]]]

def coverBoard(board):
    r, c = -1, -1

    rowLen =len(board)
    colLen = len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == True:
                r = i
                c = j

                break
        if r != -1:
                break
    if r == -1 and c == -1:
        return 1

    ret = 0
    
    for ele in location:
        cover = True
        for dr, dc in ele:

            nr = r + dr
            nc = c + dc

            if nr >= rowLen or nr < 0 or nc >= colLen or nc < 0:
                cover = False
                break
            elif not board[nr][nc]:
                cover = False
                break

        if cover:

            for dr, dc in ele:
                nr = r + dr
                nc = c + dc
                board[nr][nc] = False
            ret += coverBoard(board)
            for dr, dc in ele:
                nr = r + dr
                nc = c + dc
                board[nr][nc] = True
          
    return ret

for k in range(len(totalBoard)):
    answer = coverBoard(totalBoard[k])
    print(answer)
