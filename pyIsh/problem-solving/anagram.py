# check if strB is an anagram of strA

from re import sub

textA = "mood"
textB = "doom"

def clean_string(text: str) -> str:
    cleaned: str = sub(r"[^\w]", "", text).lower()
    sorted_string = sorted(cleaned)
    return "".join(sorted_string)

def is_anagram(strA: str, strB: str) -> bool:
    if (clean_string(textA) == clean_string(textB)):
        return True
    return False

print(is_anagram(textA, textB))