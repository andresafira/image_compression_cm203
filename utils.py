import numpy as np


def get_inv_binary_associate(i: int, size: int) -> int:
    """
    Get the binary representation of a number, invert it and then convert it
    back to decimal base (operation needed to perform the bitwise inversion
    of the array index position
    :param i: array index
    :param size: maximum size of the binary value (since the bitwise inversion
    depends on the representation size: inverse(00001) = 10000 = 2^size - 1)
    :return: bitwise inverted index position
    """
    binary = bin(i)[2:].rjust(size, '0')
    return int(binary[::-1], 2)


def swap(arr: np.ndarray, index1: int, index2: int):
    """
    Swap two given array positions.
    :param arr: array to get swapped
    :param index1: first index
    :param index2: second index
    """
    arr[index1], arr[index2] = arr[index2], arr[index1]


def bitwise_invert(arr: np.ndarray, n: int, log_n: int) -> np.ndarray:
    """
    Performs the bitwise inversion of the array indices, which leads each index
    to the index with its inverted representation in binary base.
    :param arr: array to be bitwise inverted
    :param n: the size of the array
    :param log_n: the logarithm in base 2 of n
    :return: the bitwise inverted array
    """
    to_change = set(range(n))
    for i in range(n):
        if i not in to_change:
            continue
        i2 = get_inv_binary_associate(i, log_n)
        swap(arr, i, i2)
        to_change.remove(i)
        if i != i2:
            to_change.remove(i2)
    return arr
