# Given a matrix with different colors find out size of biggest figure

MATRIX = [
    [0, 0, 2, 1],
    [0, 1, 3, 1],
    [2, 1, 1, 1]
]


class Figure:
    def __init__(self, index, color):
        self.color = color
        self.index = index
        self.size = 1


def solution(M):
    # Some edge cases
    if len(M) == 0:
        return 0

    if len(M[0]) == 0:
        return 0

    rows = len(M)
    columns = len(M[0])

    figures = [None] * columns

    result = 0

    for r in range(rows):
        row = M[r]

        for cell_idx in range(columns):
            if cell_idx == 0:  # There is no cells in left
                if figures[cell_idx] is not None and row[cell_idx] == figures[cell_idx].color:
                    # There is a figure above
                    figures[cell_idx].size += 1
                    if figures[cell_idx].size > result:
                        result = figures[cell_idx].size
                else:
                    figures[cell_idx] = Figure(cell_idx, row[cell_idx])
                    if figures[cell_idx].size > result:
                        result = figures[cell_idx].size
            else:
                if row[cell_idx] == row[cell_idx - 1]:
                    # Same color on the left
                    candidate = figures[cell_idx - 1]
                    candidate.size += 1

                    # Let's check what's going on on the top
                    if figures[cell_idx] is not None and row[cell_idx] == figures[cell_idx].color:
                        # There is a figure above with same color
                        # Let's check is it same figure

                        if id(candidate) == id(figures[cell_idx]):
                            # It's the same so just placing the candidate
                            figures[cell_idx] = candidate
                            if figures[cell_idx].size > result:
                                result = figures[cell_idx].size
                        else:
                            # Not the same figure, but with same color. Need to combine them
                            candidate.size += figures[cell_idx].size
                            figures[cell_idx] = candidate
                            if figures[cell_idx].size > result:
                                result = figures[cell_idx].size
                    else:
                        # There is no figure above, or with different color
                        figures[cell_idx] = candidate
                        if figures[cell_idx].size > result:
                            result = figures[cell_idx].size
                else:
                    # The color on left is different. Let's check the top
                    if figures[cell_idx] is not None and row[cell_idx] == figures[cell_idx].color:
                        # There is a figure above
                        figures[cell_idx].size += 1
                        if figures[cell_idx].size > result:
                            result = figures[cell_idx].size
                    else:
                        figures[cell_idx] = Figure(cell_idx, row[cell_idx])
                        if figures[cell_idx].size > result:
                            result = figures[cell_idx].size

    return result


res = solution(MATRIX)
print("The biggest figure has a size: %s" % res)
