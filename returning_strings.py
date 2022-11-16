# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
#
# [Make sure you type the exact thing I wrote or the program may not execute properly]


def greet(name):
    return "Hello, " + name + " how are you doing today?"


if __name__ == "__main__":

    ### TEST CASE ###

    # Test case 1
    assert greet('Ryan') == "Hello, Ryan how are you doing today?"
