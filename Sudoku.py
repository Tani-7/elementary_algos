def reduce(matrix):
    changed = True
    groups = getGroups(matrix)

    while changed:
        changed = reduceGroups(groups)
