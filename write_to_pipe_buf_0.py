# https://lyceum-allotments.github.io
# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-4-on-the-buffers/
# write_to_pipe_buf_0.py
# В отличии от python2 необходимо указание `b` - бинарный мод, для использования буферинга с опцией 0 и кодировать строку в байты

import time
message = "hello to a pipe\n"

with open("my_pipe", "wb", buffering=0) as f:
    print("have opened pipe, commencing writing....")
    for c in message:
        f.write(c.encode('utf-8'))
        print ("have sent a letter")
        time.sleep(1)
