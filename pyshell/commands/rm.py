import os
import shutil

def rm(target, recursive=False, force=False):
    if not os.path.exists(target):
        if not force:
            print(f"rm: no such file or directory: {target}")
        return

    try:
        if os.path.isdir(target):
            if recursive:
                shutil.rmtree(target)
                print(f"Removed directory '{target}'")
            else:
                print(f"rm: cannot remove '{target}': Is a directory")
        else:
            os.remove(target)
            print(f"Removed file '{target}'")
    except Exception as e:
        if not force:
            print(f"rm error: {e}")

def run(args):
    if not args:
        print("rm: missing operand")
        return

    flags = [a for a in args if a.startswith("-")]
    paths = [a for a in args if not a.startswith("-")]

    recursive = "-r" in flags or "-rf" in flags or "-fr" in flags
    force = "-f" in flags or "-rf" in flags or "-fr" in flags

    for path in paths:
        rm(path, recursive=recursive, force=force)
