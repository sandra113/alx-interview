#!/usr/bin/python3


def validUTF8(data):
    # Variable to track the number of bytes expected for the next character
    bytes_to_follow = 0
    
    for byte in data:
        # Check if this byte is a continuation byte (starts with '10')
        if bytes_to_follow > 0:
            # If the byte does not start with '10', it's an invalid continuation byte
            if (byte >> 6) != 0b10:
                return False
            bytes_to_follow -= 1
        else:
            # Determine the number of bytes expected for the next character
            if byte >> 7 == 0:
                bytes_to_follow = 0  # 1-byte character, no continuation bytes
            elif byte >> 5 == 0b110:
                bytes_to_follow = 1  # 2-byte character, 1 continuation byte
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2  # 3-byte character, 2 continuation bytes
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3  # 4-byte character, 3 continuation bytes
            else:
                return False  # Invalid UTF-8 prefix
            
    # If there are still bytes expected for a character after iterating through all data,
    # it means the data is incomplete and invalid
    return bytes_to_follow == 0

# Example usage:
data = [197, 130, 1]  # Represents the string 'ñ' encoded in UTF-8
print(validUTF8(data))  # Output: True

