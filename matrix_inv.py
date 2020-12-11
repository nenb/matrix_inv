def submtrx(m, i, j):
    return [col[:j] + col[j + 1 :] for col in m[:i] + m[i + 1 :]]


def det(m):
    if len(m) == 1:
        return m[0][0]
    else:
        d = 0
        for idx, value in enumerate(m[0]):
            d += ((-1) ** idx) * value * det(submtrx(m, 0, idx))
        return d


def cofactor(m, i, j):
    if len(m) == 1:
        return 1
    else:
        return ((-1) ** (i + j)) * det(submtrx(m, i, j))


def adj(m):
    return [[cofactor(m, i, j) for i in range(len(m))] for j in range(len(m))]


def inv(m):
    try:
        d = det(m)
        return [[a / d for a in row] for row in adj(m)]
    except ZeroDivisionError:
        print("Determinant is zero, matrix has no inverse.")


def add_square(x, y):
    return [[x[i][j] + y[i][j] for j in range(len(x))] for i in range(len(x))]


def transpose_square(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m))]


def dot_prod(x, y):
    return sum(i[0] * i[1] for i in zip(x, y))


def mult_square(x, y):
    y_t = transpose_square(y)
    return [[dot_prod(x[i], y_t[j]) for j in range(len(x))] for i in range(len(x))]


def ident(dim):
    return [[0.0 if i != j else 1.0 for j in range(dim)] for i in range(dim)]
