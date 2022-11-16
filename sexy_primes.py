# Sexy primes are pairs of two primes that are 6 apart.
# In this kata, your job is to complete the function sexy_prime(x, y) which returns true if x & y are sexy, false otherwise.
#
# Examples:
#
#     sexy_prime(5,11)
#     --> True
#
#     sexy_prime(61,67)
#     --> True
#
#     sexy_prime(7,13)
#     --> True
#
#     sexy_prime(5,7)
#     --> False
#
#     sexy_prime(1,7)
#     --> False
#     ( 1 is not considered prime )
#
# Note: x & y are always positive integers > 0, but they are not always in order of precendence...
# you can be given either (5,11) or (11,5). Both are equally valid.


def is_prime(num):

    divisor = 2

    while divisor < num and num % divisor != 0:
        divisor += 1

    if divisor == num:
        return True
    return False


def sexy_prime(x, y):

    return is_prime(x) and is_prime(y) and (x - y == 6 or y - x == 6)


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert sexy_prime(5, 11) == True

    # test case 2
    assert sexy_prime(13, 19) == True

    # test case 3
    assert sexy_prime(83, 89) == True

    # test case 4
    assert sexy_prime(1, 11) == False
