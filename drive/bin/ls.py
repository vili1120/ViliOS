import os

def main(arg1=None, arg2=None):
    if arg1:
        return os.system(f"ls {arg1}")
    else:
        return os.system("ls")
