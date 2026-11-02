''' Palendrome Test Suite
test_generate_palindrome.py
Chris Coggins
'''

from palindrome import validate_type, is_palindrome

def test_validate_input():
    validate_type(0)        # enter integer to raise Value error

def test_returns_f_empty():
    assert is_palindrome('') == False