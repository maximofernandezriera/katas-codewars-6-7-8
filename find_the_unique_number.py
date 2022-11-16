# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
#     findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
#     findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
#
# It’s guaranteed that array contains more than 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.


def find_uniq(arr):

    if arr.count(max(arr)) == 1:
        return max(arr)
    else:
        return min(arr)


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2

    # test case 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

    # test case 3
    assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10
