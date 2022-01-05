import time
import os
import toml
import subprocess
import sys

def debug(msg):
    print(msg)

branch = "main"
if len(sys.argv) > 1:
    branch = sys.argv[1]

def check():
    subprocess.check_output(["git", "fetch"])
    ret = subprocess.check_output(["git", "diff", branch, f"origin/{branch}"])
    if ret == b"":
        return False
    else:
        return True


def update():
    subprocess.check_output(["git", "pull"])

    if os.path.exists("requirements.txt"):
        print("pip install -r requirements.txt")
        subprocess.check_output(["python", "-m", "pip", "install", "-r", "requirements.txt"])

    if os.path.exists("setup.py"):
        print("python setup.py install")
        subprocess.check_output(["python", "setup.py", "install"])

       
        
while True:
    time.sleep(10)
    if check():
        break

    # subprocess.check_output(["git", "pull"])
