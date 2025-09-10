import re


def normalise(text: str) -> str:
    """
    # strip whitespace and special chars (any non-alphanumeric chars) and set to lowercase
    """
    return re.sub(r"[^a-zA-Z0-9]", "", text).lower()


def reverse(text: str) -> str:
    """
    # reverse incoming str
    """
    return text[::-1]  # slicing syntax [start:stop:step]


def is_palindrome(text: str) -> bool:

    normalised = normalise(text)
    normalised_and_reversed = reverse(normalised)

    return normalised == normalised_and_reversed


user_input = input("Enter string: ")
if is_palindrome(user_input):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
