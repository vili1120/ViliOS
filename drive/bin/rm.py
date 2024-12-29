import os

def main(arg1=None, arg2=None):
    protected_dir = "/home/vili1120/Projects/OS/drive/bin"

    if os.getcwd() != protected_dir:
        if not arg1:
            print("Error: No file or directory specified to remove.")
            return

        if arg2:
            arg2 = os.path.abspath(arg2)

        if arg1.startswith('-'):
            flags = arg1
            if not arg2:
                print("Error: No target specified to remove.")
                return
            target = os.path.abspath(arg2)
        else:
            flags = ""
            target = os.path.abspath(arg1)

        if target == protected_dir or target.startswith(protected_dir + os.sep):
            print(f"Error: Cannot remove '{target}' because it is the protected 'bin' directory or within it.")
            return

        command = f"rm {flags} {target}"

        try:
            result = os.system(command)
            if result != 0:
                print(f"Failed to remove: {target}")
            else:
                print(f"Successfully removed: {target}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Error: Cannot perform operations in the protected 'bin' directory.")
