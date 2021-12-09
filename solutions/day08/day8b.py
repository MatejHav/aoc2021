import numpy as np

data = np.array(open('8a.txt').read().split('\n'))

out = []
for line in data:
    inp = line.split('|')[0].split(' ')
    o = line.split('|')[1].split(' ')
    sorted(inp, key=len)
    con = {}
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        con[i] = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    for i in inp:
        s = {j for j in i}
        if len(i) == 2:
            two.append(i)
            con['c'] = con['c'].intersection(s)
            con['f'] = con['f'].intersection(s)
        if len(i) == 3:
            three.append(i)
            con['a'] = con['a'].intersection(s)
            con['c'] = con['c'].intersection(s)
            con['f'] = con['f'].intersection(s)
        if len(i) == 4:
            four.append(i)
            con['b'] = con['b'].intersection(s)
            con['d'] = con['d'].intersection(s)
            con['c'] = con['c'].intersection(s)
            con['f'] = con['f'].intersection(s)
        if len(i) == 5:
            five.append(i)
        if len(i) == 6:
            six.append(i)
        if len(i) == 7:
            seven.append(i)

    temp = {letter for letter in three[0]}
    for f in five:
        temp = temp.intersection({letter for letter in f})
    assert len(temp) == 1
    con['a'] = list(temp)[0]

    temp = {letter for letter in six[0]}
    for s in six:
        temp = temp.intersection({letter for letter in s})
    for f in five:
        temp = temp.intersection({letter for letter in f})
    temp.remove(con['a'])
    assert len(temp) == 1
    con['g'] = list(temp)[0]

    temp = {letter for letter in two[0]}
    for f in six:
        temp = temp.intersection({letter for letter in f})
    assert len(temp) == 1
    con['f'] = list(temp)[0]
    con['c'].remove(con['f'])
    con['c'] = list(con['c'])[0]

    temp = {letter for letter in four[0]}
    for s in six:
        temp = temp.intersection({letter for letter in s})
    temp.remove(con['f'])
    assert len(temp) == 1
    con['b'] = list(temp)[0]

    con['d'].remove(con['b'])
    con['d'].remove(con['c'])
    con['d'].remove(con['f'])
    con['d'] = list(con['d'])[0]

    con['e'].remove(con['a'])
    con['e'].remove(con['b'])
    con['e'].remove(con['c'])
    con['e'].remove(con['d'])
    con['e'].remove(con['f'])
    con['e'].remove(con['g'])
    con['e'] = list(con['e'])[0]

    trans = {}
    for key in con.keys():
        trans[con[key]] = key

    truth = {
        'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4,
        'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9
    }
    t = []
    for i in o[1:]:
        proper = ''
        for letter in i:
            proper += trans[letter]
        proper = ''.join(sorted(proper))
        t.append(str(truth[proper]))
    out.append(int(''.join(t)))
print(sum(out))

    
    
                    







