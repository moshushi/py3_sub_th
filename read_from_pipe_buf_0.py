import sys

with open("my_pipe", "r") as f:
    print("have opened pipe, commencing reading....")
    while 1:
        c = f.read(1)
        if c:
            sys.stdout.write(c)
            sys.stdout.flush()
        else:
            break
