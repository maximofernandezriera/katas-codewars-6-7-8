# Very simple, given a number, find its opposite.
# But can you do it in 1 line of code and without any conditionals?


def opposite(number):
  return number - number - number


if __name__ == "__main__":

    ### TEST CASE ###

    # test case 1
    assert opposite(1) == -1
