import os 
import sys
import shutil
import subprocess

# Colored output
BLUE = "\033[94m"
WHITE = "\033[97m"
DIM = "\033[90m"
GREEN = "\033[92m"
RESET = "\033[0m"

def list_dir():
    items = os.listdir()
    for item in sorted(items):
        if os.path.isdir(item):
            print(f"{BLUE}DIR{RESET}  {DIM}-------{RESET}  {BLUE}{item}{RESET}")
        else:
            size = os.path.getsize(item)
            print(f"{WHITE}FILE{RESET} {DIM}{size:7} bytes{RESET}  {WHITE}{item}{RESET}")

def make_dir(name):
    try:
        os.mkdir(name)
        print(f"{GREEN}Directory '{name}' created.{RESET}")
    except FileExistsError:
        print(f"{DIM}mkdir:{RESET} cannot create directory '{name}': File exists")

def change_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"{DIM}cd:{RESET} no such file or directory: {path}")
    except NotADirectoryError:
        print(f"{DIM}cd:{RESET} not a directory: {path}")

def remove_item(name):
    if not os.path.exists(name):
        print(f"{DIM}rm:{RESET} no such file or directory: {name}")
        return

    try:
        if os.path.isdir(name):
            shutil.rmtree(name)
            print(f"Removed directory '{name}'")
        else:
            os.remove(name)
            print(f"Removed file '{name}'")
    except Exception as e:
        print(f"Error: {e}")

def run_nvim(filename):
    try:
        subprocess.run(["nvim", filename])
    except FileNotFoundError:
        print(f"{DIM}nvim:{RESET} Neovim not found. Install it or update PATH.")

def run_shell():
    print(f"{GREEN}Welcome to pyshell🐍{RESET}")
    while True:
        current_dir = os.path.basename(os.getcwd()) or "/"
        command_input = input(f"{BLUE}{current_dir}{RESET} $ ").strip()

        if not command_input:
            continue

        parts = command_input.split()
        command = parts[0]
        args = parts[1:]

        if command == "exit":
            print(f"{GREEN}Exiting pyshell cya👋{RESET}")
            break
        elif command == "ls":
            list_dir()
        elif command == "mkdir" and args:
            make_dir(args[0])
        elif command == "cd" and args:
            change_dir(args[0])
        elif command == "rm" and args:
            remove_item(args[0])
        elif command == "nvim" and args:
            run_nvim(args[0])
        else:
            print(f"{DIM}Unknown command:{RESET} {command}")

if __name__ == "__main__":
    run_shell()
