import numpy as np

data = np.array(open('10b.txt').read().split('\n'))

points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

trans = {
    '(' : ')',
    '{' : '}',
    '[' : ']',
    '<' : '>'
}


score = 0

for line in data:
    stack = []
    for letter in line:
        if letter in [')', ']', '}', '>']:
            if letter != stack.pop():
                score += points[letter]
                break
        else:
            stack.append(trans[letter])
print(score)