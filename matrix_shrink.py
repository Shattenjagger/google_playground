matrix = [
    [20, 80, 60, 70],
    [11, 90, 22, 44],
    [33, 99, 49, 88]
]


def compress(A):
    rows = len(A)

    unsorted_array = []
    positions = {}
    for i in range(rows):
        for j in range(len(A[i])):
            unsorted_array.append(A[i][j])
            positions[A[i][j]] = (i, j)

    sorted_array = sorted(unsorted_array)

    for i in range(len(sorted_array)):
        pos = positions[sorted_array[i]]
        A[pos[0]][pos[1]] = i + 1

    N = len(sorted_array)

    for n in range(1, N + 1):

        has_changes = False
        for i in range(rows):
            for j in range(len(A[i])):
                if A[i][j] < n:
                    continue
                # for every number in row bigger than N - 1 and lesser than N
                smallest_in_row = True
                smallest_in_column = True

                for ix in range(rows):
                    if ix == i:
                        continue
                    if A[ix][j] < n:
                        continue
                    if A[i][j] > A[ix][j]:
                        smallest_in_column = False

                for jx in range(len(A[i])):
                    if jx == j:
                        continue
                    if A[i][jx] < n:
                        continue
                    if A[i][j] > A[i][jx]:
                        smallest_in_row = False

                if smallest_in_column and smallest_in_row:
                    has_changes = True
                    A[i][j] = n

        if not has_changes:
            break

    return A


print(compress(matrix))
