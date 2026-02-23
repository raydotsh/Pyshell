import os
import importlib

BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"
DIM = "\033[90m"

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

        try:
            module = importlib.import_module(f"commands.{command}")
            module.run(args)
        except ModuleNotFoundError:
            print(f"{DIM}Unknown command:{RESET} {command}")
        except AttributeError:
            print(f"{DIM}Command '{command}' is broken (no run function){RESET}")

if __name__ == "__main__":
    run_shell()
