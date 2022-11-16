# Write a function called repeatStr which repeats the given string string exactly n times.


def repeat_str(repeat, string):
    return repeat * string


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert repeat_str(4, 'a') == 'aaaa'

    # test case 2
    assert repeat_str(3, 'hello ') == 'hello hello hello '

    # test case 3
    assert repeat_str(2, 'abc') == 'abcabc'
