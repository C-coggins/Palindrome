''' palindrome verifier
palindrome.py
Chris Coggins

this program with take an input string and verify whether the characters creat a palindrome;
where the characters read the same forwards or backwards
'''



def validate_type(string):
    if type(string) != str:
        raise ValueError("The input is not a string")


def main():

    string = "a"
    validate_type(0)

if __name__ == '__main__':
        main()
