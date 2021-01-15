# DP implementation for Coin Change problem
def countMemoized(set_of_given_coins: list,
                  length_of_set_of_given_coins: int,
                  number_of_cents: int) -> int:
    '''
    Returns a memoized table taking care of the coin changes possible

    Parameters:
    - @param: set_of_given_coins - This is a given set of the input array for 
    the set of coins that we have to make change for
    - @param: length_of_set_of_given_coins - simply an integer denoting 
    - @param: number_of_cents - the total number of cents we can make 
    changes with

    Returns:
    - The last obtained result in the memoized table created
    '''

    # We would need to create n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value case (n = 0)
    memoized_table = [[0 for iterator in range(
        length_of_set_of_given_coins)] for iterator in range(number_of_cents+1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(length_of_set_of_given_coins):
        memoized_table[0][i] = 1

    # Fill rest of the memoized_table entries in bottom up manner
    for ith_row in range(1, number_of_cents+1):
        for jth_col in range(length_of_set_of_given_coins):

            # Count of solutions including set_of_given_coins[j]
            if ith_row-set_of_given_coins[jth_col] >= 0:
                x = memoized_table[ith_row -
                                   set_of_given_coins[jth_col]][jth_col]
            else:
                x = 0

            # Count of solutions excluding set_of_given_coins[j]
            if jth_col >= 1:
                y = memoized_table[ith_row][jth_col-1]
            else:
                y = 0

            # total count
            memoized_table[ith_row][jth_col] = x + y

    # Return the last obtained result
    print(f'{len(memoized_table)}, {len(memoized_table[0])} {number_of_cents}, {length_of_set_of_given_coins}')
    return memoized_table[number_of_cents-1][length_of_set_of_given_coins-1]


def countBottomUp(set_of_given_coins: list,
                  length_of_set_of_given_coins: int,
                  number_of_cents: int):
    '''
    Performs the countBottomUp operation, for performing the Coin
    Change problem in a bottom up fashion

    Parameters:
    - @param: set_of_given_coins - This is a given set of the input array for 
    the set of coins that we have to make change for
    - @param: length_of_set_of_given_coins - simply an integer denoting 
    - @param: number_of_cents - the total number of cents we can make 
    changes with

    Returns:
    - The last obtained result in the memoized table created
    '''

    # Memoized_table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the memoized_table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all memoized_table values as 0
    memoized_table = [0 for k in range(number_of_cents+1)]

    # Base case if given value is 0
    memoized_table[0] = 1

    # Pick all coins one by one and update the memoized_table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for ith_row in range(0, length_of_set_of_given_coins):
        for jth_col in range(set_of_given_coins[ith_row], number_of_cents+1):
            memoized_table[jth_col] += memoized_table[jth_col -
                                                      set_of_given_coins[ith_row]]

    return memoized_table[number_of_cents]


def countSelection(dataset: list, number_of_cents: int = 307,
                   option_selection: int = 2):
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

    result = 0

    if option_selection == 1:
        result = countMemoized(dataset, len(dataset), number_of_cents)

    if option_selection == 2:
        result = countBottomUp(dataset, len(dataset), number_of_cents)

    return result
