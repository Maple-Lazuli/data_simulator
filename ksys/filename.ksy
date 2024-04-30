meta:
  id: filename_record
  endian: be
seq:
  - id: filenames
    type: filename
   # repeat: eos
types:
  filename:
    seq:
      - id: name
        type: str
        size: 8
        encoding: ASCII
      - id: ext
        type: str
        size: 3
        encoding: ASCII