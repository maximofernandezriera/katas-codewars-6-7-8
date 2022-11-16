# The wide mouth frog is particularly interested in the eating habits of other creatures.
#
# He just can't stop asking the creatures he encounters what they like to eat.
# But then he meet the alligator who just LOVES to eat wide-mouthed frogs!
#
# When he meets the alligator, it then makes a tiny mouth.
#
# Your goal in this kata is to create complete the mouth_size method this method
# take one argument animal which corresponds to the animal encountered by frog.
# If this one is an alligator (case insensitive) return small otherwise return wide.


def mouth_size(animal):

    if animal.lower() == 'alligator':
        return 'small'
    return 'wide'


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert mouth_size("toucan") == "wide"

    # test case 2
    assert mouth_size("ant bear") == "wide"

    # test case 3
    assert mouth_size("alligator") == "small"
