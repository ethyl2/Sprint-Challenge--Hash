from typing import List
from os.path import basename


def finder2(files, queries):
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


def finder(files: List[str], queries: List[str]):
    # Here is an alternate implementation. For this version, the lookup element is the queries, not the files.

    # The challenge states that dictionaries must be used and not sets.
    # If it didn't say that, I'd use a set here instead of a dictionary:
    queries_dict = {}
    output = []
    for query in queries:
        queries_dict[query] = True

    for file in files:
        if get_end_of_path(file) in queries_dict:
            output.append(file)
    return output

# Two additional ways to get the end of the path of the files:


def get_end_of_path(filename: str) -> str:
    index = filename.rfind('/')
    if index == -1:
        return filename
    return filename[index+1:]


def get_end_of_path2(filename: str) -> str:
    return basename(filename)


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
