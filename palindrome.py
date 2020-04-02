# Troy Jeffrey Amegashie
# Assignment 8 - Recursion
# 04-01-2020


def palindrome_check(string):
    string.lower()
    string.strip()

    if len(string) == 0 or len(string) == 1:
        print("Yes it is")
        return True

    elif string[0] != string[-1]:
        print("No it isn't")
        return False

    else:
        return palindrome_check(string[1:-1])


while True:

    word = str(input("Enter a word or a phrase and I'll tell you if it's a palindrome.\n>"))

    if word.isalpha():
        palindrome_check(word)

    else:
        print("You did not enter a word")
