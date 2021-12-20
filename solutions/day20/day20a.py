import numpy as np

data = np.array(open('20a.txt').read().split('\n'))

ref = data[0]
width = 101
height = 101
image = np.zeros((width, height), dtype=np.int64)


def determine(args):
    number = int('0b' + ''.join([''.join([str(b) for b in a]) for a in args]), 2)
    return 1 if ref[number] == '#' else 0


for j, line in enumerate(data[1:]):
    for index, letter in enumerate(line):
        image[j, index] = 1 if letter == '#' else 0


def convolve(image, pad=0):
    img = np.zeros((image.shape[0] + 10, image.shape[1] + 10), dtype=np.int64)
    if pad == 1:
        img = np.ones((image.shape[0] + 10, image.shape[1] + 10), dtype=np.int64)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            img[5 + x, 5 + y] = image[x, y]

    res = np.zeros(img.shape, dtype=np.int64)
    if pad == 0:
        res = np.ones(img.shape, dtype=np.int64)
    for x in range(1, img.shape[0] - 1):
        for y in range(1, img.shape[1] - 1):
            res[x, y] = determine(img[x - 1:x + 2, y - 1:y + 2])
    return res


for i in range(25):
    image = convolve(image)
    image = convolve(image, 1)
    print(np.sum(image))
