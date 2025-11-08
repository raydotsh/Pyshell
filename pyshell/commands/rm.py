import os
import shutil

def rm(target):
    if os.path.isfile(target):
        os.remove(target)
        print(f"Removed file '{target}'")
    elif os.path.isdir(target):
        try:
            shutil.rmtree(target)
            print(f"Removed directory '{target}'")
        except Exception as e:
            print(f"Error removing directory '{target}': {e}")
    else:
        print(f"'{target}' not found")
