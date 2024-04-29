def hex_dump(string, endianess='be'):
    byte_array = bytes(string, 'utf-8')
    str_array = [hex(b)[2:].zfill(2).upper() for b in byte_array]
    if endianess == 'le':
        str_array = str_array[::-1]
    return " ".join(str_array)


class Format:
    def __init__(self, data, endianess='be'):
        self.data = data
        self.endianess = endianess

    def get_bytes(self):
        return bytes(self.data, 'utf-8')

    def get_hex_dump(self):
        return hex_dump(self.data, self.endianess)

    def __and__(self, other):
        return self.get_hex_dump() + " " + other.get_hex_dump()

    def __or__(self, other):
        return self.get_bytes() + other.get_bytes()
