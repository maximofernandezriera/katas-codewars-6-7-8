# Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.
#
# Can you help her?


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert greet("James") == "Hello, James!"

    # test case 2
    assert greet("Jane") == "Hello, Jane!"

    # test case 3
    assert greet("Jim") == "Hello, Jim!"

    # test case 4
    assert greet("Johnny") == "Hello, my love!"
