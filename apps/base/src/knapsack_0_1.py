# A naive recursive implementation of the 0-1 Knapsack Problem
def knapSackRecursive(total_weight_available: int,
                      weight_list: list, value_list: list,
                      total_values: int):
    '''
    Returns the maximum value that can be put in a knapsack of
    capacity total_weight_available

    Parameters:
    - @param: total_weight_available - Total capacity available in the knapsack
    - @param: weight_list - List of weights associated with their respective values
    - @param: value_list - List of values associated with their respective weights
    - @param: total_values - Total length of the weights to values dict

    @Returns:
    - (int), the answer is an ephemearal, obtained via the recursive method
    '''

    # Base Case # 1
    if total_values == 0:
        return 0

    # Base Case # 2
    if total_weight_available == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity total_weight_available,
    # then this item cannot be included
    # in the optimal solution
    if (weight_list[total_values-1] > total_weight_available):
        return knapSackRecursive(total_weight_available, weight_list, value_list, total_values-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            value_list[total_values-1] + knapSackRecursive(
                total_weight_available -
                weight_list[total_values-1], weight_list,
                value_list, total_values-1),
            knapSackRecursive(total_weight_available, weight_list, value_list, total_values-1))


def knapSackDynamic(total_knapsack_capacity: int, weight_dataset: list,
                    value_dataset: list, total_values: int):
    '''
    A Dynamic Programming based Python
    Program for 0-1 Knapsack problem
    Returns the maximum value that can
    be put in a knapsack of capacity W

    Parameters:
    - @param: total_weight_available - Total capacity available in the knapsack
    - @param: weight_list - List of weights associated with their respective values
    - @param: value_list - List of values associated with their respective weights
    - @param: total_values - Total length of the weights to values dict

    @Returns:
    - (int), the answer is an ephemearal, obtained via the recursive method
    '''

    K = [[0 for x in range(total_knapsack_capacity + 1)]
         for x in range(total_values + 1)]

    # Build table K[][] in bottom up manner
    for i in range(total_values + 1):

        for w in range(total_knapsack_capacity + 1):

            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight_dataset[i-1] <= w:
                K[i][w] = max(value_dataset[i-1]
                              + K[i-1][w-weight_dataset[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[total_values][total_knapsack_capacity]


def knapsackMemoization(total_weight_available: int,
                        weight_list: list, value_list: list,
                        total_values: int):
    '''
    This is the memoization approach of
    0 / 1 Knapsack approach in Python. It's a 
    Recursive and Memoized based solution to give DP

    Parameters:
    - @param: total_weight_available - Total capacity available in the knapsack
    - @param: weight_list - List of weights associated with their respective values
    - @param: value_list - List of values associated with their respective weights
    - @param: total_values - Total length of the weights to values dict

    @Returns:
    - (int), the answer is an ephemearal, obtained via the recursive method
    '''

    # We initialize the matrix with -1 at first.
    matrix_t = [[-1 for i in range(total_weight_available + 1)]
                for j in range(total_values + 1)]

    # base conditions
    if total_values == 0 or total_weight_available == 0:
        return 0

    if matrix_t[total_values][total_weight_available] != -1:
        return matrix_t[total_values][total_weight_available]

    # choice diagram code
    if weight_list[total_values-1] <= total_weight_available:

        matrix_t[total_values][total_weight_available] = max(
            value_list[total_values-1] + knapsackMemoization(
                total_weight_available-weight_list[total_values-1],
                weight_list, value_list, total_values-1),

            knapsackMemoization(total_weight_available, weight_list,
                                value_list, total_values-1))

        return matrix_t[total_values][total_weight_available]

    elif weight_list[total_values-1] > total_weight_available:

        matrix_t[total_values][total_weight_available] = knapsackMemoization(
            total_weight_available, weight_list,
            value_list, total_values-1)

        return matrix_t[total_values][total_weight_available]


def knapsackSelection(weight_dataset: list, value_dataset: list,
                      total_knapsack_capacity: int = 307, option_selection: int = 2,
                      ):
    '''
    Select the needed knapsackSelection. 1 for the Memoized version, 2 for the
    BottomUp version

    Parameters:
    - @param; weight_dataset: The dataset ( array ) passed in for the weights
    - @param: value_dataset - The dataset ( array ) passed in for the values
    - @param: total_knapsack_capacity - Total knapsack capacity. Default value
    set as the last three digits of the roll number specified in the requirement
    for the proposal
    - @param: option_select - Value can be either 1, 2, or 3

    Returns:
    - None
    '''

    print(
        f'The knapsack method has been selected. Passed in is {option_selection}')

    # See this article for more clarity https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    result = 0
    if option_selection == 1:
        result = knapSackRecursive(
            total_knapsack_capacity, weight_dataset, value_dataset, len(value_dataset))
    elif option_selection == 2:
        result = knapSackDynamic(
            total_knapsack_capacity, weight_dataset, value_dataset, len(value_dataset))
    elif option_selection == 3:
        result = knapsackMemoization(
            total_knapsack_capacity, weight_dataset, value_dataset, len(value_dataset))
    return result
