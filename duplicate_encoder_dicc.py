# The goal of this exercise is to convert a string to a new string where each character in the new string is
#  '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string.
#  Ignore capitalization when determining if a character is a duplicate.
#
#  Examples: "din" => "(((" "recede" => "()()()" "Success" => ")())())" "(( @" => "))(("
# Redone using Dictionaries


def duplicateEncoder(string):

    string = string.upper()

    words = {}
    for letter in string:
        if letter not in words:
            words[letter] = '('
        else:
            words[letter] = ')'

    result = ""
    for letter in string:
        result += words[letter]

    return result


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert duplicateEncoder("din") == "((("

    # test case 2
    assert duplicateEncoder("recede") == "()()()"

    # test case 3
    assert duplicateEncoder("Success") == ")())())"

    # test case 4
    assert duplicateEncoder("(( @") == "))(("
