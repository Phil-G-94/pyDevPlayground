# a string is an anagram if it's it read the same
# front to back and back to front
# 'madam', 'A man, a plan, a canal - Panama!', 'racecar'
# shouldn't take into account special chars; whitespace, or char case

from re import sub

anagram_list = [
    "Madam", "Racecar", "A man, a plan, a canal - Panama!"
]

def sanitise_input(str: str) -> str:
    return sub(r"[^a-zA-Z0-9]", "", str).lower()

def reverse_input(str: str)-> str:
    return str[::-1]

def is_anagram(arr: list[str])-> str:
    for anagram in anagram_list:
        sanitised = sanitise_input(anagram)
        reversed = reverse_input(sanitised)
        if (sanitised == reversed):
            print(f"{anagram} is an anagram")
        else:
            print(f"{anagram} is not an anagram")

    return "Can't determine..."

print(is_anagram(anagram_list))


