__author__ = 'Fulvio Corno'


def verify(v):
    if (10 * v['a'] + v['b']) * (10 * v['b'] + v['c']) != 100 * v['d'] + 10 * v['e'] + v['f']:
        return False
    if (10 * v['a'] + v['g']) - (10 * v['a'] + v['a']) != v['h']:
        return False
    if (10 * v['c'] + v['f']) + (10 * v['i'] + v['b']) != (10 * v['g'] + v['d']):
        return False
    if (10 * v['a'] + v['b']) + (10 * v['a'] + v['g']) != (10 * v['c'] + v['f']):
        return False
    if (10 * v['b'] + v['c']) + (10 * v['a'] + v['a']) != (10 * v['i'] + v['b']):
        return False
    if (100 * v['d'] + 10 * v['e'] + v['f']) / (v['h']) != (10 * v['g'] + v['d']):
        return False

    return True


def recurse(keys, v, rest, level):
    if level == 9:
        if verify(v):
            print(v)
        return

    for num in rest:
        v[keys[level]] = num
        rest2 = [r for r in rest if r != num]
        recurse(keys, v, rest2, level + 1)
        v[keys[level]] = None


if __name__ == '__main__':
    v = {}

    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    for k in keys:
        v[k] = None

    rest = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    recurse(keys, v, rest, 0)
