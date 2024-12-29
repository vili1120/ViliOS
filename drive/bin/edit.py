import os

def main(arg1=None, arg2=None):
    if arg1:
        os.system(f"nano {arg1}")
    else:
        os.system("nano")
