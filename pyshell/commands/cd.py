import os

previous_dir = os.getcwd()

def run(args):
    global previous_dir

    try:
        # No args → go home
        if len(args) == 0:
            target = os.path.expanduser("~")

        # cd -
        elif args[0] == "-":
            target = previous_dir
            print(target)  # mimic real shell behavior

        else:
            target = os.path.expanduser(args[0])

        current = os.getcwd()
        os.chdir(target)
        previous_dir = current

    except FileNotFoundError:
        print(f"cd: no such file or directory: {target}")
    except NotADirectoryError:
        print(f"cd: not a directory: {target}")
    except PermissionError:
        print(f"cd: permission denied: {target}")


