from data_simulator.format import Format


class Bit(Format):
    def __init__(self, val, size, endianess='be'):
        Format.__init__(self, None, "big" if endianess == 'be' else 'little')
        if type(val) == int:
            self.bits = bin(val)[2:].zfill(size)
        elif type(val) == str:
            self.bits = val
        self.size = size

    def get_bytes(self):
        return int(self.bits,2).to_bytes(length=1, byteorder=self.endianess)

    def get_hex_dump(self):
        byte_array = self.get_bytes()
        hex_dump = [hex(b)[2:].zfill(2) for b in byte_array]
        return " ".join(hex_dump)

    def __sub__(self, other):
        return Bit(self.bits + other.bits, self.size + other.size)
