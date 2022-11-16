# Create a function that gives a personalized greeting.
# This function takes two parameters: name and owner.
#
# Use conditionals to return the proper message.


def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    return 'Hello guest'


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert greet('Daniel', 'Daniel') == 'Hello boss'

    # test case 2
    assert greet('Greg', 'Daniel') == 'Hello guest'
