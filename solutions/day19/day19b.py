import numpy as np

data = np.array(open('19a.txt').read().split('\n'))

scanners = []
t = []
for line in data:
    if 'scanner' in line or line == '':
        if len(t) > 0:
            scanners.append(t)
        t = []
        continue
    t.append(np.array(line.split(',')).astype(np.int64))

ref = scanners[0]
ref_set = set()
for beam in ref:
    ref_set.add(str(beam))
scanner_pos = {0: [0, 0, 0]}

identities = [np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
              np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]),
              np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
              np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),

              np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
              np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
              np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]]),
              np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]),

              np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
              np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]),
              np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]]),
              np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]),

              np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
              np.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]]),
              np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
              np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]]),

              np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
              np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]]),
              np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]]),
              np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]]),

              np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
              np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]]),
              np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]]),
              np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]])]

for i in range(5):
    keys = [k for k in scanner_pos]
    keys = sorted(keys)
    print(keys)
    for index, scanner in enumerate(scanners[1:]):
        if index + 1 in scanner_pos:
            continue
        found = False
        for identity in identities:
            positions = {}
            for beam in scanner:
                for ref_beam in ref:
                    rot_beam = np.matmul(identity, beam)
                    position = np.array(ref_beam - rot_beam).astype(np.int64)
                    if f'{position[0]},{position[1]},{position[2]}' not in positions:
                        positions[f'{position[0]},{position[1]},{position[2]}'] = 0
                    positions[f'{position[0]},{position[1]},{position[2]}'] += 1
            temp = np.array([v for v in positions.values()])
            if len(temp[temp >= 12]) == 1:
                for position in positions:
                    if positions[position] >= 12:
                        scanner_pos[index + 1] = np.array(position.split(',')).astype(np.int64)
                        for beam in scanners[index + 1]:
                            rot_beam = np.matmul(identity, beam)
                            if str(scanner_pos[index + 1] + rot_beam) not in ref_set:
                                ref_set.add(str(scanner_pos[index + 1] + rot_beam))
                                ref.append(scanner_pos[index + 1] + rot_beam)
                        found = True
                        break
            if found:
                break

ref = sorted(ref, key=lambda x: x[0])
# print('### POINTS ###')
# for point in ref:
#     print(point)
print(len(ref))

dist = []
for scan in scanner_pos:
    for scan2 in scanner_pos:
        pos1 = scanner_pos[scan]
        pos2 = scanner_pos[scan2]
        dist.append(abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2]))
print(np.max(dist))