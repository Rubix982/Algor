def wordBreak(language_dictionary: list, input_string: str, final_output, out=""):
    '''
    Function to segment given into a space-separated
    sequence of one or more dictionary words

    Parameters:
    
    '''

    # if we have reached the end of the String,
    # print the output String
    if not input_string:
        final_output.append(out)
        return

    for i in range(1, len(input_string) + 1):
        # consider all prefixes of current String
        prefix = input_string[:i]

        # if the prefix is present in the dictionary, add prefix to the
        # output and recur for remaining String
        if prefix in language_dictionary:
            wordBreak(language_dictionary, input_string[i:], final_output, out + " " + prefix)
