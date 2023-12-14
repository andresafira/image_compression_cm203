import numpy as np
import math
from utils import bitwise_invert


def fft(x: np.ndarray, inv: int = 1) -> np.ndarray:
    """
    Performs the discrete fourier transform, according to Cooley-Tukey FFT Recursive
    algorithm for the 1-dimensional vector of points given
    :param x: 1-dimensional vector of points to make the Fourier Transform.
    :param inv: parameter that represents the type of transform, 1 for forward transform
    and -1 for the inverse transform.
    :return: the discrete fourier transform of the vector x
    """
    n = x.shape[0]

    # Base case for the recursive logic
    if n == 1:
        return x

    # The even and odd extensions of the transform
    x_even = fft(x[::2], inv)
    x_odd = fft(x[1::2], inv)
    factor = np.array([np.exp(-2j * math.pi * omega / n * inv) for omega in range(int(n / 2))])
    return np.concatenate([x_even + factor * x_odd,
                           x_even - factor * x_odd])


def ifft(X: np.ndarray) -> np.ndarray:
    """
    Performs the inverse fourier transform of the 1-dimensional vector X. It utilizes the
    same logical structure of the Recursive FFT forward function, but only inverts the
    exponent sign and divides the final result by N (len(X))
    :param X: 1-dimensional vector to be transformed by the ifft
    :return: the inverse fourier transform of vector X
    """
    return fft(X, inv=-1) / X.shape[0]


def fft2(img: np.ndarray, tech: str = "recursive") -> np.ndarray:
    """
    Performs the Fourier Transform of a 2-dimensional array by making two successive
    fft's, by rows and columns, in order.
    :param img: 2-dimensional vector that represents the image
    :param tech: technique involved in the fft algorithm (can be 'recursive' or 'inplace')
    :return: transformed vector
    """
    if tech == "recursive":
        FFT = fft
    elif tech == "inplace":
        FFT = fft_inplace
    else:
        raise ValueError(f"{tech} is not a valid parameter, it must be 'recursive' or 'inplace'")

    Nx, Ny = img.shape
    fft_1 = np.array([FFT(img[i]) for i in range(Nx)])
    fft_2 = np.array([FFT(fft_1[:, i]) for i in range(Ny)]).T
    return fft_2


def ifft2(img: np.ndarray, tech: str = "recursive") -> np.ndarray:
    """
    Performs the Inverse Fourier Transform of a 2-dimensional array by reversing the
    two successive fft's made, by columns and rows, in order.
    :param img: 2-dimensional vector that represents the image to be inverted
    :param tech: technique involved in the ifft algorithm (can be 'recursive' or 'inplace')
    :return: transformed vector
    """
    if tech == "recursive":
        IFFT = ifft
    elif tech == "inplace":
        IFFT = ifft_inplace
    else:
        raise ValueError(f"{tech} is not a valid parameter, it must be 'recursive' or 'inplace'")

    Nx, Ny = img.shape
    ifft_1 = np.array([IFFT(img[:, i]) for i in range(Ny)]).T
    ifft_2 = np.array([IFFT(ifft_1[i]) for i in range(Nx)])
    return ifft_2


def fft_inplace(x: np.ndarray, inv: int = 1) -> np.ndarray:
    """
    Performs the Fourier Transformation using a non-recursive, inplace method.
    :param x: the vector to be transformed
    :param inv: an indicator for forward (1) or inverted(-1) transform
    :return: the transformed vector
    """
    # Perform the bitwise inversion
    n = x.shape[0]
    log_n = int(np.log2(n))
    x = bitwise_invert(x.astype(complex), n, log_n)

    # Make the transformation by steps
    for scale in range(1, log_n+1):
        step = int(2**scale)
        for index in range(0, n, step):
            x_even = x[index:index + step // 2]
            x_odd = x[index + step//2:index + step]
            factor = np.array([np.exp(-2j*math.pi*omega/step * inv) for omega in range(step // 2)])
            x[index:index + step] = np.concatenate([x_even + factor * x_odd, x_even -factor * x_odd])
    return x


def ifft_inplace(X: np.ndarray) -> np.ndarray:
    """
    Performs the Inverse Fourier Transformation using a non-recursive, inplace method.
    :param X: the vector to be transformed
    :return: the transformed vector
    """
    return fft_inplace(X, -1) / X.shape[0]
