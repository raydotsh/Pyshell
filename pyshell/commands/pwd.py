import os
import sys

def pwd(args: list[str]) -> None:
    if len(args) > 1:
        print("pwd: too many arguments")
        return

    use_physical = False
    if args and args[0] == '-P':
        use_physical = True
        args = []
    elif args:
        print(f"pwd: invalid option -- '{args[0]}'")
        return

    try:
        cwd = os.getcwd()
        if use_physical:
            cwd = os.path.realpath(cwd)
        print(cwd)
    except OSError as e:
        print(f"pwd: failed to get current directory: {e}")

if __name__ == "__main__":
    pwd(sys.argv[1:])

def run(args):
    pwd(args)
