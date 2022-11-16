# Nathan loves cycling.
#
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
#
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
#
# For example:
#
#     time = 3 ----> litres = 1
#
#     time = 6.7---> litres = 3
#
#     time = 11.8--> litres = 5


def litres(time):

     result = int(time) * 0.5

     return int(result)


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert litres(2) == 1

    # test case 2
    assert litres(1.4) == 0

    # test case 3
    assert litres(12.3) == 6

    # test case 4
    assert litres(0.82) == 0

    # test case 5
    assert litres(11.8) == 5

    # test case 6
    assert litres(1787) == 893

    # test case 7
    assert litres(0) == 0
