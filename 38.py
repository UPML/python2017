import binascii
import base64
from urllib import parse
with open('input.txt') as f:
    for file1 in f:
        file1 = file1[22:]
        file1 = str(file1)
        file2 = binascii.unhexlify(file1)[31:]
        file3 = base64.b64decode(file2)[21:]
        file4 = file3.decode('utf8')[26:]
        for i in range(10):
            file4 = parse.unquote(file4)
        print(file4[169:])