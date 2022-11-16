# In your class, you have started lessons about "arithmetic progression".
# Because you are also a programmer, you have decided to write a function.
#
# This function, arithmetic_sequence_sum(a, r, n), should return the sum of the first (n) elements
# of a sequence in which each element is the sum of the given integer (a), and a number of occurences of the given integer (r),
# based on the element's position within the sequence.
#
# For example:
#
# arithmetic_sequence_sum(2, 3, 5) should return 40:
#
#     1     2        3          4            5
#     a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r)
#     2 + (2+3) + (2+3+3) + (2+3+3+3) + (2+3+3+3+3) = 40


def arithmetic_sequence_sum(a, r, n):
    result = a
    count = 1
    while count < n:
        result += a + (count * r)
        count += 1
    return result


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert arithmetic_sequence_sum(3, 2, 20) == 440

    # test case 2
    assert arithmetic_sequence_sum(2, 2, 10) == 110

    # test case 3
    assert arithmetic_sequence_sum(1, -2, 10) == -80
