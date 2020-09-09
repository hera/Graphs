def earliest_ancestor(ancestors, starting_vertex):

    vertices = {}

    for a in ancestors:
        parent = a[0]
        child = a[1]

        if child not in vertices:
            vertices[child] = []

        vertices[child].append(parent)
    
    if starting_vertex not in vertices:
        return -1
    
    s = []
    paths = []

    s.append([starting_vertex])
    paths.append([starting_vertex])

    while len(s) > 0:
        popped = s.pop()
        last = popped[-1]
        
        if last in vertices:
            for n in vertices[last]:
                s.append(popped + [n])
                paths.append(popped + [n])

    max_length = 0

    for p in paths:
        if len(p) > max_length:
            max_length = len(p)

    earliest = []

    for p in paths:
        if len(p) == max_length:
            earliest.append(p[-1])
    
    return min(earliest)


if __name__ == "__main__":
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(ancestors, 6))