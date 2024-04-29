from data_simulator.format import Format


def hex_dump(byte_array):
    str_array = [hex(b)[2:].zfill(2).upper() for b in byte_array]
    return " ".join(str_array)


def convert_bytes(string, encoding, size):
    bytes_array = bytes(string, encoding)
    if size == -1:
        return bytes_array
    elif (size - len(bytes_array)) >= 0:
        difference = size - len(bytes_array)
        return bytes(difference) + bytes_array
    else:
        return bytes_array[0:size]


class String(Format):
    def __init__(self, data, endianess, size, encoding):
        Format.__init__(self, data, endianess)
        self.size = size
        self.encoding = encoding

    def get_bytes(self):
        byte_array = bytes(self.data, self.encoding)
        if self.endianess == 'le':
            byte_array = byte_array[::-1]
        return byte_array

    def get_hex_dump(self):
        byte_array = bytes(self.data, self.encoding)
        dump = hex_dump(byte_array)
        if self.endianess == 'le':
            dump = dump[::-1]
        return dump


class Unicode(String):
    def __init__(self, data, endianess='be', size=-1, encoding='utf-8'):
        String.__init__(self, data, endianess, size, encoding)
