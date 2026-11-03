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

def test_returns_f_abc():
    assert is_palindrome('abc') == False        # enter varying character string

def test_returns_t_laval():
    assert is_palindrome('laval') == True        # enter 'laval' character string

def test_returns_t_toronto():
    assert is_palindrome('toronto') == False     # enter 'toronto' character string

def test_returns_t_Able_was():
    assert is_palindrome('Able was I ere I saw Elba') == True          # enter 'Able was I ere I saw Elba' character string