import numpy as np
import math
from fft import fft2, ifft2


def type_adjustment(img: np.ndarray) -> np.ndarray:
    """
    Adjusts the image type and clips the value to stay between the range 0 - 255.
    :param img: input image
    :return: adjusted image
    """
    clipped = np.maximum(np.minimum(img, 255), 0)
    return np.floor(clipped).astype(np.uint8)


def expand(img: np.ndarray) -> np.ndarray:
    """
    Expand the image size two the next power of two, by padding the original image with
    zeros
    :param img: 2-dimensional vector that represents the image to be padded
    :return: the padded image
    """
    # The new nx and ny (next powers of 2)
    nx, ny = 2 ** (int(math.ceil(np.log2(img.shape[0])))), 2 ** (int(math.ceil(np.log2(img.shape[1]))))
    new_img = np.zeros((nx, ny))
    new_img[:img.shape[0], :img.shape[1]] = img.copy()
    return new_img


def contract(img: np.ndarray, original_shape: tuple) -> np.ndarray:
    """
    Contract the image size to its original shape
    :param img: 2-dimensional array that represents the image to be contracted
    :param original_shape: the original image shape
    :return: the contracted image
    """
    return img[:original_shape[0], :original_shape[1]].copy()


def compress(img: np.ndarray, compression_factor: float, tech: str = "recursive") -> np.ndarray:
    """
    Coordinates the compression operation, by transforming the monotone image (three or more color channels),
    removing the excessive information and then after, performing the inverse transformation
    :param img: n-dimensional vector to be compressed (n > 2)
    :param compression_factor: represents the compression ratio. A compression_factor of 100
    means the compressed image will be 100 times smaller
    :param tech: technique involved in the fourier transform algorithm (can be 'recursive' or 'inplace')
    :return: the compressed image
    """
    shape = img.shape
    if len(shape) == 2:
        return type_adjustment(compress_monotone(img, compression_factor, tech))
    elif len(shape) != 3:
        raise ValueError("image shape must have 2 or 3 dimensions")

    compressed_img = np.zeros(shape)
    for channel in range(shape[2]):
        compressed_img[:, :, channel] = compress_monotone(img[:, :, channel], compression_factor, tech)
    return type_adjustment(compressed_img)


def compress_monotone(img: np.ndarray, compression_factor: float, tech: str = "recursive") -> np.ndarray:
    """
    Coordinates the compression operation, by transforming the monotone image (only one color channel),
    removing the excessive information and then after, performing the inverse transformation
    :param img: 2-dimensional vector to be compressed
    :param compression_factor: represents the compression ratio. A compression_factor of 100
    means the compressed image will be 100 times smaller
    :param tech: technique involved in the fourier transform algorithm (can be 'recursive' or 'inplace')
    :return: the compressed image
    """
    # Expand the original image to have sizes as powers of 2
    original_shape = img.shape
    expanded_img = expand(img)

    # Get the transformed image
    F_img = fft2(expanded_img, tech)

    # Order and filter the coefficients by size (absolute value)
    F_img_sorted = np.sort(np.abs(F_img), axis=None)[::-1]
    thres_index = int(len(F_img_sorted) // compression_factor)
    threshold = F_img_sorted[thres_index]
    compressed_img = F_img * (np.abs(F_img) > threshold)

    # Revert the transformation and contract the image to its original shape
    IF_img = ifft2(compressed_img, tech)
    final_img = contract(IF_img, original_shape)
    return type_adjustment(final_img.real)
