#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Check if a byte string is a valid UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        # Binary representation of number as string of bits
        binary_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            # Count number of leading 1 in first byte
            for bit in binary_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1-byte character (ASCII), if n_bytes is 0
            if n_bytes == 0:
                continue

            # Invalid case
            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            # If the byte doesn't start with 10, then it's invalid
            if not (binary_rep[0] == '1' and binary_rep[1] == '0'):
                return False

        # One byte in this character's multi-byte sequence
        n_bytes -= 1

    # If n_bytes is not 0, it's invalid
    return n_bytes == 0
