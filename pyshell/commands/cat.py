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
