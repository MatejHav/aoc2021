import numpy as np

data = np.array(open('16a.txt').read().split('\n'))[0]

versions = []
j = 0
h = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def translate(data):
    out = ''
    for letter in data:
        out += h[letter]
    return out

inp = translate(data)

def value_packet(inp):
    number = ''
    go = True
    i = 6
    while go:
        temp = inp[i: i + 5]
        if temp[0] == '0':
            go = False

        number += temp[1:5]
        i += 5

    return int('0b' + number, 2), inp[i:]


def operator_packet(inp):
    numbers = []
    if inp[6] == '0':
        I = 15
        length = int('0b' + inp[7: 7 + I], 2)
        inp = inp[7 + I:]
        while length > 0:
            t = len(inp)
            number, inp = solve(inp)
            length -= abs(len(inp) - t)
            numbers.append(number)
    else:
        I = 11
        length = int('0b' + inp[7: 7 + I], 2)
        inp = inp[7 + I:]
        for i in range(length):
            number, inp = solve(inp)
            numbers.append(number)
    return numbers, inp


def solve(inp):
    if len(inp) == 0:
        return inp

    id = int('0b' + inp[3:6], 2)
    version = int('0b' + inp[0:3], 2)
    versions.append(version)
    result = 0
    if id == 4:
        result, inp = value_packet(inp)
    if id == 0:
        numbers, inp = operator_packet(inp)
        result = sum(numbers)
    if id == 1:
        numbers, inp = operator_packet(inp)
        result = 1
        for p in numbers:
            result *= p
    if id == 2:
        numbers, inp = operator_packet(inp)
        result = np.min(numbers)
    if id == 3:
        numbers, inp = operator_packet(inp)
        result = np.max(numbers)
    if id == 5:
        numbers, inp = operator_packet(inp)
        result = 1 if numbers[0] > numbers[1] else 0
    if id == 6:
        numbers, inp = operator_packet(inp)
        result = 1 if numbers[0] < numbers[1] else 0
    if id == 7:
        numbers, inp = operator_packet(inp)
        result = 1 if numbers[0] == numbers[1] else 0
    return result, inp


solve(inp)
print(sum(versions))
