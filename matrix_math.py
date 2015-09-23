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


def matrix_add(matrix1, matrix2):
    shape_checker(matrix1, matrix2)
    added_matrix = []
    for index, value in enumerate(matrix1):
        added_matrix.append(vector_add(matrix1[index], matrix2[index]))
    return added_matrix


def matrix_sub(matrix1, matrix2):
    shape_checker(matrix1, matrix2)
    subtract_matrix = []
    for index, value in enumerate(matrix1):
        subtract_matrix.append(vector_sub(matrix1[index], matrix2[index]))
    return subtract_matrix


def matrix_scalar_multiply(matrix, scalar):
    output_matrix = []
    for row in matrix:
        output_row = []
        for col in row:
            output_row.append(col * scalar)
        output_matrix.append(output_row)
    return output_matrix


def matrix_vector_multiply(matrix, vector):
    if len(matrix_row(matrix, 0)) != len(vector):
        raise ShapeException()
    output_vector = []
    for row in matrix:
        output_row = []
        for index, value in enumerate(row):
            output_row.append(value * vector[index])
        output_vector.append(sum(output_row))
    return output_vector


def matrix_matrix_multiply():
    def matrix_matrix_multiply(matrix1, matrix2):
    if len(matrix_row(matrix1, 0)) != len(matrix_col(matrix2, 0)):
        raise ShapeException()
    output_matrix_final = []
    for r in matrix1:
        output_matrix = []
        for row_index, row in enumerate(matrix2):
            output_row = []
            output_matrix.append(vector_multiply(row, r[row_index]))
        output_matrix_final.append(output_matrix)
    return output_matrix_final
    pass
