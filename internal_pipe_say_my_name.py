# internal_pipe_say_my_name.py
# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-5-subprocesses-and-pipes/

import subprocess
import sys

proc = subprocess.Popen(["python3", "say_my_name.py"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

proc.stdin.write(("matthew\n").encode('utf-8'))
proc.stdin.write(("mark\n").encode('utf-8'))
proc.stdin.write(("luke\n").encode('utf-8'))
proc.stdin.close()

while proc.returncode is None:
    proc.poll()

print("I got back from the program this:\n{0}".format(proc.stdout.read().decode('utf-8')))
