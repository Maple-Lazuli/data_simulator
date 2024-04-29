from data_simulator.format import Format


class Integer(Format):
    def __init__(self, data, endianess='big', size=1, signed=False):
        Format.__init__(self, data, endianess)
        self.size = size
        self.signed = signed

    def get_bytes(self):
        return int(self.data).to_bytes(length=self.size, byteorder=self.endianess, signed=self.signed)

    def get_hex_dump(self):
        byte_array = self.get_bytes()
        hex_dump = [hex(b)[2:].zfill(2) for b in byte_array]
        return " ".join(hex_dump)


class S(Integer):
    def __init__(self, data, e='b', size=1):
        endian = "big" if e == 'b' else 'little'
        Integer.__init__(self, data, endian, size, True)


class U(Integer):
    def __init__(self, data, e='b', size=1):
        endian = "big" if e == 'b' else 'little'
        Integer.__init__(self, data, endian, size, False)
