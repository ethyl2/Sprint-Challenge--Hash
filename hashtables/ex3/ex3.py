def intersection(arrays):
    """
    Find the numbers that exist in all of the lists.

    # First, flatten the list (maybe)
    # Next, make a count dict
    # Loop through the flattened list and increment the values as the keys show up.
    # Return the keys whose value is the length of the original list (arrays).
    """
    # Flatten the arrays
    flattened = [val for sublist in arrays for val in sublist]
    # print(flattened)

    count_dict = dict()
    for num in flattened:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    # print(count_dict)

    result = [val[0]
              for val in list(count_dict.items()) if val[1] == len(arrays)]
    # print(result)
    return result


if __name__ == "__main__":

    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
    '''
    arrays = [
        [1, 2, 3, 4, 5],
        [12, 7, 2, 9, 1],
        [99, 2, 7, 1, ]
    ]

    intersection(arrays)
    '''
