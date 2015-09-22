# initial commit and pull request
class ShapeException(Exception):
    pass


def dot(vec1, vec2):
    shape_checker(vec1, vec2)
    values = []
    for index, value in enumerate(vec1):
        values.append(value * vec2[index])
    return sum(values)


def magnitude(vector):
    return dot(vector, vector) ** 0.5


def shape(vecmat):
    num_rows = len(vecmat)
    for row in vecmat:
        if type(row) == list:
            num_cols = len(row)
            return num_rows, num_cols
        else:
            return num_rows,


def shape_checker(matrix1, matrix2):
    if shape(matrix1) != shape(matrix2):
        raise ShapeException()


def vector_add(vec1, vec2):
    shape_checker(vec1, vec2)
    added_vector = []
    for index, value in enumerate(vec1):
        added_vector.append(vec1[index] + vec2[index])
    return added_vector


def vector_sub(vec1, vec2):
    shape_checker(vec1, vec2)
    subtract_vector = []
    for index, value in enumerate(vec1):
        subtract_vector.append(vec1[index] - vec2[index])
    return subtract_vector


def vector_sum(*vecs):
    vecs = list(vecs)
    summed_vec = [0 for num in range(len(vecs[0]))]
    for vec in vecs:
        if len(vec) != len(summed_vec):
            raise ShapeException()
    for vec in vecs:
        for index, value in enumerate(vec):
            summed_vec[index] += value
    return summed_vec


def vector_multiply(vector, scalar):
    mult_vector = []
    for row in vector:
        mult_vector.append(row * scalar)
    return mult_vector


def vector_mean(*vecs):
    mean_vector = []
    total_vecs = len(list(vecs))
    summed_vec = vector_sum(*vecs)
    for vec in summed_vec:
        mean_vector.append(vec/total_vecs)
    return mean_vector


def matrix_row(matrix, row):
    return matrix[row]


def matrix_col(matrix, col):
    col_list = []
    for row in matrix:
        col_list.append(row[col])
    return col_list


def matrix_scalar_multiply():
    pass


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass
