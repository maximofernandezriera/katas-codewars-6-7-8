# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#
# For example:
#
#     summation(2) -> 3
#     1 + 2
#
#     summation(8) -> 36
#     1 + 2 + 3 + 4 + 5 + 6 + 7 + 8


def summation(num):

    result = 0
    count = 1

    while count <= num:
        result += count
        count += 1

    return result


if __name__ == '__main__':

    ### TEST CASES ###

    # test case 1
    assert summation(1) == 1

    # test case 2
    assert summation(8) == 36
