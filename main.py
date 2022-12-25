from multiprocessing import Process


def element(i, j):
    # get a middle dimension
    N = len(matrix1[0]) or len(matrix2)
    matrix3[i][j] = sum([matrix1[i][k] * matrix2[k][j] for k in range(N)])
    write_matrix("matrix_result.txt", matrix3, i, j)
    return matrix3

def write_matrix(filename, matrix, i, j):
    with open(filename, "a") as f:
        if i == j == 0:
            f.write(str(matrix3[i][j]) + " ")
        elif j == 0:
            f.write("\n" + str(matrix3[i][j]) + " ")
        else:
            f.write(str(matrix3[i][j]) + " ")

def read_matrix(filename):
    with open(filename, "r") as f:
        return [[int(i) for i in line.split(" ")] for line in f]


def write_matrix_input(filename, matrix):
    with open(filename, "w") as f:
        for row in matrix:
            f.write(" ".join([str(a) for a in row]) + "\n")

# matrix1 = [[1, 2, 4], [3, 4, 5]]
# matrix2 = [[2, 9], [1, 2], [9, 0]]
# write_matrix_input("matrix1.txt", matrix1)
# write_matrix_input("matrix2.txt", matrix2)

matrix1 = read_matrix("matrix1.txt")
matrix2 = read_matrix("matrix2.txt")
matrix3 = [[0]*len(matrix1) for i in range(len(matrix1))]


if __name__ == "__main__":
    res = 0
    l_m1 = len(matrix1)
    procs = []

    cells = []
    for i in range(l_m1):
        for j in range(l_m1):
            cells += [(i, j)]

    for i, j in cells:
        proc = Process(target=element, args=(i, j))
        procs.append(proc)

    for proc in procs:
        proc.start()
        proc.join()

