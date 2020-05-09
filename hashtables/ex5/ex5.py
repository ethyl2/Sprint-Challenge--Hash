def finder(files, queries):
    """
    Given a list of files and a list of queries, return the files that contain the queries

    Make a dict in which the keys are the last part of the path (file), values the whole path (file).
    Then go through list of queries and look them up in the dict. If an entry exists, append
    the value to the result.
    """
    files_dict = dict()
    for file in files:
        file_split = file.split('/')
        # print(file_split)
        desired = file_split[-1]
        # print(desired)
        if desired not in files_dict:
            files_dict[desired] = [file]
        else:
            files_dict[desired].append(file)
    # print(files_dict)

    result = []
    for query in queries:
        if query in files_dict:
            result.append(files_dict[query])
    # print(result)
    result = [val for sublist in result for val in sublist]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
