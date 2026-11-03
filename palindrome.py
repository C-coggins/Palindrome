''' palindrome verifier
palindrome.py
Chris Coggins

this program with take an input string and verify whether the characters creat a palindrome;
where the characters read the same forwards or backwards
'''
from collections import deque

# validate the input is a string
def validate_type(string):
    try:
        if type(string) != str:                             # if not a string
            raise ValueError("The input is not a string")   # raise an error flag
    except ValueError:                                      # ecxeption for and error flag
        print("The input is not a string")                  # print Error message

    return string                                           # return the validated string

# verify whether the input string is a palindrome
def is_palindrome(string):
    string_deque = deque(string)                            # copy input string to a deque
    if not string_deque:                                    # if deque is empty
        return False                                        # return false
    if len(string_deque) == 1:                              # if deque contains only 1 character
        return True                                         # return true
    if len(string_deque) > 1:                               # if deque contains 2 or more character
        while len(string_deque) > 1:                        # Loop through characters
            char_start = string_deque.popleft()             # pop the first character
            char_end = string_deque.pop()                   # pop the last character
            if char_start != char_end:                      # Are the characters the same
                return False                                # if no return false
        return True                                         # return true


def main():

    string = 'Laval'                                           # input string instantiation
    string = validate_type(string)                          # validaate string type function call
    palindrome_boolean = is_palindrome(string)                    # verify palindrome function call

    # print the appropriate message based on the result from is_palindrome function
    if palindrome_boolean:
        print(f'{string} is {palindrome_boolean} palindrome' )     # print if true                               # print return value of is_palindrome
    else:
        print(f'{string} is not a palindrome')                     # print if false
if __name__ == '__main__':
        main()
