import unittest
from hello import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, GitHub Actions!")

if __name__ == '__main__':
    unittest.main()
