import numpy as np


def levenshteinDynamic(sequence_first: str,
                       sequence_second: str) -> int:
    '''
    The greater the Levenshtein distance, the greater are the difference
    between the strings. For example, from "test" to "test" the Levenshtein 
    distance is 0 because both the source and target strings are identical. 
    No transformations are needed. In contrast, from "test" to "team" the 
    Levenshtein distance is 2 - two substitutions have to be done to turn 
    "test" in to "team".

    Parameters:
    - @Param: sequence_first - The first string sequence
    - @Param: sequence_second - The second string sequence

    Returns:
    - Returns the total number of edits required to convert 
    sequence_first -> sequence_second
    '''

    # Saving the length of both instances
    sequence_first_lenght = len(sequence_first) + 1
    sequence_second_lenght = len(sequence_second) + 1

    matrix = np.zeros((sequence_first_lenght, sequence_second_lenght))

    for x in range(sequence_first_lenght):
        matrix[x, 0] = x
    for y in range(sequence_second_lenght):
        matrix[0, y] = y

    for x in range(1, sequence_first_lenght):
        for y in range(1, sequence_second_lenght):
            if sequence_first[x-1] == sequence_second[y-1]:
                matrix[x, y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1] + 1,
                    matrix[x, y-1] + 1
                )
    return matrix[sequence_first_lenght - 1,
                  sequence_second_lenght - 1]
