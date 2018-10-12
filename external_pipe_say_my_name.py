# external_pipe_say_my_name.py
# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-5-subprocesses-and-pipes/

import subprocess
import sys

with open("input_pipe", "r") as input_pipe:
    with open("output_pipe", "wb", 0) as output_pipe:
    # with open("output_pipe", "w", 0) as output_pipe:
        proc = subprocess.Popen(["python3", "say_my_name.py"],
            stdin=input_pipe, stdout=output_pipe)

        while proc.returncode is None:
            proc.poll()
