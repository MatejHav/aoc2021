import numpy as np

data = np.array(open('10b.txt').read().split('\n'))

points = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

trans = {
    '(' : ')',
    '{' : '}',
    '[' : ']',
    '<' : '>'
}


scores = []

for line in data:
    score = 0
    stack = []
    complete = True
    for letter in line:
        if letter in [')', ']', '}', '>']:
            if letter != stack.pop():
                complete = False
                break
        else:
            stack.append(trans[letter])
    while len(stack) > 0 and complete:
        last = stack.pop()
        score *= 5
        score += points[last]
    if score != 0:
        scores.append(score)

print(np.median(scores))