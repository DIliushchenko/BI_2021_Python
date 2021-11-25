import numpy as np

# create array by 3 different ways
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.arange(1, 11)
c = np.random.rand(10)


def matrix_multiplication(A, B):
    res = np.zeros((np.shape(A)[0], np.shape(B)[1]))

    for i in range(np.shape(A)[0]):

        for j in range(np.shape(B)[1]):
                res[i][j] += np.sum(A[i, :] * B[:, j])

    return res


def multiplication_check(mat_list):
    res = np.zeros((np.shape(mat_list[0])[0], np.shape(mat_list[0])[1]))
    for i in range(1, len(mat_list)):
        if np.shape(res)[1] != np.shape(mat_list[i])[0]:
            return False
        else:
            res = np.zeros((np.shape(res)[0], np.shape(mat_list[i])[1]))
    return True


def multiply_matrices(mat_list):
    if multiplication_check(mat_list):
        for i in range(1, len(mat_list)):
            if i == 1:
                res = matrix_multiplication(mat_list[0], mat_list[1])
            else:
                res = matrix_multiplication(res, mat_list[i])
        return res
    else:
        return None


def compute_2d_distance(a1, a2):

    x = (a2[0]-a1[0]) ** 2
    y = (a2[1]-a1[1]) ** 2
    return (x + y) ** 0.5


def compute_multidimensional_distance(a1, a2):

    if len(a1) != len(a2):
        return None
    else:
        res = 0
        for i in range(len(a1)):
            res += (a2[i]-a1[i]) ** 2
        return res ** 0.5


def compute_pair_distances(matrix):

    res = np.zeros((np.shape(matrix)[0], np.shape(matrix)[0]))

    for i in range(np.shape(matrix)[0]):

        for j in range(np.shape(matrix)[0]):

            res[i][j] = compute_multidimensional_distance(matrix[i], matrix[j])

    return res
