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
