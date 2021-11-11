import numpy as np

# create array by 3 different ways
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.arange(1, 11)
c = np.random.rand(10)


def matrix_multiplication(A, B):
    res = np.zeros((np.shape(A)[0], np.shape(B)[1]))

    for i in range(np.shape(A)[0]):

        for j in range(np.shape(B)[1]):

            for k in range(np.shape(B)[0]):
                res[i][j] += A[i][k] * B[k][j]

    return res


def multiplication_check(mat_list):
    for i in range(1, len(mat_list)):
        if i == 1:
            if np.shape(mat_list[0])[1] != np.shape(mat_list[1])[0]:
                return False
            else:
                res = np.zeros((np.shape(mat_list[0])[0], np.shape(mat_list[1])[1]), dtype=int)
        else:
            if np.shape(res)[1] != np.shape(mat_list[i])[0]:
                return False
            else:
                res = np.zeros((np.shape(res)[0], np.shape(mat_list[i])[1]), dtype=int)

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
