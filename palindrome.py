''' palindrome verifier
palindrome.py
Chris Coggins

this program with take an input string and verify whether the characters creat a palindrome;
where the characters read the same forwards or backwards
'''
from collections import deque


def validate_type(string):
    try:
        if type(string) != str:
            raise ValueError("The input is not a string")
    except ValueError:
        print("The input is not a string")

    return string

def is_palindrome(string):
    string_deque = deque(string)
    if not string_deque:
        return False
    return string

def main():

    string = 'a'
    string = validate_type(string)
    string_deque = is_palindrome(string)
    print(string_deque)

if __name__ == '__main__':
        main()
