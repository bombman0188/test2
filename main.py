import time
import os
import toml
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def debug(msg):
    print(msg)

branch = "main"
if len(sys.argv) > 1:
    branch = sys.argv[1]

def check():
    # 서버 업데이트 시 변경하기
    if branch == "main":
        # return False
        pass

    subprocess.check_output(["git", "fetch"])
    ret = subprocess.check_output(["git", "diff", branch, f"origin/{branch}"])
    if ret == b"":
        return False
    else:
        return True

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event) # Your code here


while True:
    print("ping....")
    time.sleep(3)
    if check():
        break

    # subprocess.check_output(["git", "pull"])
