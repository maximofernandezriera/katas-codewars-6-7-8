# Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals,
# saying each of the following phrases each time a petal was torn:
#
#     I love you
#     a little
#     a lot
#     passionately
#     madly
#     not at
#
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
#
# Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.


def how_much_i_love_you(nb_petals):

    if nb_petals % 6 == 1:
        return "I love you"
    elif nb_petals % 6 ==  2:
        return "a little"
    elif nb_petals % 6 ==  3:
        return "a lot"
    elif nb_petals % 6 ==  4:
        return "passionately"
    elif nb_petals % 6 ==  5:
        return "madly"
    else:
        return "not at all"


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert how_much_i_love_you(7) == "I love you"

    # test case 2
    assert how_much_i_love_you(3) == "a lot"

    # test case 3
    assert how_much_i_love_you(6) == "not at all"
