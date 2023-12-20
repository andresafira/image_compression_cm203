from PIL import Image
from image import compress
from fft import fft, fft_inplace
import numpy as np
import time


def main():
    # actions
    compress_all_images = False
    show = False
    compare_compression = False
    compare_execution_time = False

    image_names = {'dave': 'dave.png',
                   'child': 'child.png',
                   'cat': 'cat.png',
                   'lena': 'lena.png'}

    images_array = {item[0]: np.array(Image.open(f'images/{item[1]}').convert('RGB')) for item in image_names.items()}

    if compress_all_images:
        compression_factor = 100
        for name, path in image_names.items():
            img = images_array[name]
            compressed_img = compress(img, compression_factor=compression_factor)
            PIL_image = Image.fromarray(compressed_img)
            PIL_image.save(f'images/compressed_{compression_factor}_{path}')
            if show:
                PIL_image.show()

    if compare_compression:
        # You can change the following image or the compression factors if wanted
        key = 'child'
        img, img_path = images_array[key], image_names[key]
        compression_factors = [2, 5, 10, 50, 100, 500, 1000, 5000]
        for compression_factor in compression_factors:
            compressed_img = compress(img, compression_factor=compression_factor)
            PIL_image = Image.fromarray(compressed_img)
            PIL_image.save(f'images/compressed_{compression_factor}_{img_path}')
            if show:
                PIL_image.show()

    if compare_execution_time:
        max_power = 15
        sizes = [2**n for n in range(max_power)]
        runs = 100
        # delta times => [0]: fft, [1]: fft_inplace, [2]: np.fft.fft
        dt = [[], [], []]

        for size in sizes:
            for index, function in enumerate([fft, fft_inplace, np.fft.fft]):
                aux = 0
                for i in range(runs):
                    arr = np.random.randn(size)
                    initial = time.time()
                    function(arr)
                    final = time.time()
                    aux += final - initial
                dt[index].append(aux / runs)

        for deltas, name in zip(dt, ['fft', 'fft_inplace', 'np.fft.fft']):
            print(f'times for {name}')
            for i in range(max_power):
                print(f'n = {2**i} -> time (ms): {deltas[i] * 1_000}')

    print([img.shape for img in images_array.values()])


if __name__ == '__main__':
    main()
