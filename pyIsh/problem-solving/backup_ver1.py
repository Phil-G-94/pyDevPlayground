# A program which creates a backup of all my important files

from dotenv import load_dotenv
import os
import time
import shutil
import tempfile

# load env variable
load_dotenv()

user = os.getenv("User")

# files / directories to be backed up
source = [os.path.expandvars(rf"C:\Users\{user}\Desktop\Playgrounds\tsDevPlayground")]

# backup destination
target_dir = r"C:\Backup"

# name of zip archive - curr date / time
archive_name = time.strftime("%Y%m%d%H%M%S")
target = os.path.join(target_dir, archive_name)

# create target directory if it does not exist
os.makedirs(target_dir, exist_ok=True)

print("Running backup...🏃🏼‍♂️‍➡️")

try:
    # use temp directory to gather all sourcers
    with tempfile.TemporaryDirectory() as temp_dir:
        for item in source:
            if os.path.exists(item):
                # copy files / directories into temp_dir
                if os.path.isdir(item):
                    shutil.copytree(
                        item, os.path.join(temp_dir, os.path.basename(item))
                    )
                else:
                    shutil.copy2(item, temp_dir)
            else:
                print(f"Warning: {item} does not exist and will be skipped.")
        # now make the zip archive from temp_dir
        backup_file = shutil.make_archive(target, "zip", temp_dir)

    print(f"Successful backup to {backup_file}")

except Exception as e:
    print("Backup FAILED:", e)
