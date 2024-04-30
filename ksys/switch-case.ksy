meta:
  id: case_record
  endian: be
seq:
  - id: fourcc
    type: u4le
    enum: pixel_formats
  - id: len
    type: u4
  - id: body
    size: len
    type:
      switch-on: fourcc
      cases:
        1: block_rgb2
        2: block_rle4
        3: block_rle8
        _: rec_other