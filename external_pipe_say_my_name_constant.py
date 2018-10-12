# external_pipe_say_my_name_constant.py
# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-5-subprocesses-and-pipes/

import subprocess

with open("output_pipe", "wb", 0) as output_pipe:
    proc = subprocess.Popen(["stdbuf", "-o0", "python3", "say_my_name.py"],
        stdin=subprocess.PIPE, stdout=output_pipe)
    
    while True:
        proc.poll()
        if proc.returncode is not None:
            break
        with open("input_pipe", "r") as input_pipe:
            proc.stdin.write(input_pipe.read().encode('utf-8'))
    # with open("output_pipe", "w", 0) as output_pipe:

