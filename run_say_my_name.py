# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-5-subprocesses-and-pipes/
# run_say_my_name.py

import subprocess
import sys

proc = subprocess.Popen(["python", "say_my_name.py"])

while proc.returncode is None:
    proc.poll()
