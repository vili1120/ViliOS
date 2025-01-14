import os
import time
from user import *

uroot = user_root.split()
User = user1.split()

def main(arg1=None, arg2=None, root=None):
    os.system("clear")
    print("Please login")
    USER = input("username> ")
    PWD = input("password> ")

    if USER == uroot[0]:
        if PWD == uroot[1]:
            with open(f"{root}/bin/PROMPT.py", "w+") as file:
                file.write(f"prompt = '{USER}'")
            file.close()
            os.system("clear")
        else:
            print("Wrong password")
            time.sleep(0.5)
            main()
    elif USER == User[0]:
        if PWD == User[1]:
            with open(f"{root}/bin/PROMPT.py", "w+") as file:
                file.write(f"prompt = '{USER}'")
            file.close()
            os.system("clear")
        else:
            print("Wrong password")
            time.sleep(0.5)
            main()
    else:
        print(f"{USER} is not an user")
        time.sleep(0.5)
        main()
