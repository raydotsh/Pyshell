import os

def cd(path):
    try:
        os.chdir(os.path.expanduser(path))
    except FileNotFoundError:
        print(f"cd: no such file or directory: {path}")
    except NotADirectoryError:
        print(f"cd: not a directory: {path}")
    except PermissionError:
        print(f"cd: permission denied: {path}")
