import shutil
import os

def run(args):
    if len(args) < 2:
        print("cp: missing file operand")
        return

    flags = [a for a in args if a.startswith("-")]
    paths = [a for a in args if not a.startswith("-")]

    recursive = "-r" in flags

    src = paths[0]
    dest = paths[1]

    if not os.path.exists(src):
        print(f"cp: no such file: {src}")
        return

    try:
        if os.path.isdir(src):
            if recursive:
                shutil.copytree(src, dest)
            else:
                print(f"cp: -r not specified for directory '{src}'")
        else:
            shutil.copy2(src, dest)

        print(f"Copied '{src}' -> '{dest}'")
    except Exception as e:
        print(f"cp error: {e}")
