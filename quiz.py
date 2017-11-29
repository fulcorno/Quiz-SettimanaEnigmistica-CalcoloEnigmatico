__author__ = 'Fulvio Corno'


def verify(v):

    n11 = v['b']
    n12 = (10*v['a']+v['i'])
    n13 = 100 * v['e'] + 10 * v['g'] + v['f']
    n21 = 10*v['e']+v['f']
    n22 = 10*v['i']+v['d']
    n23 = 10 * v['a'] + v['f']
    n31 = 100*v['i']+10*v['e']+v['h']
    n32 = 10*v['b']+v['i']
    n33 = 100*v['e']+10*v['c']+v['d']

    if n11 * n12 != n13:
        return False
    if n21 + n22 != n23:
        return False
    if n31 + n32 != n33:
        return False

    if n11 * n21 != n31:
        return False
    if n12 + n22 != n32:
        return False
    if n13 - n23 != n33:
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
