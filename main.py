import time
import os
import toml
import subprocess


def check():
    if not os.path.exists(self.local_path):
        return True

    subprocess.check_output(["git", "fetch"])
    ret = subprocess.check_output(["git", "diff", "main", "origin/main"])
    if ret == b"":
        return False
    else:
        return True


def update():
    subprocess.check_output(["git", "pull"], cwd=self.local_path)

    if os.path.exists("requirements.txt"):
        print("pip install -r requirements.txt")
        subprocess.check_output(["python", "-m", "pip", "install", "-r", "requirements.txt"])

    if os.path.exists("setup.py"):
        print("python setup.py install")
        subprocess.check_output(["python", "setup.py", "install"])

while True:
    time.sleep(10)
    print(check())

    # subprocess.check_output(["git", "pull"])
