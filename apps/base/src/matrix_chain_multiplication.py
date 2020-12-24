import sys


def matrixChainOrderDynamicProgramming(input_array: list, size_of_input: int):
    '''
    Dynamic Programming Python implementation of Matrix
    Chain Multiplication. See the Cormen book for details
    of the following algorithm.


    For simplicity of the program, one extra row and one
    extra column are allocated in m[][].  0th row and 0th
    column of m[][] are not used

    Parameters:
    - @param: input_array -
    - @param: size_of_input -

    Return:
    -

    '''

    # Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
    m = [[0 for x in range(size_of_input)] for x in range(size_of_input)]

    # m[i, j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, size_of_input):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, size_of_input):
        for i in range(1, size_of_input-L + 1):
            j = i + L-1
            m[i][j] = sys.maxsize
            for k in range(i, j):

                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + input_array[i-1] * \
                    input_array[k]*input_array[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][size_of_input-1]


def matrixChainOrderRecursive(input_array: list, starting_index: int,
                              ending_index: int) -> int:
    '''
    A naive recursive implementation that
    simply follows the above optimal
    substructure property

    For simplicity of the program, one extra row and one
    extra column are allocated in m[][].  0th row and 0th
    column of m[][] are not used

    Parameters:
    - @param: input_array - the input dataset
    - @param: starting_index - the starting index
    - @param: ending_index - the ending index

    Return:
    - The min cost
    '''

    # Matrix A[i] has dimension p[i-1] x p[i]
    # for i = 1..n

    if starting_index == ending_index:
        return 0

    _min = sys.maxsize

    # place parenthesis at different places
    # between first and last matrix,
    # recursively calculate count of
    # multiplications for each parenthesis
    # placement and return the minimum count
    for k in range(starting_index, ending_index):

        count = (matrixChainOrderRecursive(input_array, starting_index, k)
                 + matrixChainOrderRecursive(input_array, k + 1, ending_index)
                 + input_array[i-1] * input_array[k] * input_array[j])

        if count < _min:
            _min = count

    # Return minimum count
    return _min


def matrixChainOrderSelection(dataset: list,
                              option_selection: int = 1):
    '''
    Select the needed countSelection. 1 for the Memoized version, 2 for the
    BottomUp version

    Parameters:
    - @param: dataset - The dataset ( array ) passed in
    - @param: option_select - Value can be either 1 or 2
    - @param: number_of_cents - Number of cents specified, by default, it is 4

    Returns:
    - None
    '''

    print(
        f'The count method has been selected. Passed in is {option_selection}')

    # See here for more of a reference https://www.geeksforgeeks.org/python-program-for-matrix-chain-multiplication-dp-8/
    if option_selection == 1:
        result = matrixChainOrderDynamicProgramming(dataset, len(dataset))
        print(f'The result to the answer is {result}')

    if option_selection == 2:
        result = matrixChainOrderRecursive(dataset, 1, len(dataset) - 1)
        print(f"The result to the answer is {result}")
