import numpy as np

arr = np.array(open('1.txt').read().split('\n')).astype(np.int64)
temp = {}
for i in range(0, len(arr)):
    if i + 1 < len(arr) and i + 2 < len(arr):
        arr[i] += arr[i + 1] + arr[i + 2]
    elif i + 2 >= len(arr) and i + 1 < len(arr):
        arr[i] += arr[i + 1]

res = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        res += 1
print(res)