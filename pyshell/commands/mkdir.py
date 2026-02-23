import os

def mkdir(dirname):
    try:
        os.mkdir(dirname)
        print(f"Directory '{dirname}' created.")
    except FileExistsError:
        print(f"mkdir: cannot create directory '{dirname}': File exists")
    except PermissionError:
        print(f"mkdir: permission denied: {dirname}")
    except Exception as e:
        print(f"mkdir: error creating '{dirname}': {e}")

def run(args):
    if not args:
        print("mkdir: missing operand")
        return

    flags = [a for a in args if a.startswith("-")]
    dirs = [a for a in args if not a.startswith("-")]

    parents = "-p" in flags

    for d in dirs:
        try:
            if parents:
                os.makedirs(d, exist_ok=True)
            else:
                os.mkdir(d)
            print(f"Directory '{d}' created.")
        except FileExistsError:
            print(f"mkdir: cannot create directory '{d}': File exists")
        except PermissionError:
            print(f"mkdir: permission denied: {d}")
