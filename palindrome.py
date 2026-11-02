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

def main():

    string = 'bb'                                           # input string instantiation
    string = validate_type(string)                          # validaate string type function call
    string_deque = is_palindrome(string)                    # verify palindrome function call
    print(string_deque)                                     # print return value of is_palindrome

if __name__ == '__main__':
        main()
