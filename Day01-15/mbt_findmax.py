def find_max(lst):
    try:
        max_num = lst[0]
        for i in lst:
            if i > max_num:
                max_num = i
    except TypeError:
        return None
    except IndexError:
        return None
    else:
        return max_num


cases = [
    [[1, 2, 3, 4, 5], 5],
    [[-1, 0, 1], 5],
    [[-1, -2, -3, -4, -5], -1],
    [[2, 2, 2, 2], 2],
    [['a', 'b', 'c'], 'c'],
    [['a', 1, 2, 3], 3],
    [[], None],
    [[3.14, 1.73, 2 + 2j], None]
]

for case in cases:
    print(find_max(case[0]) == case[1], find_max(case[0]))
