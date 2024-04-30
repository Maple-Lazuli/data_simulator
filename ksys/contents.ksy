meta:
  id: valid_record
  endian: be
seq:
  - id: magic1
    contents: JFIF
    # expects bytes: 4A 46 49 46
  - id: magic2
    # we can use YAML block-style arrays as well
    contents:
      - 0xca
      - 0xfe
      - 0xba
      - 0xbe
    # expects bytes: CA FE BA BE
  - id: magic3
    contents: [CAFE, 0, BABE]
    # expects bytes: 43 41 46 45 00 42 41 42 45