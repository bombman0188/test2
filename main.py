import time
import os
import toml
import subprocess
import sys
from watchdog import Watchdog, ProcessHandler


def debug(msg):
    print(msg)

branch = "won0"
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

class MyHandler(ProcessHandler):
    def on_killed(self):
        debug("process killed..")

    def on_message(self, msg):
        debug(f"MSG: {msg}")

def main():
    watchdog = Watchdog(['python', '-u', 'test.py'])
    watchdog.start(MyHandler())

    while True:
        print("ping....")
        time.sleep(3)
        if check():
            break


if __name__ == "__main__":
    main()


    # subprocess.check_output(["git", "pull"])
