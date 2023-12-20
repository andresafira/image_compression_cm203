# Image Compression

## fft Module

In this module, the basic implementations of functions to be used are included, along with auxiliary functions to facilitate code implementation and readability. Below is a description of the main functions implemented in the FFT module:

- [ ]  ```fft(x, inv=1)```: Function that performs the fast Fourier transform of a one-dimensional vector with a size corresponding to a power of two, using the recursive algorithm.

- [ ] ```fft_inplace(x, inv=1)```: Function that performs the fast Fourier transform of a one-dimensional vector with a size corresponding to a power of two, using the algorithm that performs the transforms in the vector itself, without using recursion, optimizing memory allocation.

- [ ] ```fft2(img, tech)```: Function that performs the fast Fourier transform of a two-dimensional vector with a size corresponding to a power of two, using the algorithm chosen through its parameter *tech*. It first performs the transform on its rows and then on the columns of the vector.

- [ ] ```ifft(X)```: Function that performs the fast inverse Fourier transform of a one-dimensional vector with a size corresponding to a power of two, using the recursive algorithm. It uses the implementation of ```fft()``` with the parameter $inv = -1$ and divides by the size of the vector at the end.

- [ ] ```ifft_inplace(X)```: Function that performs the fast inverse Fourier transform of a one-dimensional vector with a size corresponding to a power of two, using the algorithm that performs the transforms in the vector itself, without using recursion, optimizing memory allocation. It uses the implementation of ```fft_inplace()``` with the parameter $inv = -1$ and divides by the size of the vector at the end.

- [ ] ```ifft2(img, tech)```: Function that performs the fast inverse Fourier transform of a two-dimensional vector with a size corresponding to a power of two, using the algorithm chosen through its parameter *tech*. To reverse the effect of ```fft2()```, this function first performs the inverse transforms with respect to the columns and then with respect to the rows, dividing by the size of the vector at the end.



## image Module

This module is responsible for processing images to prepare them for compression techniques, adjusting the output state (removing complex numbers and adjusting the image type), as well as performing compression and color channel adjustments. The functions used are listed below:

- [ ] ```type_adjustment(img)```: Adjusts the output image to limit values to the supported pixel color range: $[0, 255]$, and adjusts the output type to $np.uint8$, which is accepted by the PIL image library.

- [ ] ```expand(img)```: Expands the dimensions of the image to the nearest power of two, to use the developed techniques. The added values are 0 by default.

- [ ] ```contract(img, original_shape)```: Contracts the image, undoing the operation of the previous function.

- [ ] ```compress(img, compression_factor, tech)```: Performs compression of the image with possibly more than one color channel, according to the technique specified in the Introduction using the algorithm specified by the $tech$ parameter, which can be $recursive$ or $inplace$.

- [ ] ```compress_monotone(img, compression_factor, tech)```: Performs compression of the image with exclusively one color channel (the image must be one-dimensional), according to the technique specified in the Introduction using the algorithm specified by the $tech$ parameter, which can be $recursive$ or $inplace$.


## utils Module

This additional module contains the implementation of some functions not necessarily related, used in other modules to facilitate code application and readability. The implemented functions are:

- [ ] ```get_inv_binary_associate(i, size)```: Calculates the number whose binary representation reversed is equal to the binary representation of the parameter $i$. This function is used to perform the bitwise inversion operation used in the inplace algorithm. The $size$ parameter is necessary because some inverse representations may be different, depending on how many bits are available for number allocation, for example: $(0001)_2^{-1} = (1000)_2 \neq (1)_2 = (1)_2^{-1}$ even though $(0001)_2 = (1)_2$.

- [ ] ```swap(arr, index1, index2)```: Swaps the content of indices $index1$ and $index2$ of the array $arr$.

- [ ] ```bitwise_invert(arr, n, log_n)```: Performs the bitwise inversion operation on the array $arr$. This occurs when the content of position $i$ is moved to the position whose binary representation is the reverse of the binary representation of $i$.