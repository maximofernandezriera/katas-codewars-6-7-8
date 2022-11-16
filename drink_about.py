#     Kids drink toddy.
#     Teens drink coke.
#     Young adults drink beer.
#     Adults drink whisky.
#
# Make a function that receive age, and return what they drink.
#
# Rules:
#
#     Children under 14 old.
#     Teens under 18 old.
#     Young under 21 old.
#     Adults have 21 or more.


def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age >= 14 and age < 18:
        return "drink coke"
    elif age >= 18 and age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"


if __name__ == "__main__":
    
    ### TEST CASES ###

    # test case 1
    assert people_with_age_drink(13) == "drink toddy"

    # test case 2
    assert people_with_age_drink(17) == "drink coke"

    # test case 3
    assert people_with_age_drink(18) == "drink beer"

    # test case 4
    assert people_with_age_drink(20) == "drink beer"

    # test case 5
    assert people_with_age_drink(30) == "drink whisky"
