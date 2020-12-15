# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
import sys

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n


def MatrixChainOrderDynamicProgramming(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]

    # m[i, j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L + 1):
            j = i + L-1
            m[i][j] = sys.maxsize
            for k in range(i, j):

                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n-1]


def MatrixChainOrderRecursive(p, i, j):

    # A naive recursive implementation that
    # simply follows the above optimal
    # substructure property

    # Matrix A[i] has dimension p[i-1] x p[i]
    # for i = 1..n

    if i == j:
        return 0

    _min = sys.maxsize

    # place parenthesis at different places
    # between first and last matrix,
    # recursively calculate count of
    # multiplications for each parenthesis
    # placement and return the minimum count
    for k in range(i, j):

        count = (MatrixChainOrderRecursive(p, i, k)
                 + MatrixChainOrderRecursive(p, k + 1, j)
                 + p[i-1] * p[k] * p[j])

        if count < _min:
            _min = count

    # Return minimum count
    return _min


# Driver program to test above function
# arr = [1, 2, 3, 4]
# size = len(arr)

# print("Minimum number of multiplications is " +
#       str(MatrixChainOrderDynamicProgramming(arr, size)))

# See here for more of a reference https://www.geeksforgeeks.org/python-program-for-matrix-chain-multiplication-dp-8/