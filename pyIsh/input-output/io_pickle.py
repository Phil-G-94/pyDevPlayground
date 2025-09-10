# # Python provides a standard module called `pickle`
# # that we can use to store any plain Python object in a file
# # and retrieve it as needed

# import pickle
# import io

# # the name of the file where we store the object data
# shopping_list_file = "shoplist.data"

# shop_list = ["apple", "mango", "shinguards"]

# # write to the file
# file = io.open(shopping_list_file, "wb")  # "wb" write and binary

# # dump the object into the file
# pickle.dump(shop_list, file)

# # close file
# file.close()

# # destroy shop_list variable
# del shop_list

# # read back from storage
# file = io.open(shopping_list_file, "rb")  # "rb" read and binary

# # load the storad object
# stored_list = pickle.load(file)

# print(stored_list)

# file.close()

# Working with pathlib in order to specify what dir a file should be saved in #

from typing import Sequence
from pathlib import Path
import pickle

data: dict[str, str | Sequence[str]] = {
    "Customer": "Partington McAslan & Partners",
    "Partner": "Lotality IP",
    "Vendors": ["AMD", "Gooxi", "NVIDIA"],
}

# create a path for io-data directory
data_directory = (
    Path.home()
    / "Desktop"
    / "Playgrounds"
    / "PyDevPlayground"
    / "pyIsh"
    / "input-output"
    / "io-data"
)

# make exactly this one directory
data_directory.mkdir(parents=True, exist_ok=True)

data_file = data_directory / "customers-vendors.data"

with data_file.open("wb") as f:
    pickle.dump(data, f)

with data_file.open("rb") as f:
    stored_list = pickle.load(f)

print(stored_list)
