#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """UTF-8 Validation
    """
    # convert data to binary string
    binary_str: str = ""

    for i in datia:
        bin_str = bin(i)[2:]
        bin_str = bin_str.zfill(8)
        binary_str += bin_str

    # check if binary string is valid
    if binary_str[0] == "0" and len(binary_str) == 8:
        return True
    # if length is  16
    if binary_str[8:10] == "10":
        if binary_str[0:3] == "110":
            return True

        # if length is 24
        if binary_str[16:18] == "10":
            if binary_str[0:4] == "1110":
                return True

            # if lenght is 32
            if binary_str[0:5] == "11110" and binary_str[24:26] == "10":
                return True
    return False
