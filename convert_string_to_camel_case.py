# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized.
#
# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):

    newString = ''
    flag = False

    for letter in text:
        if letter == '-' or letter == '_':
            flag = True
            continue
        elif flag:
            newString += letter.upper()
            flag = False
        else:
            newString += letter

    newString = newString.replace('_', '')
    newString = newString.replace('-', '')

    return newString


if __name__ == '__main__':

    ### TEST CASES ###

    # test case 1
    assert to_camel_case('') == ''

    # test case 2
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"

    # test case 3
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"

    # test case 4
    assert to_camel_case("A-B-C") == "ABC"
