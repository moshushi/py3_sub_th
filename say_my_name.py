# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-5-subprocesses-and-pipes/
# say_my_name.py

import sys
print("what's your name?")
for name in iter(sys.stdin.readline, ''):
    name = name[:-1]
    if name == "exit":
        break
    print("Whell how do you do {0}?".format(name))
    print("What's your name?")
