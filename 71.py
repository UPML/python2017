import string


def strings(filename, min_str_len=4):
    with open(filename, 'rb') as in_file:
        result = ''
        try:
            while True:
                text = in_file.read(10000)
                if len(text) == 0: # костыль для b''
                    break
                for c in map(chr, text):
                    if c in string.printable:
                        # print(c)
                        result += c
                    else:
                        if len(result) > min_str_len:
                            yield result
                        result = ''

        finally:
            if len(result) > min_str_len:
                yield result


# print(list(strings('scoring_network_dump.bin')))