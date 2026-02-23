import os
import time

def ls(show_hidden=False):
    entries = os.listdir('.')
    if not show_hidden:
        entries = [e for e in entries if not e.startswith('.')]
    
    for e in sorted(entries):
        if os.path.isfile(e):
            size = os.path.getsize(e)
            mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(e)))
            print(f"FILE {size:>8} bytes  {mtime}  {e}")
        elif os.path.isdir(e):
            print(f"DIR  {'-'*8}        {'-'*19}  {e}")

def run(args):
    show_hidden = "-a" in args
    ls(show_hidden)


