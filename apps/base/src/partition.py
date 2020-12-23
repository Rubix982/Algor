

def isSubsetSumRecursive(input_array: list, size_of_input_array: int,
                         sum_of_subset: float):
    '''
    A utility function that returns
    true if there is a subset of
    input_array[] with sun equal to given sum

    Parameters:
    - @param: input_array - self explanatory, the input array itself
    - @param: size_of_input_array - self explanatory, the size of the input array
    - @param: sum_of_subset - reducer for the sum obtained of the subset given
    '''

    # Base Cases
    if sum_of_subset == 0:
        return True
    if size_of_input_array == 0 and sum_of_subset != 0:
        return False

    # If last element is greater than sum, then
    # ignore it
    if input_array[size_of_input_array-1] > sum_of_subset:
        return isSubsetSumRecursive(input_array, size_of_input_array-1, sum_of_subset)

    ''' 
    Else, if the above is not true, check if sum can be obtained 
    by any of the following
    (a) including the last element
    (b) excluding the last element
    '''

    # Returns true if arr[] can be partitioned in two
    # subsets of equal sum, otherwise false
    return isSubsetSumRecursive(input_array, size_of_input_array-1, sum_of_subset) or \
        isSubsetSumRecursive(input_array, size_of_input_array-1,
                             sum_of_subset-input_array[size_of_input_array-1])


def findPartionRecursive(input_array: list,
                         size_of_input_array: int):
    '''
    Recursive solution for findPartition

    Parameters:
    - @param: input_array - self explanatory, the input array itself
    - @param: size_of_input_array - self explanatory, the size of the input array
    '''

    # Calculate sum of the elements in array
    total_sum = 0
    for i in range(0, size_of_input_array):
        total_sum += input_array[i]

    # If total_sum is odd, there cannot be two subsets
    # with equal total_sum
    if total_sum % 2 != 0:
        return False

    # Find if there is subset with total_sum equal to
    # half of total total_sum
    return isSubsetSumRecursive(input_array, size_of_input_array, total_sum // 2)


def findPartitionDynamicProgramming(input_array: list,
                                    size_of_input_array: int):
    '''
    Returns true if arr[] can be
    partitioned in two subsets of
    equal sum, otherwise false

    Parameters:
    - @param: input_array - self explanatory, the input array itself
    - @param: size_of_input_array - self explanatory, the size of the input array
    '''

    total_sum = 0
    i, j = 0, 0

    # calculate total_sum of all elements
    for i in range(size_of_input_array):
        total_sum += input_array[i]

    if total_sum % 2 != 0:
        return False

    partition = [[True for i in range(size_of_input_array + 1)]
                 for j in range(total_sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, size_of_input_array + 1):
        partition[0][i] = True

    # initialize leftmost column,
    # except partition[0][0], as 0
    for i in range(1, total_sum // 2 + 1):
        partition[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, total_sum // 2 + 1):

        for j in range(1, size_of_input_array + 1):
            partition[i][j] = partition[i][j - 1]

            if i >= input_array[j - 1]:
                partition[i][j] = (partition[i][j] or
                                   partition[i - input_array[j - 1]][j - 1])

    return partition[total_sum // 2][size_of_input_array]


def findPartitionSelection(dataset: list, option_selection: int = 2):
    '''
    Select the needed countSelection. 1 for the Memoized version, 2 for the
    BottomUp version

    Parameters:
    - @param: dataset - The dataset ( array ) passed in
    - @param: option_select - Value can be either 1 or 2

    Returns:
    - None
    '''

    print(
        f'The partition method has been selected. Passed in is {option_selection}')

    # See here for more details https://www.geeksforgeeks.org/python-program-for-coin-change/
    if option_selection == 1:
        result = findPartionRecursive(dataset, len(dataset))
        print(f'The result to the answer is {result}')

    if option_selection == 2:
        result = findPartitionDynamicProgramming(dataset, len(dataset))
        print(f"The result to the answer is {result}")
