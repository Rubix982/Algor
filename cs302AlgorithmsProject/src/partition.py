# A recursive Python3 program for
# partition problem

# A utility function that returns
# true if there is a subset of
# arr[] with sun equal to given sum


def isSubsetSumRecursive(arr, n, sum):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # If last element is greater than sum, then
    # ignore it
    if arr[n-1] > sum:
        return isSubsetSumRecursive(arr, n-1, sum)

    ''' else, check if sum can be obtained by any of 
    the following
    (a) including the last element
    (b) excluding the last element'''

    return isSubsetSumRecursive(arr, n-1, sum) or isSubsetSumRecursive(arr, n-1, sum-arr[n-1])

# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false


def findPartionRecursive(arr, n):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    # If sum is odd, there cannot be two subsets
    # with equal sum
    if sum % 2 != 0:
        return False

    # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSumRecursive(arr, n, sum // 2)

    # Dynamic Programming based python
# program to partition problem

# Returns true if arr[] can be
# partitioned in two subsets of
# equal sum, otherwise false


def findPartitionDynamicProgramming(arr, n):
    sum = 0
    i, j = 0, 0

    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]

    if sum % 2 != 0:
        return False

    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):

        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])

    return part[sum // 2][n]

# See this link for more reference https://www.geeksforgeeks.org/partition-problem-dp-18/
