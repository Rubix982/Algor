
def longestIncreasingSubsequence(list_for_input: list,
                                   length_of_input: int) -> list:
    '''
    Function for finding length of longest 
    increasing subsequence

    Parameters:
    - @Param: list_for_input - The list for the input, consists of integers
    - @Param: length_of_input - Total length of the input n

    Return:
    - Returns a (list) for the sequence generated
    '''

    longest_increasing_subsequence_list = []
    parent = []

    # initialize lis with 1 as each element
    # has a subsequence length equal to 1
    for i in range(length_of_input):
        longest_increasing_subsequence_list.append(1)

    # initialize parent with -1
    for i in range(length_of_input):
        parent.append(-1)

    for i in range(length_of_input):
        for j in range(i):
            if list_for_input[j] < list_for_input[i]:
                if longest_increasing_subsequence_list[i] < longest_increasing_subsequence_list[j] + 1:
                    longest_increasing_subsequence_list[i] = longest_increasing_subsequence_list[j] + 1
                    parent[i] = j

    length = 0
    pos = 0

    # length of subsequence is the maximum value
    # in longest_increasing_subsequence array
    for i in range(length_of_input):
        if length < longest_increasing_subsequence_list[i]:
            length = longest_increasing_subsequence_list[i]
            pos = i

    # restoring the sequence
    # for storing longest increasing subsequence
    sequence = []

    while pos != -1:
        sequence.append(list_for_input[pos])
        pos = parent[pos]

    sequence.reverse()

    return sequence
