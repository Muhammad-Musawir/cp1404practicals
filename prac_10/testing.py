import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length  # Fix: change ">" to ">="

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # fix the repeat_string function above so that it passes the failing test
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # write assert statements to show if Car sets the fuel correctly
    # Test 1: using the value passed in
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"
    # Test 2: using the default value
    test_car_default = Car()
    assert test_car_default.fuel == 0, "Car does not set default fuel correctly"

run_tests()

# Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.runmod()

def format_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('this is another test')
    'This is another test.'
    """
    return phrase.capitalize() + ('.' if not phrase.endswith('.') else '')

# Run the tests
doctest.runmod()
