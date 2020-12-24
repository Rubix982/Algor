def superSeqNaive(X: str, Y: str,
                  m: int, n: int) -> int:
    '''
    A Naive recursive python program to find
    length of the shortest supersequence

    Parameters:
    - @param: X - The first sequence
    - @param: Y - The second sequence
    - @param: m - The length of the first sequence
    - @param: n - The length of the second sequence

    Returns:
    - Return the super sequence length found
    '''
    if (not m):
        return n
    if (not n):
        return m

    if (X[m - 1] == Y[n - 1]):
        return 1 + superSeqNaive(X, Y, m - 1, n - 1)

    return 1 + min(superSeqNaive(X, Y, m - 1, n),
                   superSeqNaive(X, Y, m, n - 1))


def superSeqDynamic(X: str, Y: str,
                    m: int, n: int) -> int:
    '''
    A Dynamic Approach to the  recursive python 
    program to find length of the shortest supersequence

    Parameters:
    - @param: X - The first sequence
    - @param: Y - The second sequence
    - @param: m - The length of the first sequence
    - @param: n - The length of the second sequence

    Returns:
    - Return the super sequence length found

    '''

    dp_matrix = [[0] * (n + 2) for i in range(m + 2)]

    # Fill table in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # Below steps follow above recurrence
            if (not i):
                dp_matrix[i][j] = j
            elif (not j):
                dp_matrix[i][j] = i

            elif (X[i - 1] == Y[j - 1]):
                dp_matrix[i][j] = 1 + dp_matrix[i - 1][j - 1]

            else:
                dp_matrix[i][j] = 1 + min(dp_matrix[i - 1][j],
                                          dp_matrix[i][j - 1])

    return dp_matrix[m][n]


def superSeqSelection(X: str, Y: str,
                      option_selection: int = 2):
    '''
    Select the needed countSelection. 1 for the Memoized version, 2 for the
    BottomUp version

    Parameters:
    - @param: X - The first sequence
    - @param: Y - The second sequence
    - @param: option_select - Value can be either 1 or 2

    Returns:
    - None
    '''

    print(
        f'The shortest_common_subsequence method has been selected. Passed in is {option_selection}')

    result = 0
    if option_selection == 1:
        result = superSeqNaive(X, Y, len(X), len(Y))

    if option_selection == 2:
        result = superSeqDynamic(X, Y, len(X), len(Y))
    return result
