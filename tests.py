import unittest
import numpy as np
import fft
import image


class TestFFT(unittest.TestCase):
    def test_fft(self):
        n = 64  # must be a power of two
        x = np.random.randn(n)
        result = fft.fft(x)
        expected = np.fft.fft(x)
        norm = np.linalg.norm(result - expected)

        self.assertIsInstance(result, np.ndarray)
        self.assertAlmostEquals(norm, 0)
    
    def test_ifft(self):
        n = 64  # must be a power of two
        x = np.random.randn(n)
        result = fft.ifft(x)
        expected = np.fft.ifft(x)
        norm = np.linalg.norm(result - expected)

        self.assertIsInstance(result, np.ndarray)
        self.assertAlmostEquals(norm, 0)

    def test_fft_inplace(self):
        n = 64  # must be a power of two
        x = np.random.randn(n)
        result = fft.fft_inplace(x)
        expected = np.fft.fft(x)
        norm = np.linalg.norm(result - expected)

        self.assertIsInstance(result, np.ndarray)
        self.assertAlmostEquals(norm, 0)

    def test_ifft_inplace(self):
        n = 64  # must be a power of two
        x = np.random.randn(n)
        result = fft.ifft_inplace(x)
        expected = np.fft.ifft(x)
        norm = np.linalg.norm(result - expected)

        self.assertIsInstance(result, np.ndarray)
        self.assertAlmostEquals(norm, 0)
    
    def test_fft2(self):
        n1, n2 = 16, 64  # must be powers of two
        x = np.random.randn(n1, n2)
        result = fft.fft2(x)
        expected = np.fft.fft2(x)
        norm = np.linalg.norm(result - expected)
        
        self.assertIsInstance(result, np.ndarray)
        self.assertAlmostEquals(norm, 0)

    def test_ifft2(self):
        n1, n2 = 16, 64  # must be powers of two
        x = np.random.randn(n1, n2)
        result = fft.ifft2(x)
        expected = np.fft.ifft2(x)
        norm = np.linalg.norm(result - expected)

        self.assertIsInstance(result, np.ndarray)
        self.assertAlmostEquals(norm, 0)


class TestImage(unittest.TestCase):

    def compress_basic(self, function, size):
        compress_fac = 10
        img = np.random.randint(low=0, high=256, size=size)
        result = function(img, compress_fac)

        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, size)
        self.assertIs(result.dtype, np.dtype('uint8'))
        self.assertLessEqual(np.max(result), 255)
        self.assertGreaterEqual(np.min(result), 0)

    def test_compress_monotone(self):
        self.compress_basic(image.compress_monotone, (35, 45))

    def test_compress(self):
        self.compress_basic(image.compress, (35, 45, 4))


if __name__ == '__main__':
    unittest.main()
