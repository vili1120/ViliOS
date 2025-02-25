import importlib
import sys
import os

LOAD_RAMFS = input("DIR to load> ")

os.system("clear")

drive_dir = os.path.join(os.path.dirname(__file__), LOAD_RAMFS)
if os.path.exists(drive_dir):
    os.chdir(drive_dir)
else:
    os.mkdir(drive_dir)
    os.system(f"cp -r drive/* {drive_dir}/")
    os.chdir(drive_dir)

sys.path.append(os.path.join(drive_dir, 'bin'))

def get_dir():
    current_dir = os.getcwd()
    
    if current_dir.startswith(drive_dir):
        relative_dir = '/' + current_dir[len(drive_dir):].lstrip('/')
    else:
        relative_dir = current_dir

    print(f"{relative_dir}")

Run = True

def run(program, arg1=None, arg2=None, root=None):
    global Run
    if program in ("exit", "shutdown"):
        Run = False
    elif program == "reset":
        os.system(f"rm -rf {drive_dir}")
        Run = False
    else:
        try:
            module = importlib.import_module(program)
            if hasattr(module, 'main'):
                if root:
                    module.main(arg1, arg2, root)
                elif not root:
                    module.main(arg1, arg2)
            else:
                print(f"Shell: {program} does not have a main method.")
        except ModuleNotFoundError:
            print(f"Shell: {program} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

run("login", root=drive_dir)
run("startup")

PROMPT = importlib.import_module("PROMPT")

while Run:
    if not os.getcwd().startswith(drive_dir):
        os.chdir(drive_dir)
    
    get_dir()
    user_input = input(f"{PROMPT.prompt}> ")
    parts = user_input.split()
    program = parts[0]
    arg1 = parts[1] if len(parts) > 1 else None
    arg2 = parts[2] if len(parts) > 2 else None
    if program in ["adduser", "login", "programs"]:
        run(program, arg1, arg2, drive_dir)
    else:
        run(program, arg1, arg2)
