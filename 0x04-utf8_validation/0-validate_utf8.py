#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0
    # Masks to check the most significant bits of a byte
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    # Get the least significant 8 bits of the integer
    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:
             # Check how many leading 1s there are in the current byte
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

             # If n_bytes is 0, this is a 1-byte character
            if number_bytes == 0:
                continue

             # If n_bytes is greater than 4 or 1, it's invalid
            if number_bytes == 1 or number_bytes > 4:
                return False

        # For the remaining bytes, check if they start with '10'
        else:
            if not (i & mask_1 and not (i & mask_2)):
                    return False

        # Decrement the count of bytes to process
        number_bytes -= 1

    # If all bytes have been processed correctly, n_bytes should be 0
    if number_bytes == 0:
        return True

    return False
