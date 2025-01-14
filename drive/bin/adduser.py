import os

def main(arg1=None, arg2=None, root=None):
    def cuser(name, pwd):
        with open(f"{root}/bin/user.py", "w+") as file:
            file.write('user_root = "root root"\n')
            file.write(f'user1 = "{name} {pwd}"')
        file.close()

    if arg1:
        os.system(f"mkdir {root}/home")
        os.system(f"mkdir {root}/home/{arg1}")
        PASSWORD = input("Password> ")
        cuser(arg1, PASSWORD)
    elif not arg1:
        USERNAME = input("Username> ")
        PASSWORD = input("Password> ")
        os.system(f"mkdir {root}/home")
        os.system(f"mkdir {root}/home/{USERNAME}")
        cuser(USERNAME, PASSWORD)
