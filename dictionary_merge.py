# Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.
#
# The keys in the given dictionaries can overlap.
# In that case you should combine all source values in an array.
# Duplicate values should be preserved.
#
# Here is an example:
#
#     var source1 = new Dictionary<string, int>{{"A", 1}, {"B", 2}};
#     var source2 = new Dictionary<string, int>{{"A", 3}};
#
#     Dictionary<string, int[]> result = DictionaryMerger.Merge(source1, source2);
#     // result should have this content: {{"A", [1, 3]}, {"B", [2]}}
#
# You can assume that only valid dictionaries are passed to your function.
# The number of given dictionaries might be large.
# So take care about performance.


def merge(*dicts):

    merged = {}

    for dic in dicts:

        list_key = list(sorted(dic.keys()))
        list_value = list(sorted(dic.values()))
        merged = dict(zip(list_key, list_value))

    return merged


if __name__ == '__main__':

    ### TEST CASES ###

    # test case 1
    assert merge({},{},{}) == {}

    # test case 2
    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}

    # test case 3
    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}

    # test case 4
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) == {"A": [1, 4], "B": [2], "C": [3], "D": [5]}
