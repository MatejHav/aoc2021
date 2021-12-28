import numpy as np
import ast

data = np.array(open('18b.txt').read().split('\n'))


class Node:
    def __init__(self, children):
        self.value = None
        if isinstance(children, int):
            self.value = children
        else:
            if isinstance(children[0], Node):
                self.left = children[0]
                self.right = children[1]
            else:
                self.left = Node(children[0])
                self.right = Node(children[1])

    def end(self):
        return self.value is not None

    def __str__(self):
        if self.end():
            return str(self.value)
        return f'[{self.left}, {self.right}]'


def add(last, two):
    pairs = Node([last, two])
    changed = True
    while changed:
        changed2 = split(pairs)
        # print(f'Split:\t\t {pairs}')
        changed1 = check_explode(pairs, 0)[-1]
        # print(f'Explosion:\t {pairs}')
        changed = changed1 or changed2
    return pairs


def explode(pair):
    return pair.left.value, pair.right.value



def update(node, number, style):
    if node.end():
        node.value += number
    else:
        update(node.left if style == 'l' else node.right, number, style)


def check_explode(node, depth):
    if node.end():
        return 0, 0, False, False
    if depth >= 4:
        left, right = explode(node)
        return left, right, True, True

    leftR = 0
    rightR = 0
    changed = False
    for index, n in enumerate([node.left, node.right]):
        left, right, ex, change = check_explode(n, depth + 1)
        if ex:
            n.value = 0
            n.left = None
            n.right = None

        if index == 0:
            leftR = left
        else:
            update(node.left, left, 'r')
        if index == 1:
            rightR = right
        else:
            update(node.right, right, 'l')
        if change:
            return leftR, rightR, False, True
        changed = change or changed

    return leftR, rightR, False, changed


def split(node):
    if node.end():
        if node.value >= 10:
            node.left = Node(node.value // 2)
            node.right = Node(node.value // 2 + node.value % 2)
            node.value = None
            return True
        return False
    else:
        one = split(node.left)
        if one:
            return True
        two = split(node.right)
        return one or two


def magnitude(node):
    if node.end():
        return node.value
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


first = Node(ast.literal_eval(data[0]))
for line in data[1:]:
    second = Node(ast.literal_eval(line))
    first = add(first, second)
    print(first)
print(magnitude(first))
