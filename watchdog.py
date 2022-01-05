from subprocess import Popen, check_output, PIPE
import threading
import time

def debug(msg):
    print(msg)

class Job(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None):
        threading.Thread.__init__(self, name=name)

        self.target = target
        self.args = args
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()

        # ... Other thread setup code here ...

    def run(self):
        debug('Watchdog #%s started' % self.ident)
        while not self.shutdown_flag.is_set():
            # ... Job code here ...
            self.target(*self.args)
            time.sleep(0.5)
        # ... Clean shutdown code here ...
        debug('Watchdog #%s stopped' % self.ident)

class ProcessHandler:
    def on_killed(self):
        return

    def on_message(self, msg):
        return

class Watchdog:
    def __init__(self, args):
        self.args = args
        self.thread = None
        return

    def run(self, handler : ProcessHandler):
        print(1)
        while True:
            process = Popen(self.args, stdout=PIPE, universal_newlines=True)
            while True:
                if process.poll() is not None:
                    break

                line = process.stdout.readline()
                line = line.rstrip().lstrip()
                if line != "":
                    handler.on_message(line)

            handler.on_killed()

    def start(self, handler : ProcessHandler):
        self.thread = Job(target=self.run, args=(handler,))
        self.thread.daemon = True
        self.thread.start()
        return

    def stop(self):
        self.thread.shutdown_flag.set()
