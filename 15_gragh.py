fr_info = {
    'su': ['jo', 'ju', 'mi'],
    'jo': ['su', 'ju'],
    'ju': ['jo', 'su', 'mi', 'ma'],
    'mi': ['su', 'ju'],
    'ma': ['ju', 'ki'],
    'ki': ['ma'],
    'to': ['je'],
    'je': ['to']
}


def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)


print_all_friends(fr_info, 'su')
print()
print_all_friends(fr_info, 'je')
