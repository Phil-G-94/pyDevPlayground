# Exceptions #

"""
Handling exceptions using try...except
Statements inside try block
Error handlers inside except block
"""

# try:
#     text: str = input("Enter something here --> ")
# except EOFError:
#     print("EOFError - no go!")
# except KeyboardInterrupt:
#     print("KeyboardInterrupt - no go!")
# else:
#     print(f"You entered {text}")

"""
Raising exceptions using the `raise` keyword
Provide the name of the error/exception and the exception object that is to be thrown

The error or exception we throw must be directly or indirectly derived from the Exception class
"""


# class ShortInputException(Exception):
#     """A user defined exception class"""

#     def __init__(self, length: int, atleast: int):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast


# try:
#     serial: str = input("Input something here -> ")

#     if len(serial) < 3:
#         raise ShortInputException(len(serial), 3)
# except EOFError:
#     print("Why did you EOF on me?")
# except KeyboardInterrupt:
#     print("Why did you KeyboardInterrupt on me?")
# except ShortInputException as ex:
#     print(
#         f"ShortInputException: The input was {ex.length} long - expected at least {ex.atleast}"
#     )
# else:
#     print("No exception was raised")


from pathlib import Path
from pickle import dump, load
from typing import List, Optional

serial_directory = (
    Path.home()
    / "Desktop"
    / "Playgrounds"
    / "PyDevPlayground"
    / "pyIsh"
    / "exceptions"
    / "serial-num-data"
)

serial_directory.mkdir(parents=True, exist_ok=True)

serial_file = serial_directory / "serials.data"


class IncorrectSerialFormatException(Exception):
    """
    A user defined exception class
    Raised when the user provides an incorrect format for a serial number
    """

    def __init__(
        self,
        length: int | None,
        is_alphanumeric: bool | None,
        both_failed: bool = False,
    ):
        super().__init__()
        self.length = length
        self.is_alphanumeric = is_alphanumeric
        self.both_failed = both_failed  # flag for special case


def is_alphanumeric(text: str) -> bool:
    return text.isalnum()


def store_serials() -> Optional[List[str | None]] | str:
    input_text: str | None = None

    stored_serials: List[str | None]

    try:
        input_text = input("Input serial number here: ")

        too_short = len(input_text) < 8
        not_alnum = not is_alphanumeric(input_text)

        if too_short and not_alnum:
            # raise specifically for both failing
            raise IncorrectSerialFormatException(
                len(input_text), False, both_failed=True
            )
        elif too_short or not_alnum:
            # raise for single failure
            raise IncorrectSerialFormatException(
                len(input_text), is_alphanumeric(input_text)
            )

    except EOFError:
        print("Why did you EOF on me?")
    except KeyboardInterrupt:
        print("Why did you KeyboardInterrupt on me?")
    except IncorrectSerialFormatException as ex:
        if ex.both_failed:
            print(
                f"IncorrectSerialFormatException: BOTH conditions failed!\n"
                f"Input was {ex.length} chars long (too short) "
                f"and contained non-alphanumeric characters."
            )
        else:

            if ex.length is not None and ex.length < 8:
                length_msg = "too short!"
            else:
                length_msg = "length ok!"

            char_msg = (
                "The input contains only alphanumeric characters - good job!"
                if ex.is_alphanumeric
                else "The input doesn't contain only alphanumeric characters - bad job!"
            )

            print(
                f"IncorrectSerialFormatException: The input was {ex.length} chars long ({length_msg})"
                f"IncorrectSerialFormatException: {char_msg}"
            )
    else:
        # load existing serials or start a new list
        if serial_file.exists():
            with serial_file.open("rb") as f:
                stored_serials = load(f)
        else:
            stored_serials = []

        # append latest serial
        stored_serials.append(input_text)

        with serial_file.open("wb") as f:
            dump(stored_serials, f)
        return stored_serials
    finally:
        return "Execution finished."


store = store_serials()

print(store)
