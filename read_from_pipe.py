# https://lyceum-allotments.github.io
# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-3-pipes-in-python/
# read_from_pipe.py
# with open("my_pipe", "r", 0) as f:
with open("my_pipe", "r") as f:
    print("have opened pipe, commencing reading....")
    for l in f:
        print(l,)
