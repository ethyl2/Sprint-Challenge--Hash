def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    Return indices of the 2 items whose totaled weight equals the limit

    First, make a hashtable with each weight in weights as a key; its index as its value.
    Then, loop through weight to see if a key exists that is 
        equal to the limit minus the weight at the current index.
    If so, return the 2 indices, with the greater number first.
    """
    # Create weight_dict
    weight_dict = dict()
    for i in range(0, length):
        weight_dict[weights[i]] = i
    # print(weight_dict)

    # Loop through weights to look for the solution
    for i in range(0, length):
        if limit - weights[i] in weight_dict:
            weight_index1 = i
            weight_index2 = weight_dict[limit - weights[i]]
            if weight_index1 < weight_index2:
                weight_index1, weight_index2 = weight_index2, weight_index1
            return (weight_index1, weight_index2)
    return None


# weights_3 = [4, 6, 10, 15, 16]
# print(get_indices_of_item_weights(weights_3, 5, 21))
