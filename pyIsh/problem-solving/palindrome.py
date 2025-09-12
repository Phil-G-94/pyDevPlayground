# a string is a palindrome if it's it read the same
# front to back and back to front
# 'madam', 'A man, a plan, a canal - Panama!', 'racecar'
# shouldn't take into account special chars; whitespace, or char case

from re import sub

palindrome_list = [
    "Madam", "Racecar", "A man, a plan, a canal - Panama!"
]

# sanitise input by replacing all non alphanumeric chars with empty string "" and reformatting the entire resulting string to lowercase
def sanitise_input(str: str) -> str:
    return sub(r"[^a-zA-Z0-9]", "", str).lower()

# reverse string by slicing in reverse order
def reverse_input(str: str)-> str:
    return str[::-1]


def is_palindrome(arr: list[str])-> str:
    for palindrome in palindrome_list:
        sanitised = sanitise_input(palindrome)
        reversed = reverse_input(sanitised)
        if (sanitised == reversed):
            print(f"{palindrome} is a palindrome")
        else:
            print(f"{palindrome} is not a palindrome")

    return "Execution complete."

print(is_palindrome(palindrome_list))


