def rodCuttingTopDown(input_array: list,
                      rod_length: int = 307) -> int:
    '''
    Rod cutting is another kind of problem which can be solved 
    without using dynamic programming approach but we can optimize 
    it greatly by using it. According to the problem, we are 
    provided with a long rod of length n units. We can cut the 
    rod in different sizes and each size has a different cost 
    associated with it i.e., a rod of i units length will have 
    a cost of c(i). 

    Parameters:
    - @param: input_arrray - Self explanatory, the array sent for the computations
    - @param: rod_length - Self explanatory, the size of array given

    Returns:
    - The recursive ephemeral solution as an integer
    '''

    def findMax(x, y):
        if x > y:
            return x
        return y

    INF = 100000
    inf_range = [0] + [-1*INF]*5

    if(inf_range[rod_length] >= 0):
        return inf_range[rod_length]

    maximum_revenue = -1*INF

    for i in range(1, rod_length+1):

        maximum_revenue = findMax(
            maximum_revenue, input_array[i] +
            rodCuttingTopDown(input_array, rod_length-i))

    inf_range[rod_length] = maximum_revenue
    return inf_range[rod_length]
