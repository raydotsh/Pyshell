# commands/nvim.py
import subprocess

def run(args):
    if not args:
        print("nvim: missing file operand")
        return
    try:
        subprocess.run(["nvim"] + args)
    except FileNotFoundError:
        print("nvim: not found. Install Neovim or update PATH.")
