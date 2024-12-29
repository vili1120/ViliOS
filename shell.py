import importlib
import sys
import os

os.system("clear")

drive_dir = os.path.join(os.path.dirname(__file__), 'drive')
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

def run(program, arg1=None, arg2=None):
    global Run
    if program in ("exit", "shutdown"):
        Run = False
    else:
        try:
            module = importlib.import_module(program)
            if hasattr(module, 'main'):
                module.main(arg1, arg2)
            else:
                print(f"Shell: {program} does not have a main method.")
        except ModuleNotFoundError:
            print(f"Shell: {program} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

run("startup")

while Run:
    if not os.getcwd().startswith(drive_dir):
        os.chdir(drive_dir)

    get_dir()
    user_input = input("cmd> ")
    parts = user_input.split()
    program = parts[0]
    arg1 = parts[1] if len(parts) > 1 else None
    arg2 = parts[2] if len(parts) > 2 else None
    run(program, arg1, arg2)
