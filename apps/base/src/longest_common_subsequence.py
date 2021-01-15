def longestCommonSubsequenceNaive(X: str, Y: str,
                                  X_length: int, Y_length: int):
    '''
    A Naive recursive Python implementation of LCS problem

    Parameters:
    - @param: X - The first sequence, denoted by 'X'
    - @param: Y - The second sequence, denoted by 'Y'
    - @param: X_length - The length of the first sequence
    - @param: Y_length - The length of the second sequence
    '''

    if X_length == 0:
        return 0
    elif Y_length == 0:
        return 0
    elif X[X_length-1] == Y[Y_length-1]:
        return 1 + longestCommonSubsequenceNaive(X, Y, X_length-1, Y_length-1)
    else:
        return max(longestCommonSubsequenceNaive(X, Y, X_length, Y_length-1),
                   longestCommonSubsequenceNaive(X, Y, X_length-1, Y_length))


def longestCommonSubsequenceDynamic(X, Y):
    '''
    Dynamic Programming implementation of LCS problem

    Parameters:
    - @param: X - The first sequence, denoted by 'X'
    - @param: Y - The second sequence, denoted by 'Y'

    Returns:
    - L[m][n] contains length of LCS for X[0..n - 1] 
    and Y[0..m - 1]
    '''

    # find the length of the strings
    X_length = len(X)
    Y_length = len(Y)

    # declaring the array for storing the dp values
    levenshtein_matrix = [[None]*(Y_length + 1) for i
                          in range(X_length + 1)]

    '''
    Following steps build levenshtein_matrix[m + 1][n + 1] in bottom up fashion 
    Note: levenshtein_matrix[i][j] contains length of levenshteinCS_matrix of X[0..i-1] 
    and Y[0..j-1]
    '''
    for ith_row in range(X_length + 1):
        for jth_col in range(Y_length + 1):
            if ith_row == 0 or jth_col == 0:
                levenshtein_matrix[ith_row][jth_col] = 0
            elif X[ith_row-1] == Y[jth_col-1]:
                levenshtein_matrix[ith_row][jth_col] = levenshtein_matrix[ith_row-1][jth_col-1]+1
            else:
                levenshtein_matrix[ith_row][jth_col] = max(
                    levenshtein_matrix[ith_row-1][jth_col],
                    levenshtein_matrix[ith_row][jth_col-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return levenshtein_matrix[X_length][Y_length]


def longestCommonSubsequenceSelection(X: str, Y: str,
                                      option_selection: int = 2,
                                      ):
    '''
    Select the needed longestCommonSubsequence. 1 for the Naive version, 2 for the
    dynamic version

    Parameters:
    - @param: X - The first string
    - @param: Y - The second string
    - @param: option_select - Value can be either 1, or 2

    Returns:
    - None
    '''

    result = 0
    if option_selection == 1:
        result = longestCommonSubsequenceNaive(
            X, Y, len(X), len(Y))
    elif option_selection == 2:
        result = longestCommonSubsequenceDynamic(
            X, Y)

    return result
