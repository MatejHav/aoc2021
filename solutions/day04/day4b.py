import numpy as np

data = np.array(open('4a.txt').read().split('\n'))

numbers = data[0].split(',')

def check(boards):
    res = []
    out = None
    for index, board in enumerate(boards):
        good = False
        for row in board:
            if sum(row) == -5:
                out = board
                good = True
        for i in range(5):
            if board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i] == -5:
                out = board
                good = True
        if not good:
            res.append(board)
    return out, np.array(res)


boards = []
t = []
for line in data[1::]:
    if line == '':
        if len(t) != 0:
            boards.append(t)
        t = []
    else:
        t.append(np.array([int(line[0:2]), int(line[3:5]), int(line[6:8]), int(line[9:11]), int(line[12:14])]))
boards = np.array(boards)
i = 0
others = []
while True:
    current = int(numbers[i])
    i += 1
    boards = np.where(boards != current, boards, -1)
    winner, boards = check(boards)
    if winner is not None:
        others.append(winner.copy())
        if len(boards) == 0:
            print(current * np.sum(winner[winner != -1]))
            break