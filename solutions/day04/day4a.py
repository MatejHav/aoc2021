import numpy as np

data = np.array(open('4a.txt').read().split('\n'))

numbers = data[0].split(',')

def check(boards):
    for board in boards:
        for row in board:
            if sum(row) == -5:
                return board
        for i in range(5):
            if board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i] == -5:
                return board
    return None


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
    winner = check(boards)
    if winner is not None:
        print(current * np.sum(winner[winner != -1]))
        break



