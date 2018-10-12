# https://lyceum-allotments.github.io
# https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-3-pipes-in-python/
# write_to_pipe.py
# В отличии от python2 необходимо указание `b` - бинарный мод, для использования буферинга с опцией 0 и кодировать строку в байты

with open("my_pipe", "wb", buffering=0) as f:
    print("have opened pipe, commencing writing....")
    f.write(("hello through a pipe\n").encode('utf-8'))
