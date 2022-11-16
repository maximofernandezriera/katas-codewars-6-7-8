# Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
  if number % 2 == 0:
      return 'Even'
  return 'Odd'


if __name__ == "__main__":

    ### TEST CASES ###

    # test case 1
    assert even_or_odd(2) == 'Even'

    # test case 2
    assert even_or_odd(0) == 'Even'

    # test case 3
    assert even_or_odd(7) == 'Odd'

    # test case 4
    assert even_or_odd(1) == 'Odd'
