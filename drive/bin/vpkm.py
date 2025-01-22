import os
import requests

repo = "https://raw.githubusercontent.com/vili1120/ViliOS/main"

def main(arg1=None, arg2=None):
    if arg1 == "add" and arg2:
        x = f"{repo}/{arg2}.py"
        filed = requests.get(x)
        if filed.status_code == 200:
            with open(f"{arg2}.py", "wb") as file:
                file.write(filed.content)
