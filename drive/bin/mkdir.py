import os

def main(arg1=None, arg2=None):
    protected_dir = f"{os.getcwd}/bin"

    if os.getcwd() != protected_dir:
        target = os.path.abspath(arg1)
        if target != protected_dir and not target.startswith(protected_dir + os.sep):
            os.system(f"mkdir {target}")

