#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """UTF-8 Validation
    """
    # convert data to binary string
    binary_str: str = arr_to_binary(data)

    if len(binary_str) > 32:
        for i in range(0, int(len(binary_str) / 8)):
            if binary_str[i * 8] == "1":
                return False
        return True

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


def arr_to_binary(arr: list[int]) -> str:
    """Array to octet Binary
    """
    binary_str: str = ""

    # convert array to binary string
    for i in arr:
        bin_str = bin(i)[2:]
        bin_str = bin_str.zfill(8)
        binary_str += bin_str

    return binary_str
