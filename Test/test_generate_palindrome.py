''' Palendrome Test Suite
test_generate_palindrome.py
Chris Coggins
'''

from palindrome import validate_type, is_palindrome

def test_validate_input():
    validate_type(0)                            # enter integer to raise Value error

def test_returns_f_empty():
    assert is_palindrome('') == False           # enter empty string

def test_returns_t_singlea():
    assert is_palindrome('a') == True           # enter single character string

def test_returns_t_doubleb():
    assert is_palindrome('bb') == True          # enter double repeat character string