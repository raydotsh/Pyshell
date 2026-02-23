import os
import shutil

def run(args):
    if len(args) != 2:
        print("Usage: mv <source> <destination>")
        return

    src, dest = args

    if not os.path.exists(src):
        print(f"mv: no such file: {src}")
        return

    try:
        shutil.move(src, dest)
        print(f"Moved '{src}' -> '{dest}'")
    except Exception as e:
        print(f"mv error: {e}")
