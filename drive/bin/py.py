import os

def main(arg1=None, arg2=None):
	if arg1:
		os.system(f"pypy3 {arg1}")
	else:
		os.system("pypy3")
