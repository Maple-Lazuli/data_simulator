meta:
  id: valid_record
  endian: be
seq:
  # Full form of equality constraint: the only valid value is 0x42
  - id: exact_value1
    type: u1
    valid:
      eq: 0x42

  # Shortcut for the above: the only valid value is 0x42
  - id: exact_value2
    type: u1
    valid: 0x42

  # Value must be at least 100 and at most 200
  - id: bounded_value
    type: u2
    valid:
      min: 100
      max: 200

  # Value must be one of 3, 5, or 7
  - id: enum_constraint_value
    type: u4
    valid:
      any-of: [3, 5, 7]