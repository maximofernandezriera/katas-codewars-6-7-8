# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert basic_op('+', 4, 7) == 11

    # test case 2
    assert basic_op('-', 15, 18) == -3

    # test case 3
    assert basic_op('*', 5, 5) == 25

    # test case 4
    assert basic_op('/', 49, 7) == 7
