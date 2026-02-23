import sys

def cat(filepaths):
    for filepath in filepaths:
        try:
            with open(filepath, 'r') as f:
                print(f.read(), end='')
        except FileNotFoundError:
            print(f"Oops! No such file called {filepath}")
        except IsADirectoryError:
            print(f"Oops! {filepath} is a directory, not a file")
        except PermissionError:
            print(f"Oops! You don’t have permission to read {filepath}")

if __name__ == "__main__":
    filepaths = sys.argv[1:]
    if not filepaths:
        print("Usage: python cat.py <file1> <file2> ...")
    else:
        cat(filepaths)

def run(args):
    if not args:
        print("cat: missing file operand")
    else:
        cat(args)
